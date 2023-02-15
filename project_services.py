from helpers.validation_helpers  import *;
from helpers.file_handler import *;
from helpers.db_handler import *;

def create_project():
    project_info = get_project_info()
    try:
        insert_project(project_info)
    except Exception as  e:
        print(e)
    else :
        
        print(f"your project {project_info['title']} created succesfully ! ")


def delete_project():
    title = get_proj_title()
    delet_proj({"title" : title})  

create_project()

delete_project()
