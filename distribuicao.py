import json
from collections import Counter
import os

main_json = 'Datasets/bugLocationDappScan.json'
real_base = 'Datasets/DAppSCAN-main/DAppSCAN-source/'

with open(main_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

category_list = []

for item in data:
    relative_location = item['location'].replace("\\", os.sep).replace("/", os.sep)
    location = os.path.join(real_base, relative_location)
    try:
        with open(location, 'r', encoding='utf-8') as f_swcs:
            swc_json = json.load(f_swcs)
            if 'SWCs' in swc_json and isinstance(swc_json['SWCs'], list):
                for swc in swc_json['SWCs']:
                    if 'category' in swc:
                        category_list.append(swc['category'])
    except Exception as e:
        print(f"Could not read {location}: {e}")

# Count
counts = Counter(category_list)
total = sum(counts.values())

print("SWC Category\tCount\tPercent")
for k, v in counts.most_common():
    percent = 100 * v / total
    print(f"{k}\t{v}\t{percent:.2f}%")
