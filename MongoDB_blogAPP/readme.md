#database.py

from pymongo import MongoClient



client = MongoClient("mongodb+srv://Leningrad_Sniper:Denmark1945@internproject.scn9oec.mongodb.net/?retryWrites=true&w=majority&appName=Internproject")


db = client.todo_app

collection_name = db["blogs_app"]

establishes a connection to a MongoDB database named "todo_app" and selects a collection named "blogs_app". The MongoClient connects to the MongoDB server using a provided connection string containing credentials and server information. This snippet enables subsequent operations on the "blogs_app" collection within the "todo_app" database.

#models 
#
will contain the description of the blog class 

## blog_model.py

   from pydantic import BaseModel

   class Blog(BaseModel):
        id:str
        username: str
        title: str
        body: str
        completed: bool
        date: str
        comments:list 
        likes:list 
        dislikes:list  

   id: refers to the id that will be assigned to the blog by MongoDB 
   username: is the id of the author writing the blog 
   title: refers to the title of the blog 
   body: refers to the content of the blog 
   completed: checks if author has finished writing the blog or not 
   date:the date the blog has been posted 
   comments:a list which contains all comments posted by various users on a particular blog(they contain information about the comments in the form of dictionaries,so comments is a list of dictionaries)
   likes: A list of all the users who have liked the blog 
   dislikes:A list of all users who have disliked the blog 

# schemas 
## blog_schema.py 

    def blog_serializer(blog) -> dict:
    return {
        
        "id": str(blog["_id"]),
        "username": blog["username"], 
        "title": blog["title"],
        "body": blog["body"],
        "completed": blog["completed"],
        "date": blog["date"],
        "comments": blog["comments"],
        "likes":blog["likes"], 
        "dislikes":blog["dislikes"]
    }

    def blogs_serializer(blogs) -> list:
        return [blog_serializer(blog) for blog in blogs]

    The function blog_serializer takes a class Blog as a parameter and return a dictionary with all the parameters assigned its respective values 

    The function blogs_serializer takes a list of blogs and calls the function blog_serializer on each blog 

# routes 
## blog_route.py 

   from fastapi import APIRouter

   from models.blog_model import Blog
   from config.database import collection_name

   from schemas.blog_schema import blogs_serializer, blog_serializer
   from bson import ObjectId

   blog_api_router = APIRouter()

     
   @blog_api_router.get("/")
   async def get_blogs():
        blogs = blogs_serializer(collection_name.find())
        return blogs

   @blog_api_router.get("/{id}")
   async def get_blog(id: str):
        return blogs_serializer(collection_name.find({"_id": ObjectId(id)}))



   @blog_api_router.post("/")
   async def create_blog(blog: Blog):
        _id = collection_name.insert_one(dict(blog))
        return blogs_serializer(collection_name.find({"_id": _id.inserted_id}))



   @blog_api_router.put("/{id}")
   async def update_blog(id: str, blog: Blog):
        collection_name.find_one_and_update({"_id": ObjectId(id)}, {
            "$set": dict(blog)
        })
        return blogs_serializer(collection_name.find({"_id": ObjectId(id)}))


   @blog_api_router.delete("/{id}")
   async def delete_blog(id: str):
       collection_name.find_one_and_delete({"_id": ObjectId(id)})
       return {"status": "ok"}


   @blog_api_router.put("/{id}/username/comment/date/like")
   async def add_comment_to_blog(id: str, username: str,comment: str, date: str,like:bool):
       comments = {
           "username": username,
           "body": comment,
           "date": date,
        
       }
       if(like==True):
    
           collection_name.find_one_and_update({"_id": ObjectId(id)}, {
           "$push": {"likes": username}
       })

    

         else:
             collection_name.find_one_and_update({"_id": ObjectId(id)}, {
             "$push": {"dislikes": username}
        })
    
        collection_name.find_one_and_update({"_id": ObjectId(id)}, {
            "$push": {"comments": comments}
        })
        return blogs_serializer(collection_name.find({"_id": ObjectId(id)}))

    
    The get_blogs function retrieves all blog posts from the database using blogs_serializer.
    It returns a list of serialized blog objects.
    Retrieve a Single Blog:
    The get_blog function retrieves a specific blog post by its ID.
    It uses the blogs_serializer to serialize the result.
    The ID is passed as a parameter in the URL.
    Create a New Blog:
    The create_blog function creates a new blog post.
    It inserts the blog data into the database and returns the serialized blog object.
    Update an Existing Blog:
    The update_blog function updates an existing blog post.
    It finds the blog by its ID and updates its content.
    The updated blog is returned as a serialized object.
    Delete a Blog:
    The delete_blog function deletes a blog post by its ID.
    It removes the blog from the database and returns a status message.
    Add a Comment to a Blog:
    The add_comment_to_blog function adds a comment to a specific blog post.
    It takes parameters like username, comment, date, and like.
    If like is True, it adds the username to the “likes” list; otherwise, it adds it to the “dislikes” list.
    The comment details are pushed to the “comments” list in the blog document.
    Remember to create a .md file describing the API documentation for these endpoints. You can use tools like Swagger UI or ReDoc to automatically generate API documentation based on your FastAPI routes.
















