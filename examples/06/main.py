import uvicorn
from fastapi import FastAPI

import controller
from container import Container


def create_app() -> FastAPI:
    container = Container()
    container.config.from_yaml("config.yml")
    container.wire(modules=[controller])

    app = FastAPI()
    app.include_router(controller.router)
    app.container = container
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
