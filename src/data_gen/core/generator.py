import random
from datetime import datetime, timedelta
from decimal import Decimal
from faker import Faker
from typing import List, Dict, Any

from .types import TableSchema, DataType, Distribution

fake = Faker()

def generate_row(schema: TableSchema) -> Dict[str, Any]:
    """Generate a single row based on schema."""
    row = {}
    for field_name, field_schema in schema.items():
        dtype = field_schema.dtype
        constraints = field_schema.constraints
        if dtype == DataType.INT:
            min_val = constraints.get('min', 0)
            max_val = constraints.get('max', 1000)
            row[field_name] = random.randint(min_val, max_val)
        elif dtype == DataType.STRING:
            length = constraints.get('length', 50)
            row[field_name] = fake.text(max_nb_chars=length)[:-1]  # Trim period
        elif dtype == DataType.FLOAT:
            min_val = constraints.get('min', 0.0)
            max_val = constraints.get('max', 1000.0)
            row[field_name] = random.uniform(min_val, max_val)
        elif dtype == DataType.DECIMAL:
            precision = constraints.get('precision', 10)
            scale = constraints.get('scale', 2)
            row[field_name] = Decimal(random.uniform(0, 10** (precision - scale))).quantize(Decimal(10) ** -scale)
        elif dtype == DataType.DATE:
            start = constraints.get('start', datetime.now() - timedelta(days=365))
            end = constraints.get('end', datetime.now())
            row[field_name] = fake.date_between(start_date=start, end_date=end)
        elif dtype == DataType.BOOLEAN:
            row[field_name] = fake.boolean()
        # TODO: Add more types and distribution logic (e.g., normal via numpy)
    return row

def generate_data(schema: TableSchema, row_count: int) -> List[Dict[str, Any]]:
    """Generate multiple rows."""
    return [generate_row(schema) for _ in range(row_count)]