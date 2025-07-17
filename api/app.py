# app.py (api/): FastAPI application for API endpoints.
# Provides a /generate endpoint for data generation via HTTP.
# This is a stub for future expansion into a full API service.

from fastapi import FastAPI, UploadFile, File
from data_gen.parsers import infer_from_ddl, infer_from_sample
from data_gen.generators import generate_rows
from data_gen.writers import get_writer
import tempfile
import os

app = FastAPI()  # Initialize FastAPI app.

@app.post("/generate")  # POST endpoint for generation.
async def generate(ddl: str = None, sample: UploadFile = File(None), num_rows: int = 100, format: str = "csv"):
    """
    API endpoint to generate data.

    Supports DDL or uploaded sample file for schema inference.

    Parameters (via query/body):
    - ddl (str, optional): SQL DDL.
    - sample (UploadFile, optional): Sample file upload.
    - num_rows (int): Rows to generate.
    - format (str): Output format.

    Returns:
    - Dict: Message and file path (in production, serve file download).
    """
    # Infer schema from DDL if provided.
    if ddl:
        schema = infer_from_ddl(ddl)
    # Handle uploaded sample file.
    elif sample:
        # Write upload to temp file for inference.
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await sample.read())
            schema = infer_from_sample(tmp.name)
        os.unlink(tmp.name)  # Clean up temp file.
    else:
        return {"error": "Provide DDL or sample file."}

    # Generate and materialize data.
    data = list(generate_rows(num_rows, schema))
    output_path = f"output.{format}"  # Simple output path; enhance for production.
    writer = get_writer(format)
    writer.write(data, output_path)
    return {"message": "Generated", "file": output_path}  # Return info; add download in future.