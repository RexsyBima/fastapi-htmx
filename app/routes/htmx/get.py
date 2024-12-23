from . import router

from app import db, templates
from fastapi import Request


@router.get("/user/{username}")
async def get_user(request: Request, username: str):
    for user in db:
        if user.username == username:
            break
        return templates.TemplateResponse(request=request, name="htmx/user.html", context={"user": user})


@router.get("/user/")
async def get_all_users():
    return db
