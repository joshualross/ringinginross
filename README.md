Ringing in Ross is my wedding website.  I wanted to explore some different python tools 
that are available for setting up and working in web applications.  Those include

 - bottle
 - marshmallow
 - oursql


Below there are some brief notes about setting up the application on my webhost.

Create virtual env for application
==================================
create a new virtualenv for the app specifying python 2.7 and using system site packages

    virtualenv --system-site-packages --prompt="(application)" -p /usr/bin/python2.7 env

Install the requirements for application
========================================
To install the application packages use the `-I` switch to pull in system wide installed packages.

    pip install -Ir requirements.txt 

Configure web server
====================
Modify the .htaccess file:

    AddHandler fcgid-script .fcgi
    Options -Indexes
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ application.fcgi/$1 [QSA,L]

Create an application.fcgi that serves the app in the virtual env

    #!/path/to/the/virtual/env/bin/python

    import os, sys

    import bottle
    from flup.server.fcgi import WSGIServer

    os.environ['PATH'] = '/path/to/the/virtual/env/bin:' + os.environ['PATH']
    os.environ['VIRTUAL_ENV'] = '/path/to/the/virtual/env/bin'
    os.environ['PYTHON_EGG_CACHE'] = '/path/to/the/virtual/env/bin'
    os.chdir('/path/to/the/virtual/')

    # Add a custom Python path.
    sys.path.insert(0, "/path/to/the/virtual/env/bin")

    # Now import the application code
    import application.index

    WSGIServer(bottle.default_app()).run()

Create softlinks to the assets
==============================
Create some symlinks from the webserver root

    ln -s /path/to/the/application/views/assets
    ln -s /path/to/the/application/views/images

Deploy the application
======================
The python egg needs rebuilt in order to deploy changes to the application

    cd /path/to/the/application
    source env/bin/activate
    python setup.py install

