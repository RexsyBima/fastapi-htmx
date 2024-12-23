from app.form import UserRegister
from app import templates, db, start
from . import router
from typing import Annotated
from fastapi import Form, Request


@router.post("/add-user")
async def add_user(request: Request, userform: Annotated[UserRegister, Form()]):
    if userform.username not in db:
        db.append(userform)
        success = True
        return templates.TemplateResponse(request=request, name="htmx/contact.html", context={"contact": userform.username, "success": success})
    else:
        success = False
        return templates.TemplateResponse(request=request, name="htmx/fail.html", context={"success": success})
