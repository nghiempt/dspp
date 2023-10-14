# Import necessary libraries
import json
import openai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Set the OpenAI API key using the value from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate text using the OpenAI GPT-3.0 model
completion = openai.Completion.create(
    model=os.getenv("MODEL_GPT3.0"),
    prompt="Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent.\nNotes when classifying:\n+ Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides.\n+ Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it.\n+ Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided.\nNote: always gives me the result (0 or 1) in the form below:\nIncomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)\nBelow is information for 2 parts:\nData Safety - Share section: No data shared with third parties;\nPrivacy Policy - Share section: The sharing information section of the content is not clearly defined. However, the following excerpt may pertain to sharing information:\n\"We use the information we collect in various ways, including to:\n- Communicate with you, either directly or through one of our partners, including for customer service, to provide you with updates and other information relating to the website, and for marketing and promotional purposes\n- Send you emails\"\nPlease note that this is a general interpretation and the entire content should be reviewed for a comprehensive understanding of the sharing information section.",
    n=1,
    stop=None,
    temperature=1.0,
    max_tokens=150
)

# Extract the generated text from the API response
generated_text = completion.choices[0].text

print(generated_text)
