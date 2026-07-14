from fastapi import FastAPI

app = FastAPI(
    title="AI Developer OS",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {
        "message": "Live Reload Works!"
    }
