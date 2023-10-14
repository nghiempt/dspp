import json

input_json_file = '/Users/nghiempt/Corporation/scientific_research/paper_policy/_checklist/fine_tune_by_bard.json'

output_jsonl_file = '/Users/nghiempt/Corporation/scientific_research/paper_policy/_checklist/fine_tune_by_bard.jsonl'

with open(input_json_file, 'r') as json_file, open(output_jsonl_file, 'w') as jsonl_file:
    data = json.load(json_file)
    
    for item in data:
        jsonl_file.write(json.dumps(item) + '\n')
