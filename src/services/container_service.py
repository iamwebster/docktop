from src.integrations.docker_client import docker_client
from docker.models.containers import Container
from docker.errors import NotFound
from src.utils.exceptions import not_found_error


def serialize_container(container: Container) -> dict:
    return {
        "id": container.id,
        "status": container.status,
        "ports": container.ports,
        "name": container.name,
    }


def get_containers(all: bool = False) -> list[dict]:
    return [serialize_container(container) for container in docker_client.containers.list(all=all)]


def get_container(container_id: str) -> dict:
    try:
        container = docker_client.containers.get(container_id)
    except NotFound:
        raise not_found_error("container")
    
    return serialize_container(container)
