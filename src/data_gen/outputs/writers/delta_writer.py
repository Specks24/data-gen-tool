from typing import List, Dict, Any
from pyspark.sql import SparkSession
import pandas as pd

from .base_writer import BaseWriter

class DeltaWriter(BaseWriter):
    def write(self, data: List[Dict[str, Any]], output_path: str):
        spark = SparkSession.builder \
            .appName("DataGenDelta") \
            .config("spark.jars.packages", "io.delta:delta-spark_2.12:3.2.0") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .getOrCreate()
        pdf = pd.DataFrame(data)
        df = spark.createDataFrame(pdf)
        df.write.format("delta").mode("overwrite").save(output_path)