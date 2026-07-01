# Meals & Miles

Meals & Miles is a Flask-based web application that allows users to share their travel experiences and favourite meals. Users can create an account, manage a personal profile, and publish posts with images describing their travel destinations and food experiences.

## Features

* User registration and login
* User authentication using Flask-Login
* Edit and update user profile
* Create, edit and delete travel and food posts
* Upload images with posts
* View all posts
* Responsive design for desktop and mobile devices
* SQLite database using SQLAlchemy ORM

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-Migrate
* HTML5
* CSS3
* JavaScript
* SQLite
* Gunicorn (deployment)

## Project Structure

Database-Assignment/ 
│ 
├── app.py 
├── requirements.txt 
├── README.md 
├── database/ 
│ ├── __init__.py 
│ ├── models.py 
│ ├── views.py 
│ ├── static/ 
│ |── templates/ 
├── migrations/ 
└── instance/

## Installation

1. Clone the repository.

```bash
git clone https://github.com/jmichael2025/Database-Assignment.git
```

2. Navigate to the project folder.

```bash
cd Database-Assignment
```

3. Create a virtual environment.

```bash
python -m venv venv
```

4. Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

5. Install the required packages.

```bash
pip install -r requirements.txt
```

6. Run the application.

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5001
```

## Deployment

This project is configured for deployment using **Render** with **Gunicorn**.

### Build Command

```text
pip install -r requirements.txt
```

### Start Command

```text
gunicorn app:app
```

## Author
Jasmin Michael
Developed as part of a Database/Web Development assignment.

## License

This project was created for educational purposes.
