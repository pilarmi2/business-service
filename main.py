import os

from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn

from src.routers import score

# load environment variables
port = int(os.environ["PORT"])
host = os.environ["HOST"]

app = FastAPI()
app.include_router(score.router)


@app.get("/", include_in_schema=False, response_class=RedirectResponse)
async def api_spec():
    return "/docs"


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
