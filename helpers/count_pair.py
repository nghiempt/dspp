import json

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/task/manual/dataset_manual_200.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print(index + 1)