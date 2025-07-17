# test_generators.py: Unit tests for the generators module.
# Verifies basic row generation.

import pytest
from data_gen.generators import generate_rows

def test_generate_rows():
    """
    Test generation of rows with a simple schema.
    """
    schema = {'id': 'INT', 'name': 'VARCHAR'}  # Sample schema.
    rows = list(generate_rows(2, schema))  # Generate 2 rows.
    assert len(rows) == 2  # Check number of rows.
    assert 'id' in rows[0] and 'name' in rows[0]  # Check columns present.