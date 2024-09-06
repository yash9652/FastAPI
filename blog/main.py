from fastapi import FastAPI, Request, status
from .models import Base
from .database import engine
from .routers import login
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

#app.mount("/static", StaticFiles(directory="myapp/static"), name="static")




@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(login.router)