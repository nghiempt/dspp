import json

# Input JSON file path
input_json_file = '/Users/nghiempt/Corporation/scientific_research/paper_policy/case_04_gpt4.0/fine_tuning/100_second_manual_train3.json'

# Output JSONL file path
output_jsonl_file = '/Users/nghiempt/Corporation/scientific_research/paper_policy/case_04_gpt4.0/fine_tuning/100_second_manual_train3.jsonl'

# Open the input JSON file for reading and the output JSONL file for writing
with open(input_json_file, 'r') as json_file, open(output_jsonl_file, 'w') as jsonl_file:
    # Load the entire JSON file as a list of JSON objects
    data = json.load(json_file)
    
    # Iterate through the list of JSON objects
    for item in data:
        # Serialize each object as a JSON string and write it to the JSONL file followed by a newline character
        jsonl_file.write(json.dumps(item) + '\n')
