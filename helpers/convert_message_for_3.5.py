import json

input_json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/_checklist/dataset_manual_200.json'
output_json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/_checklist/fine_tune_by_m200.json'

with open(input_json_file_path, 'r') as input_file:
    data = json.load(input_file)

new_data = []

for pair in data:
    prompt = pair["prompt"]
    completion = pair["completion"]

    new_entry = {
        "messages": [
            {
                "role": "system",
                "content": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."
            },
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": completion
            }
        ]
    }

    new_data.append(new_entry)

with open(output_json_file_path, 'w') as output_file:
    json.dump(new_data, output_file, indent=4)

print("New json file created!")
