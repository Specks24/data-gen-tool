# test_writers.py: Unit tests for the writers module.
# Tests file creation for CSV writer.

import pytest
import os
from data_gen.writers import get_writer

def test_csv_writer():
    """
    Test CSV writer by writing data and checking file existence.
    """
    data = [{'id': 1, 'name': 'test'}]  # Sample data.
    writer = get_writer('csv')  # Get CSV writer.
    path = 'test.csv'  # Test path.
    writer.write(data, path)  # Write file.
    assert os.path.exists(path)  # Verify file created.
    os.remove(path)  # Clean up.