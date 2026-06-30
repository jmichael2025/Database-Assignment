import os

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user,login_required, logout_user, current_user
from .models import User, Post, Like, Comment
from . import db
import os
from werkzeug.utils import secure_filename
import os
from .models import Post

import Database

views = Blueprint('views', __name__)

@views.route('/')
def home():

    posts = Post.query.order_by(Post.id.desc()).all()

    return render_template('login.html', posts=posts)
    

@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return "Username or email already exists. Please choose a different one."

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('views.home'))
    return render_template('register.html')

@views.route('/users')
def users():

    users = User.query.all()

    output=""
    for user in users:
        output += f"Username: {user.username}, Email: {user.email}<br>"

    return output

@views.route('/process_login', methods=['POST'])
def process_login():

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    print(f"User found: {user}")

    if not user:
        posts = Post.query.order_by(Post.id.desc()).all()
        return render_template(
            "login.html",
            posts=posts,
            error="This account does not Exist.")

    
    if user.password != password:
        posts = Post.query.order_by(Post.id.desc()).all()
        return render_template(
            "login.html",
            posts=posts,
            error="Incorrect password")
        

    login_user(user)

    return redirect(url_for('views.account'))
    


@views.route('/account') 
@login_required
def account():

    community_posts = Post.query.filter(
        Post.user_id != current_user.id
    ).order_by(
        Post.id.desc()
    ).limit(5).all()

    return render_template(
        'account.html',
        user=current_user,
        community_posts=community_posts
    ) 
    


@views.route('/edit')
@login_required
def edit():
    if request.method == 'POST':
        current_user.name = request.form.get('name')
        current_user.age = request.form.get('age')
        current_user.gender = request.form.get('gender')
        current_user.place = request.form.get('place')
        current_user.interests = request.form.get('interests')
        current_user.cuisine = request.form.get('cuisine')
        current_user.about_me = request.form.get('about_me')
        db.session.commit()
        return redirect(url_for('views.account'))
    return render_template('edit.html',user=current_user)


@views.route('/save_profile', methods=['POST'])
@login_required
def save_profile():
    if request.method == 'POST':
        current_user.name = request.form.get('name')
        current_user.age = request.form.get('age')
        current_user.gender = request.form.get('gender')
        current_user.place = request.form.get('place')
        current_user.interests = request.form.get('interests')
        current_user.cuisine = request.form.get('cuisine')
        current_user.about_me = request.form.get('about_me')
        current_user.profile_description = request.form.get('profile_description')
        current_user.specify = request.form.get('specify')

        #debug prints
        print(f"Name: {current_user.name}")
        print(f"Age: {current_user.age}")
        print(f"Gender: {current_user.gender}")
        print(f"Place: {current_user.place}")
        print(f"Interests: {current_user.interests}")
        print(f"Specify: {current_user.specify}")
        print(f"Cuisine: {current_user.cuisine}")
        print(f"About Me: {current_user.about_me}")
        print(f"Profile Description: {current_user.profile_description}")

        db.session.commit()

        return redirect(url_for('views.account'))
    
    @views.route('/cancel_edit')
    @login_required
    def cancel_edit():
     return redirect(url_for('views.account'))


@views.route('/upload_profile_picture', methods=['POST'])
@login_required
def upload_profile_picture():

    if 'profile_pic' not in request.files:
        return redirect(url_for('views.account'))

    file = request.files['profile_pic']

    if file.filename == '':
        return redirect(url_for('views.account'))

    filename = secure_filename(file.filename)

    upload_path = os.path.join(
        'Database',
        'static',
        'uploads',
        filename
    )

    file.save(upload_path)

    current_user.profile_pic = f'uploads/{filename}'
    db.session.commit()

    return redirect(url_for('views.account'))

@views.route('/create', methods=['GET', 'POST'])
@login_required
def create():

    if request.method == 'POST':

        title = request.form.get('title')
        content = request.form.get('content')

        print(f"Title: {title}")
        print(f"Content: {content}")

        return redirect(url_for('views.account'))
    return render_template('create.html')


@views.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():

    if request.method == 'POST':

        title = request.form.get('title')
        content = request.form.get('content')
        file = request.files.get('image')

        image_path = None

        if file and file.filename != '':
            filename = secure_filename(file.filename)

            upload_path = os.path.join(
                'Database',
                'static',
                'uploads',
                filename
            )

            file.save(upload_path)

            image_path = f'uploads/{filename}'

        post = Post(
            title=title,
            content=content,
            image=image_path,
            user_id=current_user.id
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('views.account'))

    return render_template('create.html')



@views.route('/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)

    if post.user_id == current_user.id:
        db.session.delete(post)
        db.session.commit()

    return redirect(url_for('views.account'))

@views.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):

    print ("Edit post route reached")

    post = Post.query.get_or_404(post_id)
    print("Post ID:", post.id)
    print("Post owner:", post.user_id)
    print("Current user:", current_user.id)

    if post.user_id != current_user.id:
        return redirect(url_for('views.account'))

    if request.method == 'POST':

        post.title = request.form.get('title')
        post.content = request.form.get('content')

        file = request.files.get('image')

        if file and file.filename != '':

            filename = secure_filename(file.filename)

            upload_path = os.path.join('Database','static','uploads',filename)

            file.save(upload_path)

            post.image = f'uploads/{filename}'

        db.session.commit()

        return redirect(url_for('views.account'))

    return render_template('edit_post.html',post=post)


@views.route('/like_post/<int:post_id>')
@login_required
def like_post(post_id):

    existing_like = Like.query.filter_by(
        user_id=current_user.id,
        post_id=post_id
    ).first()

    if not existing_like:

        like = Like(
            user_id=current_user.id,
            post_id=post_id
        )

        db.session.add(like)
        db.session.commit()

    return redirect(request.referrer)



@views.route('/profile/<int:user_id>')
def profile(user_id):

    user = User.query.get_or_404(user_id)

    return render_template(
        'profile.html',
        user=user
    )

@views.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):

    text = request.form.get('comment')

    if text:

        comment = Comment(
            text=text,
            user_id=current_user.id,
            post_id=post_id
        )

        db.session.add(comment)
        db.session.commit()

    return redirect(request.referrer)

@views.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for('views.home'))


@views.route('/delete_account')
@login_required
def delete_account():

    user_id = current_user.id 
    user = User .query.get(user_id)


    logout_user()

    db.session.delete(user)
    db.session.commit()

    return redirect('/')