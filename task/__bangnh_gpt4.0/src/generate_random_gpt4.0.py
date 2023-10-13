import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

json_file_path = 'assets/dataset_random_prompt_only.json'

openai.api_key = os.getenv("OPENAI_API_KEY")

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    prompt = item.get("prompt")
    print("========================== " +
          str(index) + " times ==========================")
    response = openai.ChatCompletion.create(
        model=os.getenv("MODEL_GPT4.0"),
        messages=[
            {"role": "system", "content": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."},
            {"role": "user", "content": prompt} 
        ]
    )
    assistant_reply = response.choices[0].message['content']
    item["completion"] = assistant_reply
    print(assistant_reply)

with open('assets/dataset_random_gpt4.0.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
