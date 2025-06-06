from fastapi import APIRouter
import docker 


router = APIRouter(prefix="/containers")

docker_client = docker.from_env()

@router.get("")
async def get_containers():
    pass 
    
