from pymongo import MongoClient



client = MongoClient("mongodb+srv://<username>:<password>@internproject.scn9oec.mongodb.net/?retryWrites=true&w=majority&appName=Internproject")


db = client.todo_app

collection_name = db["blogs_app"]
