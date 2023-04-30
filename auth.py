from flask_login import LoginManager
from models.user import User
from flask import redirect,url_for
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('user.main'))