from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mysecretkey'

    os.makedirs(app.instance_path, exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(app.instance_path, 'database.db')

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

