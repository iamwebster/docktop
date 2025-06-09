from fastapi import APIRouter

from src.services.network_service import get_network, get_networks


router = APIRouter(prefix="/network", tags=["Network"])


@router.get("")
def get_networks_endpoint():
    return get_networks()


@router.get("/{network_id}")
def get_network_endpoint(network_id: str):
    return get_network(network_id)
