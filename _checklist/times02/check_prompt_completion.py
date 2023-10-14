import json
import time
import select
import sys

json_file_path = '/Users/nguyennhathung/dspp/_checklist/times02/generate_by_gpt3.0.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data):
    print("========================== " +
          str(index + 2) + " times ==========================")
    print(item['completion'])

    if index < len(data) - 1:
                # Wait for either user input or a timeout of 5 seconds
        rlist, _, _ = select.select([sys.stdin], [], [], 5)

        if rlist:
            user_input = input()  # User pressed Enter
        else:
            
            time.sleep(3)
