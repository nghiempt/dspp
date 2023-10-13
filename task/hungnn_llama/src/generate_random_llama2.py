import requests

# Define the API endpoint URL
url = 'https://www.llama2.ai/api'

# Define the payload data as a dictionary
payload = {
    "prompt": "[INST] Hello [/INST]",
    "version": "2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
    "systemPrompt": "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store.",
    "temperature": 0.75,
    "topP": 0.9,
    "maxTokens": 800,
    "image": None
}

# Make a POST request to the API with JSON data
response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response from the API
    data = response.json()
    print(data)
else:
    # If the request was unsuccessful, print an error message
    print('Error: Unable to fetch data from the API')
