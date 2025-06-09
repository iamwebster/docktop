import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from docker.errors import ImageNotFound

from src.services.image_service import get_image, get_images, serialize_image


@patch("src.services.image_service.docker_client")
def test_get_image_success(mock_docker_client):
    fake_image = MagicMock()
    fake_image.id = "123"
    fake_image.labels = {}
    fake_image.short_id = "1"
    fake_image.tags = []

    mock_docker_client.images.get.return_value = fake_image

    result = get_image("123")

    result["id"] = "123"
    result["labels"] = {}
    result["short_id"] = "1"
    result["tags"] = []


@patch("src.services.image_service.docker_client")
def test_get_image_not_found(mock_docker_client):
    mock_docker_client.images.get.side_effect = ImageNotFound("image not found")

    with pytest.raises(HTTPException) as exc:
        get_image("error")

    assert exc.value.status_code == 404
    assert "image not found" in exc.value.detail


@patch("src.services.image_service.docker_client")
def test_get_images_success(mock_docker_client):
    fake_image = MagicMock()
    fake_image.id = "123"
    fake_image.labels = {}
    fake_image.short_id = "1"
    fake_image.tags = []

    mock_docker_client.images.list.return_value = [fake_image]

    result = get_images()

    result[0]["id"] = "123"
    result[0]["labels"] = {}
    result[0]["short_id"] = "1"
    result[0]["tags"] = []


def test_serialize_image():
    fake_image = MagicMock()
    fake_image.id = "123"
    fake_image.labels = {}
    fake_image.short_id = "1"
    fake_image.tags = []

    result = serialize_image(fake_image)

    result["id"] = "123"
    result["labels"] = {}
    result["short_id"] = "1"
    result["tags"] = []
