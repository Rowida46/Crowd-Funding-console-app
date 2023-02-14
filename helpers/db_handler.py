from . import *
import json

dir = "data"
users_file ="user_data.json"
users_file = f"{dir}/{users_file}"
 
with open(users_file) as json_file:
    users_data = json.load(json_file)

def insert_user(user):
    print("inside insert")
    if is_file(users_file):
        with open(users_file) as json_file:
            users_data = json.load(json_file)
            print(users_data)
            users_data.append(user)
    