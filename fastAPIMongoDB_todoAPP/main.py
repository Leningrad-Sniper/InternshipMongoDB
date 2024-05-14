from fastapi import FastAPI
from routes.blog_route import blog_api_router

app = FastAPI()

app.include_router(blog_api_router)

