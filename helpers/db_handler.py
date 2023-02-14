from . import *
import json

dir = "data"
users_file = "user_data.json"
users_file = f"{dir}/{users_file}"

"""
with open(users_file) as json_file:
    users_data = json.load(json_file)
"""


def insert_user(user):
    print("inside insert")
    if is_file(users_file):
        with open(users_file, "r+") as json_file:
            users_data = json.load(json_file)
            users_data.append(user)
            json_file.seek(0)
            json.dump(users_data, json_file)


def search(user, users_data):
    return [ele for ele in users_data 
        if ele["email"]== user["email"] and 
        ele["password"] == user["password"]
    ]

def search_user(user):
    print("inside search")
    if is_file(users_file):
        with open(users_file, "r") as  json_file:
            users_data = json.load(json_file)
            user_info = search(user, users_data)
        return user_info
    