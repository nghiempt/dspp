import json

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/_checklist/times02/generate_by_gpt3.0.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index + 2) + " times ==========================")
    print(item['completion'])

    if (index > 5):
        break
