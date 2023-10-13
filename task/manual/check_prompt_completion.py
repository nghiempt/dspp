import json

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/task/bangnh_bard/assets/dataset_random_bard.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index) + " times ~~ " + str(item['package_name'])  + " ==========================")
    print(item['completion'])
    if (index > 2):
        break

# >>>>> Incorrect: 1\nIncomplete: 1\nInconsistent: 1 <<<<<
