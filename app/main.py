import math
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from .repository import CommentsRepository
from datetime import date

app = FastAPI()

repository = CommentsRepository()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.get("/comments")
def get_comments(request: Request, q: str = "", page: int = 1, limit: int = 5):
    comments = repository.get_all()
    if q != "":
        comments = repository.search(q)

    start = (page - 1) * limit
    end = start + limit
    pages_count = [i for i in range(1, math.ceil(len(comments) / limit) + 1)]
    return templates.TemplateResponse(
        "VoxPop/index.html",
        {
            "request": request,
            "comments": comments[start:end],
            "pages": pages_count,
            "limit": limit,
            "q": q,
        }
    )

@app.get('/comments/new')
def get_post(request: Request):
    return templates.TemplateResponse(
        "VoxPop/add_comments.html",
        {
            "request": request
        }
    )
@app.post('/comments/new')
def add_comment(request: Request, categories: str = Form(), comment: str = Form()):
    today = date.today()
    comment = {"text": comment, "categories": categories, "date": today}
    repository.save(comment)
    return RedirectResponse('/comments', status_code=303)

