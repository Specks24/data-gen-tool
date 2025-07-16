import random
from datetime import datetime, timedelta
from decimal import Decimal
from faker import Faker
from typing import List, Dict, Any

from .types import TableSchema, DataType, Distribution

fake = Faker()

def generate_row(schema: TableSchema, row_index: int = 0) -> Dict[str, Any]:
    """Generate a single row based on schema, with heuristics for realistic data."""
    row = {}
    for field_name, field_schema in schema.items():
        dtype = field_schema.dtype
        constraints = field_schema.constraints
        fname_lower = field_name.lower()
        
        if dtype == DataType.INT:
            if 'id' in fname_lower:
                # Sequential for IDs (unique; start from 1)
                row[field_name] = row_index + 1
            elif 'age' in fname_lower:
                min_val = constraints.get('min', 18)
                max_val = constraints.get('max', 90)
                row[field_name] = random.randint(min_val, max_val)
            else:
                min_val = constraints.get('min', 0)
                max_val = constraints.get('max', 1000)
                row[field_name] = random.randint(min_val, max_val)
        elif dtype == DataType.STRING:
            length = constraints.get('length', 50)
            if 'name' in fname_lower:
                row[field_name] = fake.name()[:length]  # Realistic name, truncated if needed
            elif 'email' in fname_lower:
                row[field_name] = fake.email()[:length]
            elif 'address' in fname_lower:
                row[field_name] = fake.address().replace('\n', ', ')[:length]  # Flatten newlines
            else:
                # General string: single sentence to avoid newlines
                row[field_name] = fake.sentence(nb_words=random.randint(3, 8))[:length].rstrip('.')
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
        # TODO: Add distribution logic (e.g., normal via numpy.random), more heuristics/providers
    return row

def generate_data(schema: TableSchema, row_count: int) -> List[Dict[str, Any]]:
    """Generate multiple rows, passing index for sequential fields."""
    return [generate_row(schema, row_index=i) for i in range(row_count)]