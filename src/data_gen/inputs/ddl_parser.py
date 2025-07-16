from typing import Dict
from simple_ddl_parser import DDLParser

from ..core.types import TableSchema, FieldSchema, DataType

def parse_ddl(ddl: str) -> TableSchema:
    """Parse SQL DDL using simple-ddl-parser."""
    parse_results = DDLParser(ddl).run(output_mode="sql")
    if not parse_results:
        raise ValueError("Invalid DDL")
    
    table_info = parse_results[0]  # First table
    schema = {}
    for col in table_info['columns']:
        name = col['name']
        dtype_str = col['type'].upper()
        constraints = {
            'nullable': not col.get('nullable', True),
            'primary_key': col.get('primary_key', False),
        }
        if 'size' in col:
            if isinstance(col['size'], tuple):  # e.g., DECIMAL(10,2)
                constraints['precision'], constraints['scale'] = col['size']
            else:
                constraints['length'] = col['size']
        
        # Map to our DataType
        if 'INT' in dtype_str:
            dtype = DataType.INT
        elif 'VARCHAR' in dtype_str or 'STRING' in dtype_str:
            dtype = DataType.STRING
        elif 'DECIMAL' in dtype_str:
            dtype = DataType.DECIMAL
        elif 'FLOAT' in dtype_str:
            dtype = DataType.FLOAT
        elif 'DATE' in dtype_str:
            dtype = DataType.DATE
        elif 'TIMESTAMP' in dtype_str:
            dtype = DataType.TIMESTAMP
        elif 'BOOLEAN' in dtype_str:
            dtype = DataType.BOOLEAN
        else:
            dtype = DataType.STRING  # Fallback
        
        schema[name] = FieldSchema(name, dtype, constraints)
    
    return schema