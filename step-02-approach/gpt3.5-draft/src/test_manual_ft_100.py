import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/step-02-approach/gpt3.5-draft/assets/resources/dataset_manual_200.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    prompt = "Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent.\n\nNotes when classifying:\n+ Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides.\n+ Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it.\n+ Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided.\n\nNote: always gives me the result (0 or 1) in the form below:\nIncomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)\n\nBelow is information for 2 parts:\n1. Data Safety - Share section: No data shared with third parties;\n2. Privacy Policy - Share section: The sharing information section from the given content is:\nWho we share your data with\nSuggested text: If you request a password reset, your IP address will be included in the reset email."
    print(prompt)
    answer = openai.Completion.create(
        model='ft:davinci-002:imutably-oy::86Mif1SU',
        prompt=prompt,
        temperature=1.0,
        max_tokens=1000,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )

    print("==============================")
    print(answer)

# with open('dataset_predict.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)
