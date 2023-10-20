import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

json_file_path = '../assets/dataset_random_prompt_only2.json'

openai.api_key = os.getenv("OPENAI_API_KEY")

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index) + " times ==========================")
    prompt = item.get("prompt")

    completion = openai.Completion.create(
        model=os.getenv("MODEL_GPT3.0"),
        prompt=prompt,
        n=1,
        stop=None,
        temperature=1.0,
        max_tokens=150
    )

    generated_text = completion.choices[0].text
    item["completion"] = generated_text

    print(generated_text)


with open('../assets/dataset_random_gpt3.0.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
