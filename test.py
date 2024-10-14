import json

# Load the emoji_dict.json file
with open('data/emoji_dict.json', 'r', encoding='utf-8') as f:
    emoji_data = json.load(f)

# Extract emojis and save them to emoji_list.txt
with open('data/emoji_list.txt', 'w', encoding='utf-8') as f:
    for entry in emoji_data:
        emoji = entry.get("emoji")
        if emoji:
            f.write(f"{emoji}\n")

print("emoji_list.txt has been created successfully.")