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
**Hint:** all CAPITALIZED words should be replaced with your individual terms.

1. Create a folder for this site: `$ mkdir PROJECT_FOLDER`
2. Change to the folder: `$ cd PROJECT_FOLDER`.
3. Clone the GitHub-repository: `$ git clone https://github.com/stueken/superlists.git`
4. Change to the repository folder: `$ cd superlists' (**Hint:** All commands in the following are based on this folder)
5. Check if virtualenv is installed: `$ virtualenv --version`
6. If not, install it: `$ sudo pip3 install virtualenv`
7. Create a virtual environment: `$ virtualenv --python=python3 ../NAME_OF_VIRTUALENV`
8. Activate the virtual environment: `$ source ../virtualenv/bin/activate`
9. Install required packages: `$ pip install -r requirements.txt`


## Deployment (VPS)
- tbd

## Known issues
- After sharing a list, the sharee email address doesn't pop up under the "Shared with" section right away.
- Still some bugs as a result of race conditions in the functional tests when using a Jeninks CI server. 
