#from ..helpers.validation_helpers import *
from helpers.db_handler import *

from helpers.file_handler import *

import helpers.validation_helpers as helpers; 


def Register():
    user_info= helpers.validate_user_info()
    insert_user(user_info)


Register()

