import json

username = input("please give us a username:")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)

print(f"We'll remember you when you come back, {username}")