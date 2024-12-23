from . import router
from fastapi import Request, Form
from app import templates, db


@router.get("/")
async def homepage(request: Request,):
    return templates.TemplateResponse(request=request, name="pages/homepage.html", context={"contacts": db})


@router.get("/settings")
async def settings(request: Request):
    return templates.TemplateResponse(request=request, name="pages/settings.html")
