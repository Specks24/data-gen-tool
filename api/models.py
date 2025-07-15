from pydantic import BaseModel

class GenerateRequest(BaseModel):
    ddl: str | None = None
    sample_path: str | None = None
    row_count: int = 100
    format: str