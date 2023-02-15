from helpers.validation_helpers  import *;
from helpers.file_handler import *;
from helpers.db_handler import *;

def create_project(user_id):
    project_info = get_project_info(user_id)
    try:
        insert_project(project_info)
    except Exception as  e:
        print(e)
    else :   
        print(f"your project {project_info['title']} created succesfully ! ")
    print()


def delete_project():
    title = get_proj_title()
    if check_project({"title" : title}):
        delet_project({"title" : title}) 
        print("project deleted successfully !")
    else :
        print(f'a project with this {title} title not found.')
    print()


def view_user_projects(id):
    user_projects =  get_user_projs(id)
    print()
    msg = " Here are a sample of your projects \n -------------------       " if user_projects else ""
    print(msg)
    for i,proj in enumerate(user_projects):
        print(f'{i+1} - project with {proj["title"]} has a budget of {proj["budget"]} . ')

def update_project():
    title = get_proj_title()
    project_info = get_project_details({"title":title})
    if project_info:
        project_info = project_info[0]
        print(f'your project details is title : { project_info[0]["title"]} with budget {project_info[0]["budget"]}')   
        update_project_details(project_info)
    else :
        print("project not found !  ")
    print()


#create_project()
#update_project()

#delete_project()
