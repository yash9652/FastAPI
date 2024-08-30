
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Request


app = FastAPI()

Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="TodoApp/templates")

app.mount("/static",StaticFiles(directory="TodoApp/static"),name="static")

@app.get("/")
def test(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
