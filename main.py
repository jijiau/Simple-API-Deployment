from fastapi import FastAPI 
app = FastAPI() 
@app.get("/") 
async def hello() -> dict: 
    return { "message": "Hello World -- Jihan Aurelia 18222001"} 