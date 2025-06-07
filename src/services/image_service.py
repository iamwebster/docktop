from src.integrations.docker_client import docker_client
from docker.models.images import Image 
from docker.errors import ImageNotFound
from src.utils.exceptions import not_found_error


def serialize_image(image: Image) -> dict:
    return {
        "id": image.id,
        "labels": image.labels,
        "short_id": image.short_id,
        "tags": image.tags
    }

def get_images() -> list[dict]:
    return [serialize_image(image) for image in docker_client.images.list()]

def get_image(image_id: str) -> dict:
    try:
        image = docker_client.images.get(image_id)
    except ImageNotFound:
        raise not_found_error("image")
    
    return serialize_image(image)