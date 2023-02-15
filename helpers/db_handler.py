from . import *
import json

from  helpers.validation_helpers import *;

dir = "data"
users_file = "user_data.json"
users_file = f"{dir}/{users_file}"

projects_file = "projects_data.json"
projects_file = f"{dir}/{projects_file}"

# a general function for inserting into files
def insert(file, data):
    if is_file(file):
        with open(file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print("not a valid dir ")

# get details of the given file based on some filtration
def get_details(data, file):
    # file - > working file path (users_file or projects_file)
    # data -> needed data
    if is_file(file):
        with open(file, "r") as json_file:
            file_data = json.load(json_file)
            data_info = check_user(
                data, file_data) if file == users_file else check_project(data, file_data)
        return data_info
    
def ckeck_key(data, key):
    print(key in data)
    return key in data

def edit(data, key , val):
    data[key] = val
    return data

# given a key and its new val of the given element obj of a given index
def update(file ,data, key, val, index):
    updated_data = edit(data, key, val)
    projects[index] = updated_data
    insert(file,projects)

# users staff
with open(users_file) as json_file:
    users = json.load(json_file)

def insert_user(user):
    users.append(user)
    insert(users_file, users)

def check_user(user, users_data):
    return [ele for ele in users_data
            if ele["email"] == user["email"] and
            ele["password"] == user["password"]
            ]

def get_user_details(user):
    return get_details(user, users_file)


# project

with open(projects_file) as json_file:
    projects = json.load(json_file)

def insert_project(project):
    projects.append(project)
    insert(projects_file, projects)

def delet_project(proj):
    filtered_data = filter_project(proj, projects)
    insert(projects_file,filtered_data)

def check_project(proj, projects_file = projects):
    return [(ele,index) for index,ele in enumerate(projects_file)
            if ele["title"] == proj["title"]]

def filter_project(proj, projects_data):
    return [ele for ele in projects_data
            if ele["title"] != proj["title"]]

def get_project_details(proj):
    return get_details(proj, projects_file)

def get_key_and_val(project_info):
    key = input("input your key name : ")

    if ckeck_key(project_info, key):
        if key == "budget":
            val = validate_price()
        elif key == "price":
            val = validate_price()
        elif key == "start date" or key == "end date":
            val = validate_date(f"enter {key} date in format dd/mm/yy :  ")
        elif key == "title":
            val = get_proj_title()
        else:
            val = input("your project details , u can skip this part : ")
        return key, val
    else :
        print("Key not found ")
        get_key_and_val(project_info)
    return 0,0


def update_project_details(project_info):
    proj_data, index = project_info

    key,val = get_key_and_val(proj_data)
    if key and val:
        update(projects_file,proj_data, key, val, index)
        print("project updated successfully ! ")
    else :
        print("not a valid edit process ")
    return

def get_user_projs(id):
    with open(projects_file, "r") as json_file:
        file_data = json.load(json_file)
        #print([ele for ele in file_data if ele["user_id"] == id])
        user_projects = [ele for ele in file_data if ele["user_id"] == id]
    
    return user_projects
   