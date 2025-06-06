from fastapi import APIRouter 
from src.services.image_service import get_images, get_image


router = APIRouter(prefix="/images", tags=["Images"])


@router.get("")
def get_images_endpoint():
    return get_images()

@router.get("/{image_id}")
def get_image_endpoint(image_id: str):
    return get_image(image_id)