# from scholarly import scholarly
# import jsonpickle
# import json
# from datetime import datetime
# import os
#
# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
# name = author['name']
# author['updated'] = str(datetime.now())
# author['publications'] = {v['author_pub_id']:v for v in author['publications']}
# print(json.dumps(author, indent=2))
# os.makedirs('results', exist_ok=True)
# with open(f'results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)
#
# shieldio_data = {
#   "schemaVersion": 1,
#   "label": "citations",
#   "message": f"{author['citedby']}",
# }
# with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)
import os
import requests
import json
from datetime import datetime


def fetch_all_scholar_data(scholar_id: str, api_key: str) -> dict:
    """
    使用SerpApi获取一位作者的全部学术信息，包括所有出版物。
    """
    all_articles = []
    page_num = 0

    # 1. 先进行第一次API调用，获取作者基本信息和第一页的文章
    print("正在向 SerpApi 发送初始请求，获取作者基本信息...")
    params = {
        "engine": "google_scholar_author",
        "author_id": scholar_id,
        "api_key": api_key,
    }
    response = requests.get("https://serpapi.com/search.json", params=params)

    if response.status_code != 200:
        print(f"错误：初始API请求失败，状态码: {response.status_code}")
        print("返回内容:", response.text)
        return None

    data = response.json()
    print("初始请求成功！")

    # 保存作者的基础信息和引用统计，这部分内容在每次分页请求中都一样
    author_info = data.get('author', {})
    cited_by_info = data.get('cited_by', {})

    # 将第一页的文章加入列表
    articles_on_page = data.get('articles', [])
    if articles_on_page:
        all_articles.extend(articles_on_page)
    print(f"已获取第 {page_num + 1} 页的文章，共 {len(articles_on_page)} 篇。")

    # 2. 处理分页，循环获取所有出版物
    while "next" in data.get("serpapi_pagination", {}):
        page_num += 1
        print(f"正在获取第 {page_num + 1} 页的文章...")

        # 获取下一页的链接并发起请求
        next_page_url = data["serpapi_pagination"]["next"]
        response = requests.get(next_page_url, params={"api_key": api_key})

        if response.status_code != 200:
            print(f"错误：获取第 {page_num + 1} 页时请求失败，状态码: {response.status_code}")
            break  # 如果某一页失败，则停止继续获取

        data = response.json()
        articles_on_page = data.get('articles', [])
        if not articles_on_page:
            # 如果某一页没有文章了，就停止
            print("当前页没有文章，停止获取。")
            break

        all_articles.extend(articles_on_page)
        print(f"已获取第 {page_num + 1} 页的文章，共 {len(articles_on_page)} 篇。")

    print(f"\n所有出版物获取完毕，总共 {len(all_articles)} 篇。")

    # 3. 整合所有数据，构建与原来脚本结构相同的字典
    final_data = {
        'container_type': 'author',
        'name': author_info.get('name'),
        'affiliation': author_info.get('affiliations'),
        'interests': [i['title'] for i in author_info.get('interests', [])],
        'email_domain': author_info.get('email', '').split('@')[-1] if '@' in author_info.get('email', '') else '',
        'filled': ['basics', 'indices', 'counts', 'publications'],  # 模拟scholarly库的状态
        'scholar_id': scholar_id,
        'citedby': cited_by_info.get('total'),
        'hindex': cited_by_info.get('h_index'),
        'i10index': cited_by_info.get('i10_index'),
        'citedby5y': cited_by_info.get('h_index_5_year'),  # 注意：SerpApi可能字段名不同，此处为示例
        'hindex5y': cited_by_info.get('h_index_5_year'),
        'i10index5y': cited_by_info.get('i10_index_5_year'),
        # 将出版物列表重组为以 citation_id 为键的字典，模拟原来的 'author_pub_id'
        'publications': {v['citation_id']: v for v in all_articles},
        'updated': str(datetime.now())  # 添加时间戳
    }

    return final_data


def main():
    """
    主函数：获取环境变量，调用API，并生成JSON文件。
    """
    # 从GitHub Secrets获取ID和API Key
    scholar_id = os.getenv('GOOGLE_SCHOLAR_ID')
    api_key = os.getenv('SERPAPI_API_KEY')
    print(f"GOOGLE_SCHOLAR_ID {scholar_id}, SERPAPI_API_KEY {api_key}")
    # if not scholar_id or not api_key:
    #     print("错误：请确保在GitHub Secrets中设置了 GOOGLE_SCHOLAR_ID 和 SERPAPI_API_KEY")
    #     exit(1)

    # 调用主函数获取数据
    author_data = fetch_all_scholar_data(scholar_id, api_key)

    if author_data:
        # 打印到控制台，方便调试
        print("\n最终生成的作者数据结构：")
        print(json.dumps(author_data, indent=2, ensure_ascii=False))

        # 确保results目录存在
        os.makedirs('results', exist_ok=True)

        # 写入gs_data.json文件
        with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(author_data, outfile, ensure_ascii=False, indent=4)
        print("\n已成功生成 results/gs_data.json")

        # 准备并写入用于Shields.io的JSON文件
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(author_data.get('citedby', 0)),  # 使用 str() 转换
            "color": "brightgreen"  # 可以自定义颜色
        }
        with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
            json.dump(shieldio_data, outfile, ensure_ascii=False, indent=4)
        print("已成功生成 results/gs_data_shieldsio.json")


if __name__ == "__main__":
    main()