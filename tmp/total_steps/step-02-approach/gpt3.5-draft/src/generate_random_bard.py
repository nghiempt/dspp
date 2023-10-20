# Import the necessary libraries
import json                     # To handle JSON data
from bardapi import Bard        # Custom API wrapper for the "Bard" service
from dotenv import load_dotenv  # To load environment variables from a .env file
import os                       # To interact with the operating system, especially for fetching and setting environment variables

# Load environment variables from the .env file
load_dotenv()

# Set the Bard API key in the environment using the fetched value from the loaded environment variables
os.environ['_BARD_API_KEY'] = os.getenv("BARD_API_KEY")

# Define the file path of the JSON file to read
json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/step-02-approach/gpt3.5-draft/assets/resources/dataset_random_prompt_only.json'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    # Load the contents of the JSON file into the `data` variable
    data = json.load(file)

# Loop through each item in the loaded data
for index, item in enumerate(data):
    print("======================== " + str(index) +
          " times ========================")

    # Instantiate the Bard object with a timeout of 10 seconds for API requests
    bard = Bard(timeout=10)
    
    # Extract the "prompt" key from the item
    prompt = item.get("prompt")
    
    # Fetch an answer from Bard using the prompt and extract the 'content' from the response
    response = bard.get_answer(prompt)['content']

    # Update the "completion" key of the item with the fetched response
    item["completion"] = response

    print("============================== Successfully ==============================\n")

# Save the updated data (now with completions from Bard) back into the JSON file
# The data is saved with an indentation of 4 spaces for better readability
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
