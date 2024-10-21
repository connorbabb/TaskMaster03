# Overview

Program that integrates with a firebase database. host.py which initializes the database to work through the html using flask, it also creates all the methods and routes that are used by the database to display/create/edit/delete goals.

I wanted to provide people a way to record and edit tasks and mark them in an easy and intuitive way. There should be lots of differnet ways to use it as well. I want to learn how to work with the cloud and how to link it to a database.

HOW TO USE: Go to the host.py program, change directories if needed to it if needed. Run the program either using the run button or by typing 'python host.py' that will run the program and produce a url (ex. http://127.0.0.1:5000)
Copying or following this url will take you to an html website with a list of tasks in a database. You can either choose to delete a task/edit the name or date/or create a new one. Any changes or additions will automatically uplode to the cloud database.

[Software Demo Video](https://youtu.be/Q3hW1x9J4uw)

# Cloud Database

I used Firestore to create the firebase project, the flask app in the python program calls the firebase and makes changes to it live.

The collections and documents I used were a collection of 'users', I used a document for one of the users as just my name, connor_babb. Each user has a 'task' collection and a couple of default tasks in the database.

# Development Environment

I followed a lot of the links given on the cloud database modules for research. I also watched a couple youtube videos on getting started with the cloud database and troubleshooting. AI was also used for troubleshooting and some development.

I followed the recommendations from the module page and used Python and Firestore/Firebase to create them. I used html for the website layout, and used Flask to integrate with the database and Python.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Youtube tutorial](https://www.youtube.com/watch?v=M1JjK9DXC6U)
- [mongodb](https://www.mongodb.com/resources/basics/databases/cloud-databases)

# Future Work

- Datetime features
- Priority manager
- Notifications