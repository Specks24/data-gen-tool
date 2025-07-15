from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseWriter(ABC):
    """Abstract base for data writers."""
    @abstractmethod
    def write(self, data: List[Dict[str, Any]], output_path: str):
        pass