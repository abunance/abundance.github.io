
# Read file.txt
with open('file.txt', 'r') as file:
    text = file.read()


# Delete text and Write
with open('file.txt', 'w') as file:
    # Delete
    new_text = text.replace('{"type":"Point","coordinates":', '')
    new_text = text.replace('}', '')
    # Write
    file.write(new_text)
