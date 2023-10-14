import json

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/task/bard/output.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index) + " times ==========================")
    print(item['completion'])
