import pytest
from unittest.mock import MagicMock, patch
from src.services.network_service import get_network, get_networks, serialize_networks
from fastapi import HTTPException
from docker.errors import NotFound


@patch("src.services.network_service.docker_client")
def test_get_networks_success(mock_docker_client):
    fake_network = MagicMock()
    fake_network.id = "123"
    fake_network.name = "Fedya"
    fake_network.containers = []
    fake_network.short_id = "1"

    mock_docker_client.networks.list.return_value = [fake_network]

    result = get_networks()

    assert result[0]["id"] == "123"
    assert result[0]["name"] == "Fedya"
    assert result[0]["containers"] == []
    assert result[0]["short_id"] == "1"


@patch("src.services.network_service.docker_client")
def test_get_network_success(mock_docker_client):
    fake_network = MagicMock()
    fake_network.id = "123"
    fake_network.name = "Fedya"
    fake_network.containers = []
    fake_network.short_id = "1"

    mock_docker_client.networks.get.return_value = fake_network

    result = get_network("123")

    assert result["id"] == "123"
    assert result["name"] == "Fedya"
    assert result["containers"] == []
    assert result["short_id"] == "1"


@patch("src.services.network_service.docker_client")
def test_get_network_error(mock_docker_client):
    mock_docker_client.networks.get.side_effect = NotFound("not found")

    with pytest.raises(HTTPException) as exc:
        get_network("1")

    assert exc.value.status_code == 404
    assert exc.value.detail == "network not found"


def test_serialize_networks():
    fake_network = MagicMock()
    fake_network.id = "123"
    fake_network.name = "Fedya"
    fake_network.containers = []
    fake_network.short_id = "1"

    result = serialize_networks(fake_network)

    assert result["id"] == "123"
    assert result["name"] == "Fedya"
    assert result["containers"] == []
    assert result["short_id"] == "1"
