from src.integrations.docker_client import docker_client
from docker.models.containers import Container
from docker.errors import NotFound
from fastapi import HTTPException, status


def serialize_container(container: Container) -> dict:
    return {
        "id": container.id,
        "status": container.status,
        "ports": container.ports,
        "name": container.name,
    }


def get_containers(all: bool = False) -> list[dict]:
    containers: list[Container] = docker_client.containers.list(all=all)
    return [serialize_container(container) for container in containers]


def get_container(container_id: str) -> dict:
    try:
        container = docker_client.containers.get(container_id)
    except NotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="container not found")
    
    return serialize_container(container)
