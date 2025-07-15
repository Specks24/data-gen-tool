import pytest
from data_gen.outputs.writers.csv_writer import CSVWriter

def test_csv_writer(tmp_path):
    data = [{'id': 1}]
    writer = CSVWriter()
    path = tmp_path / 'test.csv'
    writer.write(data, str(path))
    assert path.exists()