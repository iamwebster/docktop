from fastapi import APIRouter 
from src.services.volume_service import get_volume, get_volumes


router = APIRouter(prefix="/valumes", tags=["Volumes"])


@router.get("")
def get_volumes_endpoint():
    return get_volumes()


@router.get("/{volume_id}")
def get_volume_endpoint(volume_id: str):
    return get_volume(volume_id)

