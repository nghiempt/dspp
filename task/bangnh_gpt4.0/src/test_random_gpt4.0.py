# Import necessary libraries
import requests                # Used to send HTTP requests
import json                    # To handle JSON data
import openai                  # OpenAI library to interact with their API, although not used directly in this snippet
from dotenv import load_dotenv # To load environment variables from a .env file
import os                      # To interact with the operating system, especially for fetching environment variables

# Load environment variables from the .env file
load_dotenv()

# Define the OpenAI chat completions API endpoint
url = "https://api.openai.com/v1/chat/completions"

# Set up the headers for HTTP requests, including authorization and content type
headers = {
    "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
    "Content-Type": "application/json",
}

# Define the file path of the JSON file to read
json_file_path = '../assets/result_random_gpt4.0.json'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    dataJson = json.load(file)

# Loop through each item in the loaded data
for index, item in enumerate(dataJson):
    print("======================== " + str(index) + " times ========================")

    # Define the payload to send to OpenAI's chat completions endpoint
    # This format uses a "system" message to guide the assistant's behavior and a "user" message containing the prompt to be completed.
    data = {
        "model": os.getenv("GPT3.5_FT_BY_GPT4.0"),
        "messages": [
            {
                "role": "system",
                "content": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."
            },
            {
                "role": "user",
                "content": item["prompt"]
            }
        ]
    }

    # Send a POST request to the OpenAI API with the defined headers and data
    response = requests.post(url, headers=headers, json=data)

    # Check the status code of the response
    if response.status_code == 200:  # HTTP status 200 means the request was successful
        # Parse the completion from the response and save it to the item
        item["completion"] = response.json().get("choices")[0].get("message").get("content")
        print("======================== Successfully ========================\n")
    else:  # The request was not successful
        print("======================== Failed ========================")

# Save the updated data (with completions) back into the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(dataJson, json_file, indent=4)
