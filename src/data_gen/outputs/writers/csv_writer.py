from typing import List, Dict, Any
import pandas as pd

from .base_writer import BaseWriter

class CSVWriter(BaseWriter):
    def write(self, data: List[Dict[str, Any]], output_path: str):
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)