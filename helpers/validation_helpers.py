import time
from pyclbr import Function


def validate_email():
    import re
    email = input("your email address : ")
    expr = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(expr, email):
        print("not a valid emaill addres")
        email = validate_email()
    return email


def get_user_name():
    name = input("input your username : ")
    if any(chr.isdigit() for chr in name) or not name:
        print(" not a valid user name ")
        name = get_user_name()
    return name


def validate_password(msg=''):
    password = input(msg)
    while len(password) < 4:
        password = validate_password(
            "min lenth is 4, enter a valid password : ")
    return password


def get_user_passwords(login=False):
    password1 = validate_password("enter your paassword : ")
    password2 = validate_password(
        "confirm your password : ") if not login else ''
    return password1, password2


def confirm_password(password1, password2):
    while password1 != password2:
        print("password dnt match ! ")
        password1, password2 = get_user_passwords()
    print("password confirmed succesfully ! ")
    return password1, password2


def validate_phone_number(phone_number):
    return len(phone_number) == 11 and all(num.isdigit() for num in phone_number)


def get_user_phone_number(msg="enter your phone number : "):
    phone_number = input(msg)
    while not validate_phone_number(phone_number):
        phone_number = get_user_phone_number(
            "not a valid egyption phone number : ")
    return phone_number


def validate_user_registration_info():
    name = get_user_name()
    email = validate_email()
    password1, password2 = get_user_passwords()
    password1, password2 = confirm_password(password1, password2)
    phone_number = get_user_phone_number()

    user_info = {"id": round(time.time()),
                 "name": name, "email": email, "phone_number": phone_number,
                 "password": password1}

    return user_info


def validate_user_login_info():
    email = validate_email()
    password, _ = get_user_passwords(login=True)
    user_info = {"email": email, "password": password}
    return user_info


# project related staff 

def get_proj_title():
    name = input("input your project title : ")
    if any(chr.isdigit() for chr in name) or not name:
        print(" not a valid prject name ")
        name = get_proj_title()
    return name

date_regx = '^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'

import datetime;

def validate_date(msg='enter date in format dd/mm/yy : '):
    date, is_valid_date = input(msg), True
   
    d, m, y = date.split("/")
    try:
        datetime.datetime(int(y), int(m), int(d))
    except ValueError:
        is_valid_date = False
        print("not a valid date format ! ")
        data = validate_date()
    return date

def validate_price(msg="your target (i.e 250000 EGP)  : "):
    budget = input(msg)
    while not any(num.isdigit() for num in budget):
        budget = validate_price(
            "not a valid price  number : ")
    return budget

def get_project_info():
    title = get_proj_title()
    desc = input("your project details , u can skip this part : ")
    budget = validate_price()
    # Set start/end time for the campaign (validate the date formula
    start = validate_date("enter start date in format dd/mm/yy  : ")
    end = validate_date("enter end date in format dd/mm/yy :  ")

    project_info = {"title" : title, "description" : desc, 
        "budget" : budget , "start date" : start , "end date" : end}
    return project_info


