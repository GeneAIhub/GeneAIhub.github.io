import os
print("Running main.py")
print("GOOGLE_SCHOLAR_ID =", os.getenv("GOOGLE_SCHOLAR_ID"))
from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime



# Checking if GOOGLE_SCHOLAR_ID is set
google_scholar_id = os.getenv("GOOGLE_SCHOLAR_ID")
if not google_scholar_id:
    print("GOOGLE_SCHOLAR_ID is not set!")
    exit(1)

print("Running main.py")
print("GOOGLE_SCHOLAR_ID =", google_scholar_id)

# Try fetching the author data
try:
    author = scholarly.search_author_id(google_scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
except Exception as e:
    print(f"Error occurred while fetching author data: {e}")
    exit(1)


# name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
print("Running main.py")
print("GOOGLE_SCHOLAR_ID =", os.getenv("GOOGLE_SCHOLAR_ID"))
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print("Data saved successfully!")