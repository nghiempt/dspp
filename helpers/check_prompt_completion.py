import json

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/14_09_2023/bard/bard_generate/input1.3.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index) + " times ==========================")
    print(item['package_name'])
