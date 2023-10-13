# Import necessary libraries
import requests                # Used to send HTTP requests
import json                    # To handle JSON data
from dotenv import load_dotenv  # To load environment variables from a .env file
# To interact with the operating system, especially for fetching environment variables
import os

# Load environment variables from the .env file
load_dotenv()

# Define the API endpoint URL
url = "https://www.llama2.ai/api"

# Define the headers, including the authorization token
headers = {
    # "Authorization": "Bearer " + os.getenv("LLAMA_API_KEY"),
    "Content-Type": "application/json",  # Adjust the content type as needed
}

# Define the file path of the JSON file to read
json_file_path = '../assets/dataset_random_prompt_only.json'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    dataJson = json.load(file)

# Loop through each item in the loaded data
for index, item in enumerate(dataJson):
    print("======================== " + str(index) +
          " times ========================")

    # Define the request body as a dictionary (you can also use JSON)
    data = {
        "prompt": "[INST] Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent.\nNotes when classifying:\n+ Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides.\n+ Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it.\n+ Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided.\nNote: always gives me the result (0 or 1) in the form below:\nIncomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)\nBelow is information for 2 parts:\nData Safety - Share section: Personal info(Name, User IDs, Sexual orientation, Other info), Messages(Other in-app messages), Photos and videos(Photos, Videos), App activity(App interactions, Other user-generated content), App info and performance(Crash logs, Diagnostics), Device or other IDs(Device or other IDs);\nPrivacy Policy - Share section: The sharing information section from the given content is as follows:\nHow we share your Personal Information\nWe may share your personal information with the following third parties and as otherwise described in this Privacy Policy or at the time of collection:\n- Service providers. Companies and individuals that provide services on our behalf or help us operate the Service or our business.\n- Third party platforms. Social media and other third party platforms that you connect to the Service.\n- The public. Other users of the Service and the public, when you disclose personal information for public use.\n- Professional advisors. Professional advisors, such as lawyers, bankers, auditors and insurers.\n- Authorities and others. Law enforcement, government authorities, and private parties, as we believe in good faith to be necessary or appropriate to comply with law or for the compliance, fraud prevention and safety purposes described above. [/INST]",
        "version": "2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
        "systemPrompt": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store.",
        "temperature": 0.75,
        "topP": 0.9,
        "maxTokens": 800,
        "image": "null"
    }

    # Send a POST request to the OpenAI API with the defined headers and data
    response = requests.post(url, headers, json=data)

    # Check the status code of the response
    if response.status_code == 200:  # HTTP status 200 means the request was successful
        # Parse the completion from the response and save it to the item
        item["completion"] = response.json()[0].get("generated_text")
        print(response)
        print("======================== Successfully ========================\n")
    else:  # The request was not successful
        print(response)
        print("======================== Failed ========================")

# Save the updated data (with completions) back into the JSON file
with open('../assets/dataset_random_prompt_llama.json', 'w') as json_file:
    json.dump(dataJson, json_file, indent=4)
