from src.integrations.docker_client import docker_client
from docker.models.networks import Network
from docker.errors import NotFound
from src.utils.exceptions import not_found_error


def serialize_networks(network: Network) -> dict:
    return {
        "id": network.id,
        "name": network.name,
        "containers": network.containers,
        "short_id": network.short_id,
    }


def get_networks() -> list[dict]:
    return [serialize_networks(network) for network in docker_client.networks.list()]


def get_network(network_id: str) -> dict:
    try:
        network = docker_client.networks.get(network_id)
    except NotFound:
        raise not_found_error("network")

    return serialize_networks(network)
