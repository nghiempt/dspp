import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/step-02-approach/gpt3.5-draft/assets/resources/dataset_manual_100.json'

openai.api_key = os.getenv("OPENAI_API_KEY")

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    prompt = item.get("prompt")
    print("========================== " +
          str(index) + " times ==========================")
    response = openai.ChatCompletion.create(
        model=os.getenv("MODEL_GPT3.5"),
        messages=[
            {"role": "system", "content": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."},
            {"role": "user", "content": prompt} 
        ]
    )
    assistant_reply = response.choices[0].message['content']
    item["completion"] = assistant_reply
    print(assistant_reply)

with open('/Users/nghiempt/Corporation/scientific_research/paper_policy/step-02-approach/gpt3.5-draft/assets/results-after-fine-tuned/result_manual_100.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
