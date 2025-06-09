from fastapi import FastAPI

from src.api.v1 import (
    container_endpoint,
    image_endpoint,
    volume_endpoint,
    network_endpoint,
)


app = FastAPI()
app.include_router(container_endpoint.router)
app.include_router(image_endpoint.router)
app.include_router(volume_endpoint.router)
app.include_router(network_endpoint.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", reload=True)
