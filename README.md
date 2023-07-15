# Basket Ball League Score manager

This is a sample applicaiton written in Django (v4.2.3) and Python (v3.10.12) to address the requirements mentioned [requirements.txt](requirements.txt).

## Steps to Run
### 1. Install Pre-requisites
1. Python 3.10

### 2. Create the database
Run following command from the root directory.
    python manage.py migrate

### 3. Load seed data
Run following command from the root directory.
    python manage.py loaddata backend/fixtures/*

### 4. Run the application
Run following command from the root directory.
    python manage.py runserver