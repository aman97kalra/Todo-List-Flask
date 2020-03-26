# Todo-List

A simple todo-list web app created using flask which provides the following functionality:  

- Create a new list of todo items  
- Mark a todo item as complete or incomplete    
- Delete a todo item if it's no longer required

The project makes use of Python3, Flask, SQLite, SQLAlchemy, HTML and Css.

![Screenshot](static/img.png?raw=true "Optional Title")


### Note
- You can't deploy to heroku using SQLite database as Heroku's dynos don't have a filesystem that persists across deploys, a file-based database like SQLite3 isn't going to be suitable. It's a great DB for development/quick prototypes, though.Instead of using SQLite on Heroku you can configure your app to run on Postgres.

