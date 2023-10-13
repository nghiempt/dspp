import json

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/step-01-dataset/assets/json/dataset_random_250.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print(index + 1)