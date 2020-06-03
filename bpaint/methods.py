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
    users = User.query.all()
    user = next(filter(lambda u: u.username == username_or_email or u.email == username_or_email, users))
    if user and user.is_verified(password):
        return login_user(user)
    return False

def returnTrue():
    return True
        