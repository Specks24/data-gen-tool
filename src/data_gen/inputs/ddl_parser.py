import sqlparse
from typing import Dict

from ..core.types import TableSchema, FieldSchema, DataType

def parse_ddl(ddl: str) -> TableSchema:
    """Parse SQL DDL to extract schema."""
    parsed = sqlparse.parse(ddl)[0]
    schema = {}
    if parsed.get_type() == 'CREATE':
        table_name = parsed.token_next(2)[0].value  # Skip CREATE TABLE
        columns = parsed.token_next(parsed.token_next(4)).tokens  # Get column defs
        for token in columns:
            if isinstance(token, sqlparse.sql.TokenList):
                name = token[0].value
                dtype_str = token[1].value.upper()
                if 'INT' in dtype_str:
                    schema[name] = FieldSchema(name, DataType.INT)
                elif 'VARCHAR' in dtype_str or 'STRING' in dtype_str:
                    schema[name] = FieldSchema(name, DataType.STRING)
                elif 'DECIMAL' in dtype_str:
                    schema[name] = FieldSchema(name, DataType.DECIMAL)
                elif 'DATE' in dtype_str:
                    schema[name] = FieldSchema(name, DataType.DATE)
                # TODO: Handle more types, constraints (e.g., PRIMARY KEY)
    return schema