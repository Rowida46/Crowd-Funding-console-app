from . import *
import json

dir = "data"
users_file = "user_data.json"
users_file = f"{dir}/{users_file}"

projects_file = "projects_data.json"
projects_file = f"{dir}/{projects_file}"

"""sample of opening json file
with open(users_file) as json_file:
    users_data = json.load(json_file)
"""

# a general function for inserting into files


def insert(file, data):
    print("inside insert")
    if is_file(file):
        with open(file, "r+") as json_file:
            get_data = json.load(json_file)
            get_data.append(data)
            json_file.seek(0)
            json.dump(get_data, json_file) 
          #  , indent=4,  separators=(',',': '))
    else:
        print(file)
        print("not a valid dir ")


def get_details(data, file):
    # file - > working file path (users_file or projects_file)
    # data -> needed data
    print("inside search")
    if is_file(file):
        print(file)
        with open(file, "r") as json_file:
            file_data = json.load(json_file)
            data_info = check_user(
                data, file_data) if file == users_file else check_project(data, file_data)
        return data_info

# users staff
def insert_user(user):
    print(user)
    insert(users_file, user)


def check_user(user, users_data):
    return [ele for ele in users_data
            if ele["email"] == user["email"] and
            ele["password"] == user["password"]
            ]


def get_user_details(user):
    return get_details(user, users_file)


# project

def insert_project(project):
    insert(projects_file, project)

""" def delet_proj(proj):
    print()
    with open(projects_file,'r+') as json_file:
        file_data = json.load(json_file)
        filtered_data = filter_project(proj, file_data)
        json_file.seek(0)
        insert_project(filtered_data)

 """
def delet_proj(proj):
    if is_file(projects_file):
        with open(projects_file, "r+") as json_file:
            get_data = json.load(json_file)
            filtered_data = filter_project(proj, get_data)
            json_file.seek(0)
            json_file.write(json.dumps(filtered_data))
    else:
        print(projects_file)
        print("not a valid dir ")

""" 

 print(projects_file)

        file_data = json.loads(json_file)
        print('ffff', file_data)
        filtered_data = filter_project(proj, file_data)
        print("filtered", file_data)
        json_file.seek(0)
        json.dump(filtered_data, json_file) """

def check_project(proj, projects_file):
    return [ele for ele in projects_file
            if ele["title"] == proj["title"]]


def filter_project(proj, projects_data):
    print(projects_data)
    print("------------")
    print([ele['title'] != proj['title'] for ele in projects_data])
    print("000000000")
    print([ele for ele in projects_data
            if ele["title"] != proj["title"]])

    return [ele for ele in projects_data
            if ele["title"] != proj["title"]]

def get_project_details(proj):
    return get_details(proj, projects_file)


