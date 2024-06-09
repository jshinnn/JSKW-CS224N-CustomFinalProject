import json

# TODO: REPLACE WITH APPROPRIATE FILE PATH
with open('', 'r') as file:
    lines = file.readlines()

data = []
current_entry = {}

for line in lines:
    line = line.strip()
    if line.startswith("user:"):
        # if there's an existing entry, save it
        if current_entry:
            data.append(current_entry)
        # split the line into user and assistant parts if they are on the same line
        if 'assistant:' in line:
            user_part, assistant_part = line.split('assistant:', 1)
            current_entry = {"user": user_part[len("user:"):].strip(), "assistant": assistant_part.strip()}
        else:
            current_entry = {"user": line[len("user:"):].strip(), "assistant": ""}
    elif line.startswith("assistant:"):
        current_entry["assistant"] = line[len("assistant:"):].strip()
    else:
        if "assistant" in current_entry:
            current_entry["assistant"] += " " + line.strip()
        else:
            current_entry["assistant"] = line.strip()

if current_entry:
    data.append(current_entry)

json_data = json.dumps(data, indent=4)

# TODO: REPLACE WITH APPROPRIATE FILE PATH
with open('', 'w') as json_file:
    json_file.write(json_data)