import json

json_file_path = 'ft_3.5_m2.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index + 2) + " times ==========================")
    print(item['completion'])

    # if (index > 98):
    #     break
