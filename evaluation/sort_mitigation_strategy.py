import json
import re

# TODO: REPLACE WITH APPROPRIATE FILE PATH
with open('', 'r') as file:
    lines = file.readlines()

data = []
current_entry = {}

combined_text = " ".join([line.strip() for line in lines])

entries = re.split(r'(<system>.*?)(?=<system>|$)', combined_text)
entries = [entry for entry in entries if entry.strip()]  

for entry in entries:
    if entry.startswith("<system>"):
        if current_entry:
            data.append(current_entry)
        current_entry = {
            "system": "",
            "user": "",
            "assistant": ""
        }
        # extract system part
        system_part_match = re.search(r'<system>(.*?)(?=user:|$)', entry, re.DOTALL)
        if system_part_match:
            current_entry["system"] = system_part_match.group(1).strip()
        # extract user part
        user_part_match = re.search(r'user:(.*?)(?=assistant:|$)', entry, re.DOTALL)
        if user_part_match:
            current_entry["user"] = user_part_match.group(1).strip()
        # extract assistant part
        assistant_part_match = re.search(r'assistant:(.*)', entry, re.DOTALL)
        if assistant_part_match:
            current_entry["assistant"] = assistant_part_match.group(1).strip()

if current_entry:
    data.append(current_entry)

json_data = json.dumps(data, indent=4)

# TODO: REPLACE WITH APPROPRIATE FILE PATH
with open('', 'w') as json_file:
    json_file.write(json_data)
