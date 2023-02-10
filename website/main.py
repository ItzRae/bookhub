from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
import time
from website import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

