import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/step-02/gpt3.5/assets/dataset_manual_01.json'

openai.api_key = os.getenv("OPENAI_API_KEY")

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    prompt = item.get("prompt")
    print("========================== " +
          str(index) + " ==========================")
    print(prompt)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."},
            {"role": "user", "content": prompt} 
        ]
    )

    assistant_reply = response.choices[0].message['content']

    print("============================================")
    print(assistant_reply)

with open('dataset_random.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
