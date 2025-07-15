from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
def generate_data(body: dict):
    # TODO: Implement using core generator
    return {"status": "stub"}