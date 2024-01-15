# DJANGO ONLINE VOTING APP

## How to start the project

### For linux and Mac
```bash
cd OnlineVoting-Django # to navigate to the project directory if not in the same directory

python3 -m venv venv # for creating an virtualenv

. venv/bin/activate # for bash shell

. venv/bin/activate.fish # for fish shell

pip install -r requirements.txt # to install the all python packages for the project

python3 manage.py makemigrations # to create db if not created already

python manage.py migrate # to migrate meaning to implement changes

python manage.py createsuperuser # to begin superuseraccount, enter your email, password and username.

python manage.py runserver # to development server
```

### For Windows
```powershell
cd "OnlineVoting-Django" # # to navigate to the project directory if not in the same director

python -m venv env # to create virtualenv

env\Scripts\activate.bat # to activate virtualenv

pip install -r requirements.txt # to install the python packages

python manage.py makemigrations # to create db if not created already

python manage.py migrate # to migrate meaning to implement changes

python manage.py createsuperuser # to begin superuseraccount, enter your email, password and username.

python manage.py runserver # to run server on localhost
```
1. Open this link http://localhost:8000/ on your browser