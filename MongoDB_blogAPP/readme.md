MongoDB Blog Application
This repository contains code for a blog application that utilizes MongoDB as its database. The application allows users to create, read, update, and delete blog posts. Below, I’ll explain the key components of the project.

Database Connection
The database.py file establishes a connection to a MongoDB database named “todo_app” and selects a collection named “blogs_app”. Here’s how it works:
from pymongo import MongoClient

# Connect to MongoDB using the provided connection string
client = MongoClient("mongodb+srv://<username>:<password>@internproject.scn9oec.mongodb.net/?retryWrites=true&w=majority&appName=Internproject")

# Select the "blogs_app" collection within the "todo_app" database
db = client.todo_app
collection_name = db["blogs_app"]
This snippet enables subsequent operations on the “blogs_app” collection within the “todo_app” database.

Blog Model
The blog_model.py file defines a Pydantic model called Blog. This model represents the structure of a blog post. Here are the fields included in the Blog model:

id: Refers to the unique ID assigned to the blog by MongoDB.
username: Represents the author’s ID who wrote the blog.
title: Refers to the title of the blog.
body: Contains the content of the blog.
completed: Indicates whether the author has finished writing the blog.
date: The date when the blog was posted.
comments: A list containing dictionaries with information about comments posted by various users on a particular blog.
likes: A list of all users who have liked the blog.
dislikes: A list of all users who have disliked the blog.
Blog Serializer
The blog_schema.py file provides a function called blog_serializer(blog) that converts a blog document (retrieved from MongoDB) into a dictionary with the same fields as the Blog model. Here’s the implementation:

def blog_serializer(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "username": blog["username"],
        "title": blog["title"],
        "body": blog["body"],
        "completed": blog["completed"],
        "date": blog["date"],
        "comments": blog["comments"],
        "likes": blog["likes"],
        "dislikes": blog["dislikes"]
    }
This serializer function ensures consistent data representation when interacting with the database.