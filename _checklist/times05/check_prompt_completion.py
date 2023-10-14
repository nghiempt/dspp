import json

json_file_path = 'ft_3.5.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    if index < 200:
        continue
    print("========================== " +
          str(index + 2) + " times ==========================")
    print(item['completion'])

    # if (index > 200):
    #     break
