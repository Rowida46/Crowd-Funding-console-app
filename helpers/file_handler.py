import os 

# working on   `data` folder 
dir = "data"

def create_initial_setup():
    if not os.path.isdir(dir):
        os.mkdir(dir)
    else:
        print("folder found")
    

def is_file(file_name):
    return os.path.exists(file_name)

create_initial_setup()
