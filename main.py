from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "microservice-2", "status": "ok"}
