# test_parsers.py: Unit tests for the parsers module.
# Uses pytest to verify schema inference functionality.

import pytest
from data_gen.parsers import infer_from_ddl

def test_infer_from_ddl():
    """
    Test DDL inference with a simple CREATE TABLE statement.
    """
    ddl = "CREATE TABLE test (id INT, name VARCHAR)"  # Sample DDL.
    schema = infer_from_ddl(ddl)  # Call function.
    assert schema == {'id': 'INT', 'name': 'VARCHAR'}  # Verify output.