=========
Inventory
=========

.. contents::

Requirements
------------
- Python 3.7+
- Django 2.2+ [1]_
- database software (We use mariadb/mysql, but Django is configurable with pretty much any database software.)
- mysqlclient [1]_
- djangorestframework [1]_
- django-url-filter [1]_
- virtualenv
- targets linux clients

.. [1] install inside venv environment

Setup
=====

venv
----

To set up the virtual environment and then activate it, run the following commands:

::

    virtualenv venv
    . venv/bin/activate

Your Python dependencies should be installed while venv is active.
You'll know venv is active because you'll see `(venv)` before your command prompt.
To quit venv at any time you just need to use the following command:

::

    deactivate

mysql
-----

In mysql, create a new user and a new database, and give that user permissions to use that database.
To open mysql as admin:

::

    sudo mysql -uroot

Then in mysql

::

    CREATE DATABASE inventorydb;
    CREATE USER 'yourusername'@'localhost' IDENTIFIED BY 'yourpassword';
    GRANT ALL PRIVILEGES ON inventorydb.* TO 'yourusername'@'localhost';
    FLUSH PRIVILEGES;

That should be adequate for setting up the database.


Configuring Django
------------------
Then you need to make the following changes in `settings.py`:

- Change DATABASES to match the following pattern: (Obviously, these can be configured to whatever you need them to be.)

::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'inventorydb',
            'USER': 'yourusername',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

- Make sure `TIME_ZONE` is set to the proper time zone.

Then, we need to run the following commands from the
terminal (Make sure you've set up and are using venv first):

::

    python manage.py migrate
    python manage.py makemigrations csnetinventory
    python manage.py migrate

You can test your setup using the following:

::

    python manage.py sqlmigrate csnetinventory 0001


Then we need to create an admin account. Run the following commmand,
and it will prompt you for a username, email, and password for the admin account.

::

    python manage.py createsuperuser

You may also find it helpful to access the project python shell:

::

    python manage.py shell

Running the server
------------------

::

    python manage.py runserver

