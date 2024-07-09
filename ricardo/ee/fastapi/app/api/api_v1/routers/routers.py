"""API routing module."""

from fastapi import APIRouter

from ..endpoints.parks import parks_router
from ..endpoints.species import species_router
from ..endpoints.visitor import visitors_router

api_router = APIRouter()

api_router.include_router(parks_router, prefix="/parks")
api_router.include_router(species_router, prefix="/species")
api_router.include_router(visitors_router, prefix="/visitors")
