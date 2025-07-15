from typing import Dict

from ..core.types import TableSchema

def validate_schema(schema: TableSchema) -> bool:
    """Basic schema validation."""
    return bool(schema)  # TODO: Add checks for types/constraints