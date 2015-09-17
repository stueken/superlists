# Superlists
A to-do list app created on basis of the book [Test-Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754) by Harry J.W. Percival.

You are welcome to try it out at http://superlists.nrbrt.com/

![My Lists](http://img5.fotos-hochladen.net/uploads/superlistsmylijiv1of5u4l.jpg)

## Features
- Create, share and collaborate on lists with others 
- User authentication through [Mozilla Persona](https://www.mozilla.org/en-US/persona/)

## Planned
- Delete as well as change items and lists
- Fully responsive design

## Local setup instructions
This app is written and tested in Python 3, running it with Python 2 could lead to unforseen problems. All CAPITALIZED terms in the following instructions should be replaced with your individual terms.

1. Create a folder for this site: `$ mkdir PROJECT_FOLDER` and change to it: `$ cd PROJECT_FOLDER`.
2. Clone the GitHub-repository: `$ git clone https://github.com/stueken/superlists.git` and change to the repository folder: `$ cd superlists` (**Hint:** All commands in the following are based on this folder)
3. Install the latest version of Selenium, a browser automation tool, which is used for the functional tests: `$ sudo pip3 install --upgrade selenium`
4. Check if virtualenv is installed: `$ virtualenv --version`. If not, install it: `$ sudo pip3 install virtualenv`
5. Create a virtual environment: `$ virtualenv --python=python3 ../NAME_OF_VIRTUALENV` and activate it: `$ source ../virtualenv/bin/activate`
6. Install required packages: `$ pip install -r requirements.txt`


## Deployment (VPS)
- tbd

## Known issues
- After sharing a list, the sharee email address doesn't pop up under the "Shared with" section right away.
- Still some bugs as a result of race conditions in the functional tests when using a Jeninks CI server. 
