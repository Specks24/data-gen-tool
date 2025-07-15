from typing import List, Dict, Any

from .base_writer import BaseWriter

class TXTWriter(BaseWriter):
    def write(self, data: List[Dict[str, Any]], output_path: str):
        with open(output_path, 'w') as f:
            for row in data:
                f.write(str(row) + '\n')