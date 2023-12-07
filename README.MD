
# CONFIG
Edit settings.py with Email configuration and database info


Python 3.10.13
Pip 23.3.1
Postgres 14

pip install requirements.txt

python manage.py migrate

python manage.py createsuperuser 

Follow the prompts.

Run server

python manage.py runserver

Go to http://localhost:8000/admin

Add some users to the user model, make sure to include email address

Then navigate to

http://localhost:8000/api-auth/login

Login as one of the users. You will be redirected to /companies.

Here you see your list of companies with filtering & ordering and you can POST a new company i.e add it to the user.

Add few companies, you will see them in the list at /companies

Open any company at /companies/<id> to see Company detail view with all data about the company.

Send PATCH/PUT request, only number_of_employees will be updated

Run tests with python manage.py test

#TODOS
1. Unit tests for the API -- some done already
2. Put config variables from settings in enviroment .env
3. Package the app with Docker
