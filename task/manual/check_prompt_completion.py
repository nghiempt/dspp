import json

json_file_path = 'task\manual\dataset_manual_100.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index) + " times ~~ " + str(item['package_name'])  + " ==========================")
    print(item['prompt'])
    if index < len(data) - 1:
        input()

# >>>>> Incorrect: 1\nIncomplete: 1\nInconsistent: 1 <<<<<
