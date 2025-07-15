from fastapi import APIRouter

router = APIRouter()

@router.post("/infer-schema")
def infer_schema(body: dict):
    # TODO: Implement using inputs
    return {"status": "stub"}