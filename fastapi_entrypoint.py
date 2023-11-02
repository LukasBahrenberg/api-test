from fastapi import FastAPI, HTTPException
from fastapi.routing import APIRoute
import uvicorn
from pydantic import BaseModel


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)


class ResponseMessage(BaseModel):
    message: str


@app.get("/", response_model=ResponseMessage, tags=["health"])
async def health():
    return {"message": "alive"}


if __name__ == "__main__":
    uvicorn.run(
        "fastapi_entrypoint:app",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        reload=True,
    )
