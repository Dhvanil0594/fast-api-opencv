from fastapi import APIRouter

from src.api.v1.views import (api_employee_auth_view, api_fruit_detection_view)

router = APIRouter(prefix="/api/v1")

router.include_router(api_employee_auth_view.router, tags=["Authentication Endpoints"])
router.include_router(api_fruit_detection_view.router, tags=["Detection Endpoints"])
