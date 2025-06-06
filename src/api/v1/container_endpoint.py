from fastapi import APIRouter

from src.services.container_service import get_containers, get_container


router = APIRouter(prefix="/containers", tags=["Containers"])

@router.get("")
def get_containers_endpoint(all: bool = False):
    return get_containers(all)
    

@router.get("/{container_id}")
def get_container_endpoint(container_id: str):
    return get_container(container_id)
