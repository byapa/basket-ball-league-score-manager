# Basket Ball League Score manager

This is a sample application written in Django (v4.2.3) and Python (v3.10.12) to address the requirements
mentioned [here](https://docs.google.com/document/d/1SocsseqSSvIbxkrs4gBC_Iqrhihn8RRb28gq8iwVq_w/edit?usp=sharing).

## Steps to Run

### 1. Install Pre-requisites
1. Install Python 3.10
2. Clone the project, navigate to the root directory and run following command to install the virtual environment
```commandline
python3.10 -m venv env
```
3. Activate the virtual environment. Following command can be used on Linux
```commandline
source env/bin/activate
```
4. Install dependencies using following command
```commandline
pip install -r requirements.txt
```

### 2. Create the database
Run following command from the root directory.
```commandline
python manage.py migrate
```

### 3. Load seed data
Run following command from the root directory.
```commandline
python manage.py loaddata backend/fixtures/*
```

### 4. Run the application
Run following command from the root directory.
```commandline
python manage.py runserver
```