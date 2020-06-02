from sqlalchemy import or_


'''
METHODS
--------------
'''
import arrow

#MODELS
from bpaint.model import *
from bpaint import login_user

#EXAMPLE METHOD
def try_login(username_or_email, password):
    user = User.query.filter(or_(
        User.username == username_or_email,
        User.email == username_or_email
    )).one()
    if user and user.is_verified(password):
        return True
    return False

def returnTrue():
    return True
        