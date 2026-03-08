from fastapi import FastAPI

app = FastAPI(title="Framework Selector API")

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}