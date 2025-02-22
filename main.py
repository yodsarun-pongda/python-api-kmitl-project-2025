import os
import importlib
from fastapi import FastAPI

app = FastAPI()

module_path = "endpoint"
for filename in os.listdir(module_path):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"{module_path}.{filename[:-3]}"
        module = importlib.import_module(module_name)
        if hasattr(module, "router"):
            app.include_router(module.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World, From Main!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")