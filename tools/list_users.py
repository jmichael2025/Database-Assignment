from Database import create_app
from Database.models import User

app = create_app()

with app.app_context():
    users = User.query.all()

    for u in users:
        print("ID:", u.id)
        print("Username:", u.username)
        print("----")