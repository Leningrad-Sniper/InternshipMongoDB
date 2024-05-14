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

