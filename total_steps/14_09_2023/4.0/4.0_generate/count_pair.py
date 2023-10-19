# Import the necessary library to work with JSON data
import json

# Define the file path for the JSON file to read (provide the actual path)
json_file_path = ''

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    # Load the contents of the JSON file into the 'data' variable
    data = json.load(file)

# Loop through each item in the loaded JSON data
for index, item in enumerate(data):
    # Print the index (starting from 1) to identify each item
    print(index + 1)
