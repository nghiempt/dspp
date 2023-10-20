import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

information = "1. Data Safety - Share section: No data shared with third parties\nPrivacy Policy - Share section: The sharing information section mentions IP address being shared if a password reset is requested.\n\nIncomplete: 1\nIncorrect: 0\nInconsistency: 0\n\n2. Data Safety - Share section: No data shared with third parties\nPrivacy Policy - Share section: No mention of sharing any data.\n\nIncomplete: 0\nIncorrect: 0\nInconsistency: 0"

prompt = "Information: {" + information + "} \nFrom information above. Please summarize for me the result with format: Incomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)."

response = openai.ChatCompletion.create(
    model=os.getenv("MODEL_GPT3.5"),
    messages=[
        {"role": "system", "content": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."},
        {"role": "user", "content": prompt}
    ]
)

assistant_reply = response.choices[0].message['content']

print(assistant_reply)
