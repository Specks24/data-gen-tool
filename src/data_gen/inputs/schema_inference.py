import pandas as pd
from typing import Dict

from ..core.types import TableSchema, FieldSchema, DataType

def infer_schema_from_sample(file_path: str) -> TableSchema:
    """Infer schema from sample CSV/Parquet."""
    df = pd.read_csv(file_path)  # TODO: Support Parquet via pd.read_parquet
    schema = {}
    for col in df.columns:
        dtype = df[col].dtype
        if 'int' in str(dtype):
            schema[col] = FieldSchema(col, DataType.INT)
        elif 'float' in str(dtype):
            schema[col] = FieldSchema(col, DataType.FLOAT)
        elif 'object' in str(dtype):
            schema[col] = FieldSchema(col, DataType.STRING)
        # TODO: Infer distributions from data stats (e.g., min/max)
    return schema