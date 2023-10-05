from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"appVersion": "2.53.0", "osVersion": "7"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
