from fastapi import FastAPI

app = FastAPI(title="City Temperature Management API")

@app.get("/health")
def health():
    return {"status": "ok"}
