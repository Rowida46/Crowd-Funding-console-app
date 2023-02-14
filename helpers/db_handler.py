from . import *
import json

dir = "data"
users_file ="user_data.json"
users_file = f"{dir}/{users_file}"
 
with open(users_file) as json_file:
    users_data = json.load(json_file)


def write_users(data, filename=users_file):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def insert_user(user):
    print("inside insert")
    if is_file(users_file):
        with open(users_file, "r+") as  json_file:
            users_data = json.load(json_file)
            users_data.append(user)
            json_file.seek(0)
            json.dump(users_data, json_file)

    