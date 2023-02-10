from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# inititialize SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():

    app = Flask(__name__)
    app.secret_key = 'wadnjkwadn jwdjanwd'

    # Ensure templates are auto-reloaded
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def get(id):
        return User.query.get(id)


    # blueprint for the auth routes
    from .auth import auth
    from .views import views
    from .models import User, Note

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()
    app.static_folder = 'static'

    return app

def create_database(app):       
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('DATABASE CREATED!!!!!!!!!!')
