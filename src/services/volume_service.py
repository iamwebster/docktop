from src.integrations.docker_client import docker_client
from docker.models.volumes import Volume
from docker.errors import NotFound
from src.utils.exceptions import not_found_error


def serialize_volume(volume: Volume) -> dict:
    return {"id": volume.id, "name": volume.name, "short_id": volume.short_id}


def get_volumes() -> list[dict]:
    return [serialize_volume(volume) for volume in docker_client.volumes.list()]


def get_volume(volume_id: str) -> dict:
    try:
        volume = docker_client.volumes.get(volume_id)
    except NotFound:
        raise not_found_error("volume")

    return serialize_volume(volume)
