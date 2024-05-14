from pymongo import MongoClient



client = MongoClient("mongodb+srv://Leningrad_Sniper:Denmark1945@internproject.scn9oec.mongodb.net/?retryWrites=true&w=majority&appName=Internproject")


db = client.todo_app

collection_name = db["blogs_app"]