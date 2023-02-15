from authenticate_user import *
from helpers.user_menu_helpers import *

from project_services import *

# keep on reading till we got unvalid option
def auth():
    while True:
        auth = authenticate_user()
        if auth == 1:
            global USER 
            USER = Login()
            break
        elif auth == 2:
            Register()
            print("U r  now registered !,pleaze log in")   
        else :
            print("not a vaild option try again ! ")
            auth = authenticate_user()

auth()

while True:
    if USER:
        print("---------------------------")
        action = asking_for_project_action(USER["name"])
        if action == 1:
            create_project(USER["id"])
        elif action == 2:
            view_user_projects(USER["id"])
        elif action == 3:
            delete_project()
        elif action == 4:
            update_project()
        else :
            print ("not a valid option")
            break
    else :
        auth()



