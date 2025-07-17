# writers.py: Module for writing generated data to various formats.
# Uses a factory pattern for extensibility (easy to add new formats).
# Supports CSV, TXT, Parquet, and Delta (with optional Spark).

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
# Import pyspark if available for Delta support.
try:
    from pyspark.sql import SparkSession
    SPARK_AVAILABLE = True  # Flag to indicate if Spark is available.
except ImportError:
    SPARK_AVAILABLE = False  # No Spark if import fails.

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Writer(ABC):
    """
    Abstract base class for data writers.

    Subclasses must implement the write method.
    """
    @abstractmethod
    def write(self, data: List[Dict], path: str):
        """
        Write data to the specified path.

        Parameters:
        - data (List[Dict]): List of row dictionaries.
        - path (str): Output file path.
        """
        pass

class CSVWriter(Writer):
    """
    Writer for CSV format using Pandas.
    """
    def write(self, data: List[Dict], path: str):
        pd.DataFrame(data).to_csv(path, index=False)  # Convert to DF and write CSV without index.

class TXTWriter(Writer):
    """
    Writer for tab-delimited TXT format using Pandas.
    """
    def write(self, data: List[Dict], path: str):
        pd.DataFrame(data).to_csv(path, sep='\t', index=False)  # Write as TSV.

class ParquetWriter(Writer):
    """
    Writer for Parquet format using PyArrow.
    """
    def write(self, data: List[Dict], path: str):
        # Convert to Pandas DF, then to Arrow Table, and write Parquet.
        table = pa.Table.from_pandas(pd.DataFrame(data))
        pq.write_table(table, path)

class DeltaWriter(Writer):
    """
    Writer for Delta Lake format using PySpark.
    """
    def __init__(self):
        if not SPARK_AVAILABLE:
            raise ImportError("PySpark not installed for Delta support.")
        # Initialize Spark session if available.
        self.spark = SparkSession.builder.appName("DataGen").getOrCreate()

    def write(self, data: List[Dict], path: str):
        # Create Spark DataFrame and write as Delta table in overwrite mode.
        df = self.spark.createDataFrame(data)
        df.write.format('delta').mode('overwrite').save(path)

def get_writer(format: str) -> Writer:
    """
    Factory function to get the appropriate Writer instance.

    Parameters:
    - format (str): The output format (e.g., 'csv').

    Returns:
    - Writer: Instance of the corresponding writer class.

    Raises:
    - ValueError: If format is unsupported.
    """
    formats = {  # Dictionary mapping formats to writer instances.
        'csv': CSVWriter(),
        'txt': TXTWriter(),
        'parquet': ParquetWriter(),
        'delta': DeltaWriter(),
    }
    if format in formats:
        return formats[format]
    raise ValueError(f"Unsupported format: {format}")