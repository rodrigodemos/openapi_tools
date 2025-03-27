import datetime
import json
import os
import sys

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print("Usage: python ado_openapi_aiagents_prep.py <specfile>")
        sys.exit(1)
    file = sys.argv[1]
    # Load the JSON file

    file_path = os.path.join(os.path.dirname(__file__), file)
    data = load_json_file(file_path)

    for item in data['paths']:
        for operation in data['paths'][item]:
            #remove spaces from all the operationId values
            data['paths'][item][operation]['operationId'] = data['paths'][item][operation]['operationId'].replace(" ", "_")
            # print(data['paths'][item][operation]['operationId'])

    # Remove all the x-ms-examples from the JSON file
    for item in data['paths']:
        for operation in data['paths'][item]:
            if 'x-ms-examples' in data['paths'][item][operation]:
                del data['paths'][item][operation]['x-ms-examples']
    
    # Save file with same name and the current timestamp suffix in yyyymmdd_hhmmss format
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    new_file_path = os.path.join(os.path.dirname(__file__), f"{timestamp}_{file}")
    save_json_file(new_file_path, data)