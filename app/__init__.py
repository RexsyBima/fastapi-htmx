from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.form import UserRegister

db: list[UserRegister] = [UserRegister(username="Joko", hobby="memancing")]
start = 0

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
from . import routing  # noqa
