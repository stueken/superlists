# Superlists
A to-do list app created on basis of the book [Test-Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754) by Harry J.W. Percival.

You are welcome to try it out at http://superlists.nrbrt.com/

![My Lists](http://img5.fotos-hochladen.net/uploads/superlistsmylijiv1of5u4l.jpg)

## Features
- Create, share and collaborate on lists with others 
- User authentication through [Mozilla Persona](https://www.mozilla.org/en-US/persona/)
- Automated testing with unittest, selenium (functional tests) and qunit (JavaScript)
- Automated deployment with fabric

## Planned
- Delete as well as change items and lists
- Fully responsive design

## Local setup instructions
This app is written and tested in Python 3, running it with Python 2 could lead to unforseen problems. All CAPITALIZED terms in the following instructions should be replaced with your individual terms.

1. Create a folder for this site: `$ mkdir PROJECT_FOLDER` and change to it: `$ cd PROJECT_FOLDER`.
2. Clone the GitHub-repository: `$ git clone https://github.com/stueken/superlists.git` and change to the repository folder: `$ cd superlists` (**Note:** All commands in the following are based on this folder)
3. Install the latest version of Selenium, a browser automation tool, which is used for the functional tests: `$ sudo pip3 install --upgrade selenium`
4. Check if virtualenv is installed: `$ virtualenv --version`. If not, install it: `$ sudo pip3 install virtualenv`
5. Create a virtual environment: `$ virtualenv --python=python3 ../NAME_OF_VIRTUALENV` and activate it: `$ source ../virtualenv/bin/activate`
6. Install required packages: `$ pip install -r requirements.txt`
7. Create database directory: `$ mkdir ../database` and create the database: `python3 manage.py migrate`
8. If wanted, run all tests (functional and unit) automatically with `python3 manage.py test` or run the test server manually with `$ python3 manage.py runserver localhost:8000`


## Automated Deployment with Fabric (VPS)
In order to get this to work, you should have a domain and an own (virtual) server (Ubuntu 14.04) running. You should have root access and be able to SSH into it. 

How to set up your domain and server in detail, please follow from here: gh from here: http://chimera.labs.oreilly.com/books/1234000000754/ch08.html#_getting_a_domain_name.

1. Setup your server according to the notes in deploy_tools/provisioning_notes.md
2. If you haven't already, install fabric with: `$ pip2 install fabric`
3. Change to the deploy directory: `$ cd deploy_tools` and deploy your app with `$ fab deploy:host=USERNAME@YOUR-DOMAIN`
4. SSH into your server: `$ ssh YOUR-IP-ADDRESS`
5. Restart the Gunicorn webserver: `USER@SERVER:# sudo restart gunicorn-YOUR-DOMAIN`
6. From your local terminal, run the tests on the server: `$ python3 manage.py test functional_tests --liveserver=YOUR-DOMAIN` 

## Known issues
- After sharing a list, the sharee email address doesn't pop up under the "Shared with" section right away.
- Still some bugs as a result of race conditions in the functional tests when using a Jeninks CI server. 
