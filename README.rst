=========
Inventory
=========

.. contents::

Requirements
------------
(This guide is for installing on a Linux/Ubuntu distro.)

- Python 3.7+
- mariadb
- libmariadbclient-dev
- python3-dev
- libpython3-dev
- libsasl2-dev
- libldap2-dev
- libssl-dev

You may also need python3-venv, depending on your Python installation.

See also requirements.txt


Setup
=====
venv
----
To set up the virtual environment and then activate it, run the following
commands:

::
    python3.x -m venv venv
    . venv/bin/activate

Your Python dependencies should be installed while venv is active.
You'll know venv is active because you'll see `(venv)` before your command
prompt.
To quit venv at any time you just need to use the following command:

::

    deactivate

mysql
-----

In mysql, create a new user and a new database, and give that user permissions
to use that database.
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

ldap
----
A la this_ stackoverflow page, you probably need to copy the cert file to
``/etc/ssl/certs/`` and add TLS_CACERT /etc/ssl/certs/[cert name] to
``/etc/ldap/ldap.conf``.The cert can be obtained here_.

.. _this: https://serverfault.com/questions/398684/ubuntu-12-04-ldap-ssl-self-signed-cert-not-accepted/419068#419068?newreg=d93209c894f64b158a82d13727f2a07d
.. _here: https://accounts.cs.sunyit.edu/ucs-root-ca.crt

Configuring Django
------------------
Then you need to make the following changes in `settings.py`:

- Change DATABASES to match the following pattern: (Obviously, these can be
    configured to whatever you need them to be.)

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
    python manage.py makemigrations
    python manage.py migrate

You can test your setup using the following:

::

    python manage.py sqlmigrate csnetinventory 0001


Then we need to create an admin account. Run the following commmand,
and it will prompt you for a username, email, and password for the
admin account.

::

    python manage.py createsuperuser


Running the server
------------------

::

    python manage.py runserver

Other helpful Django commands
-----------------------------
Access the project python shell:

::

    python manage.py shell

Change a user's password
Note! This only works for accounts using Django's implmentation, i.e., the
superuser. This server by default uses the CSNet LDAP for user authentication.
These users' passwords cannot be changed using this method.

::

    python manage.py changepassword

In Linux environments, ``./manage.py [command]`` works as shorthand
for ``python manage.py [command].``