import json

input_json_file = 'assets/ft_random_gpt4.0.json'

output_jsonl_file = 'assets/ft_random_gpt4.0.jsonl'

with open(input_json_file, 'r') as json_file, open(output_jsonl_file, 'w') as jsonl_file:
    data = json.load(json_file)
    
    for item in data:
        jsonl_file.write(json.dumps(item) + '\n')
