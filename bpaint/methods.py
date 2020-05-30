
'''
METHODS
--------------
'''
import arrow

#MODELS
from bpaint.model import *
from bpaint import login_user

#EXAMPLE METHOD
def do_login(phone, password):
    user = User.query.filter_by(phone=phone).first()
    if user and user.is_verified(password):
        return True
    return False

def returnTrue():
    return True
        