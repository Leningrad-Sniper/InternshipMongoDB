from fastapi import APIRouter

from models.blog_model import Blog
from config.database import collection_name

from schemas.blog_schema import blogs_serializer, blog_serializer
from bson import ObjectId

blog_api_router = APIRouter()

# retrieve
@blog_api_router.get("/")
async def get_blogs():
    blogs = blogs_serializer(collection_name.find())
    return blogs

@blog_api_router.get("/{id}")
async def get_blog(id: str):
    return blogs_serializer(collection_name.find({"_id": ObjectId(id)}))


# post
@blog_api_router.post("/")
async def create_blog(blog: Blog):
    _id = collection_name.insert_one(dict(blog))
    return blogs_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@blog_api_router.put("/{id}")
async def update_blog(id: str, blog: Blog):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(blog)
    })
    return blogs_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@blog_api_router.delete("/{id}")
async def delete_blog(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}

# comment
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


