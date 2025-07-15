from enum import Enum
from typing import Dict, Any, Optional

class DataType(Enum):
    """Supported data types for generation."""
    INT = 'int'
    STRING = 'string'
    FLOAT = 'float'
    DECIMAL = 'decimal'
    DATE = 'date'
    TIMESTAMP = 'timestamp'
    BOOLEAN = 'boolean'

class Distribution(Enum):
    """Data distributions for generation."""
    UNIFORM = 'uniform'
    NORMAL = 'normal'
    FIXED = 'fixed'  # For constants

class FieldSchema:
    """Schema for a single field/column."""
    def __init__(self, name: str, dtype: DataType, constraints: Optional[Dict[str, Any]] = None, distribution: Distribution = Distribution.UNIFORM):
        self.name = name
        self.dtype = dtype
        self.constraints = constraints or {}  # e.g., {'min': 0, 'max': 100} for int
        self.distribution = distribution

TableSchema = Dict[str, FieldSchema]  # Schema as dict of field name to FieldSchema