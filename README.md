# Personalized Workout API System

## Description
An API made with Django REST Framework which allows users to create personalized workout plans,
add new excercises to them via a predefined workout table which stores 20 initial excercises,
and to modify them. The user can also track the weight and goals.

## Tech Stack
- __Python__
- __Django__
- __Django REST Framework__
- __SQLite__

## Instructions for use

1. ### Cloning and setting up

To get started, first clone the repository: 
~~~bash 
git clone git@github.com:TheActualSanny/Sweeft_WorkoutSystem.git
~~~
enter it's directory and create a __virtual environment__:
~~~shell
python -m venv venv
~~~
and activate it: 
~~~shell
. venv/bin/activate
~~~

2. ### Installing the essential modules
All of the necessary libraries that are utilized in the project are written in the __requirements text file__.
Install these modules by running:
~~~shell
pip install -r requirements.txt
~~~

3. ### Running the initial migrations
The migrations which are essential to set up the necessary models in the project are all commited to the repository.
In order for the API to function correctly, run the migrations:
~~~shell
python manage.py migrate
~~~
This will not only set up the models, but it will also __populate the DefinedWorkouts table with the initial 20 excercises__.

4. ### The API setup
After running the commands, the API should be ready to go.
To test the endpoints, run the server:
~~~shell
python manage.py runserver
~~~
And head over to the page:
~~~
http://127.0.0.1:8000/api/v1/
~~~

The descriptions for the endpoints of the API are all written on the swagger page, though,
the authroization guide and short descriptions will also be written here.

## Authorization
First, create a user or login in an already existing one. Both of the endpoints will return an __access token__ in the response,
as the API utilzes JWT-s for safety. 

Copy the access token and press the __Authroize__ button on the swagger view

In the __value__ field, type the following:
~~~
Bearer {Your Access Token}
~~~

And press authorize. You are now authorized to use any of the other endpoints.

### NOTE:
Only endpoints which do not require the access token header are register and login.
