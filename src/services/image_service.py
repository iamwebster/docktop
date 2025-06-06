from src.integrations.docker_client import docker_client
from docker.models.images import Image 
from fastapi import HTTPException, status
from docker.errors import ImageNotFound


def servialize_image(image: Image) -> dict:
    return {
        "id": image.id,
        "labels": image.labels,
        "short_id": image.short_id,
        "tags": image.tags
    }

def get_images() -> list[dict]:
    images = docker_client.images.list()
    return [servialize_image(image) for image in images]

def get_image(image_id: str) -> dict:
    try:
        image = docker_client.images.get(image_id)
    except ImageNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="image not found")
    
    return servialize_image(image)