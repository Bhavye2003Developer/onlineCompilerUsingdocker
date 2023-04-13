# onlineCompilerUsingdocker

Make sure you have installed docker on ubuntu or docker desktop on linux.

Installation

- git clone this repo.
- running commands as root

- cd ide
- python3 manage.py runserver
- go to you browser and type http://0.0.0.0:8000/ It will open the IDE.

This ide is created using django as backened and docker to run containers, Wenever a user types in code and selects a langauge like python or c++, dockerfile
will create an image and run in background, and run the code the user types and pushes it to frontend to be shown as output.
