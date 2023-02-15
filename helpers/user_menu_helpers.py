def authenticate_user():
    try:
        decision = int(input(f'please login or register first : \n '
                             f'Enter 1 for Login.\n'
                             f' Enter 2 for Register. \n'
                             f' type here : '))
        return decision
    except:
        print("invalid, try again ")
        authenticate_user()


def asking_for_project_action(user_name):
    try:
        decision = int(input(f'please {user_name} choose what do you want to do : \n '
                             f'Enter 1 for creating new project.\n'
                             f' Enter 2 for viewing all projects. \n'
                             f' Enter 3 for deleting one of your projects.\n'
                             f' Enter 4 for update a project all projects. \n'
                             f' type here : '))
        return decision

    except:
        print("invalid, try again ")
        asking_for_project_action(user_name)
