import json

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/task/hungnn_llama/hungnn_llama_nodejs/input.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print(index + 1)