from app import app, templates
from fastapi import Request
from .routes import pages
from .routes import htmx

app.include_router(pages.router)
app.include_router(htmx.router)


# @app.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(request=request, name="base/index.html")
