from fastapi import APIRouter

from src.services.docker_service import get_containers, get_container


router = APIRouter(prefix="/containers")

@router.get("")
async def get_containers_endpoint(all: bool = False):
    return get_containers(all)
    
    
@router.get("/{container_id}")
async def get_container_endpoint(container_id: str):
    return get_container(container_id)
