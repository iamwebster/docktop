from fastapi import FastAPI

from src.api.v1 import container_endpoint


app = FastAPI()
app.include_router(container_endpoint.router)


if __name__ == "__main__":
    import uvicorn 

    uvicorn.run("src.main:app", reload=True)
