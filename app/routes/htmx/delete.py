from . import router

from app import db, templates
from fastapi import Request


@router.delete("/delete/{contact}")
async def delete_user(request: Request, contact: str):
    for i, user in enumerate(db, start=0):
        if user.username == contact:
            db.pop(i)
    return None
