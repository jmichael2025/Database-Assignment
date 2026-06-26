from Database import create_app, db
from Database.models import User

app = create_app()

with app.app_context():
    users = User.query.all()
    print(users)