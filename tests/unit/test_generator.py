import pytest
from data_gen.core.generator import generate_row
from data_gen.core.types import TableSchema, FieldSchema, DataType

def test_generate_row():
    schema = {'id': FieldSchema('id', DataType.INT)}
    row = generate_row(schema)
    assert isinstance(row['id'], int)