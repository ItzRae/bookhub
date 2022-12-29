from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
import time
from website import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

# from .models import User, Note

# auth = Blueprint('app', __name__)

#configure application
# app = Flask(__name__)
# app.secret_key = os.urandom(24)

# db = SQLAlchemy()
# DB_NAME = 'database.db'

# # Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# app.config["SQLAlCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
# db.init_app(app)

#Create Blueprint