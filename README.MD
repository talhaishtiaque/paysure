# PaySure
PaySure API is a Python Django API for Policies upload and payments authorization.

## Installation

Use the python and pip to install and deploy.

```bash
git clone https://github.com/talhaishtiaq/
mkvirtualenv --python=/usr/bin/python3.6 paysure-venv
cd paysure
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API URLs

Policies and payments are available on following urls:

http://localhost:8000/policy/

http://localhost:8000/payment/

##Uploadding Policies

##Payment Authorization

## Developent

API is using defaut Django file structure and urls.

APIViews are implemented in paysure/views.py.

To modify any of the API functionality just add a function for it in the ApiView class.

## Database

Database is sqlite and defined in paysure/settings.py

Tables are there in paysure_api/models.py and can be changed and saved via migrations.
