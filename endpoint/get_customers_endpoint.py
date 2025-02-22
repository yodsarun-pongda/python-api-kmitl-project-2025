from fastapi import APIRouter

router = APIRouter()

@router.get("/customers")
async def get_users():
    return {"customers": ["Alice", "Bob", "Charlie"]}