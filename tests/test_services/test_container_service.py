import pytest 
from unittest.mock import patch, MagicMock
from docker.errors import NotFound
from fastapi import HTTPException

from src.services.container_service import get_container, get_containers, serialize_container


@patch("src.services.container_service.docker_client")
def test_get_container_success(mock_docker_client):
    fake_container = MagicMock()
    fake_container.id = "abc"
    fake_container.name = "nginx"
    fake_container.status = "nginx"
    fake_container.ports = {}

    mock_docker_client.containers.get.return_value = fake_container

    result = get_container("abc")

    assert result["id"] == "abc"
    assert result["name"] == "nginx"


@patch("src.services.container_service.docker_client")
def test_get_container_not_found(mock_docker_client):
    mock_docker_client.containers.get.side_effect = NotFound("not found")

    with pytest.raises(HTTPException) as exc:
        get_container("missing")

    assert exc.value.status_code == 404
    assert "not found" in exc.value.detail


def test_serialize_container():
    fake_container = MagicMock()
    fake_container.id = "123"
    fake_container.status = "ok"
    fake_container.ports = {}
    fake_container.name = "Oleg"


    result = serialize_container(fake_container)

    assert result["id"] == "123"
    assert result["status"] == "ok"
    assert result["ports"] == {}
    assert result["name"] == "Oleg"


@patch("src.services.container_service.docker_client")
def test_get_containers(mock_docker_client):
    fake_container = MagicMock()
    fake_container.id = "123"
    fake_container.status = "ok"
    fake_container.ports = {}
    fake_container.name = "Oleg"

    mock_docker_client.containers.list.return_value = [fake_container]

    result = get_containers(all=True)
    assert result[0]["id"] == "123"
    assert result[0]["status"] == "ok"
    assert result[0]["ports"] == {}
    assert result[0]["name"] == "Oleg"
