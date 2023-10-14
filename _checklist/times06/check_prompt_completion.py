import json

json_file_path = 'llama_generate.json'


with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

for index, item in enumerate(data):
    if index < 200:
        continue
    print("========================== " +
          str(index + 2) + " times ==========================")
    print(item['completion'])

    
