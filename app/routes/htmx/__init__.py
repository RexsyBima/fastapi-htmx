from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["apis"],
)

from . import delete, get, post, patch, put  # noqa
