import time

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
    if any(chr.isdigit() for chr in  name) or not name:
        print(" not a valid user name ")
        name = get_user_name()
    return name

def validate_password(msg=''):
    password = input(msg)
    while len(password) < 4 :
        password = validate_password("min lenth is 4, enter a valid password : ")
    return password
    
    
def get_user_passwords(login=False):
    password1 = validate_password("enter your paassword : ") 
    password2 = validate_password("confirm your password : ") if not login else ''
    return password1, password2

def confirm_password(password1, password2):
    while password1 != password2 :
        print("password dnt match ! ")
        password1, password2 = get_user_passwords()
    print("password confirmed succesfully ! ")
    return password1, password2

def validate_phone_number(phone_number):
    return len(phone_number) == 11 and all(num.isdigit() for num in phone_number)

def get_user_phone_number(msg="enter your phone number : "):
    phone_number = input(msg)
    while  not validate_phone_number(phone_number):
        phone_number = get_user_phone_number("not a valid egyption phone number : ")
    return phone_number

def validate_user_registration_info():
    name = get_user_name()
    email = validate_email()
    password1, password2 = get_user_passwords()
    password1, password2 = confirm_password(password1, password2)
    phone_number = get_user_phone_number()

    user_info = {"id" : round(time.time()),
     "name": name , "email": email, "phone_number" : phone_number,
      "password" : password1}

    return user_info



def validate_user_login_info():
    email = validate_email()
    password, _ = get_user_passwords(login=True)
    user_info = {"email": email, "password" : password}
    return user_info 
