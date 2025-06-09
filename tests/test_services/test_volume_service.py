from src.services.volume_service import get_volume, get_volumes, serialize_volume
from unittest.mock import MagicMock, patch
import pytest
from docker.errors import NotFound
from fastapi import HTTPException


@patch("src.services.volume_service.docker_client")
def test_get_volume_success(mock_docker_client):
    fake_volume = MagicMock()
    fake_volume.id = "123"
    fake_volume.name = "Oleg"
    fake_volume.short_id = "1"

    mock_docker_client.volumes.get.return_value = fake_volume

    result = get_volume("123")
    assert result["id"] == "123"
    assert result["name"] == "Oleg"
    assert result["short_id"] == "1"


@patch("src.services.volume_service.docker_client")
def test_get_volumes_success(mock_docker_client):
    fake_volume = MagicMock()
    fake_volume.id = "123"
    fake_volume.name = "Anton"
    fake_volume.short_id = "12"

    mock_docker_client.volumes.list.return_value = [fake_volume]
    result = get_volumes()

    assert result[0]["id"] == "123"
    assert result[0]["name"] == "Anton"
    assert result[0]["short_id"] == "12"


@patch("src.services.volume_service.docker_client")
def test_get_volume_error(mock_docker_client):

    mock_docker_client.volumes.get.side_effect = NotFound("not found")

    with pytest.raises(HTTPException) as exc:
        get_volume("1")

    assert exc.value.status_code == 404
    assert exc.value.detail == "volume not found"


def test_serialize_volume():
    fake_volume = MagicMock()
    fake_volume.id = "123"
    fake_volume.name = "Denis"
    fake_volume.short_id = "12"

    result = serialize_volume(fake_volume)

    assert result["id"] == "123"
    assert result["name"] == "Denis"
    assert result["short_id"] == "12"
