# Django-CockroachDb
This is starter bundle for Django-CockroachDb project.

Download CockroachDb from offical CockrochDb website.
Install it on locally and follow instaructions from https://www.cockroachlabs.com/docs/stable/install-cockroachdb.html
This documentation will guide you to setup database server nodes as well as understand Cockroachdb architecture.

----------------------------------------------------------------------------------------------------------------------------
After successful installation move open command prompt and change directory to cockroach-django-master.
Run a command - 'pip install .'
This will install cockroach-django custom driver. (Prerequisite are python and pip)

-----------------------------------------------------------------------------------------------------------------------------

Open new command prompt and change directory to cockroachdb_demo.
run commands as follows:
    - python manage.py makemigrations (Check for newly create tables and check if there is any database schema update)
    - python manage.py migrate  (Migrate all the tables to database)
    - python manage.py createsuperuser (create user with admin priviledges)
    - python manage.py runserver (Runs a server on port 8000)
