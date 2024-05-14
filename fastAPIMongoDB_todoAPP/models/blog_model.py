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

