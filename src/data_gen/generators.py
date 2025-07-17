# generators.py: Module for generating synthetic data rows based on schema.
# Uses Faker for basic data, NumPy/SciPy for distributions, and supports heuristics.
# Designed as a generator for memory efficiency with large datasets.

from faker import Faker
import numpy as np
import scipy.stats as stats
from typing import Generator, Dict, Any

fake = Faker()  # Initialize Faker instance for generating fake data.

TYPE_MAP = {  # Mapping of SQL types to default generation functions.
    'INT': lambda: fake.random_int(min=0, max=1000),  # Generate random integer.
    'VARCHAR': lambda: fake.word(),  # Generate random word as string.
    'FLOAT': lambda: fake.random_number(decimals=2),  # Generate random float.
    # Add more types as needed (e.g., 'DATE': fake.date).
}

def generate_rows(num_rows: int, schema: Dict[str, str], heuristics: Dict[str, Dict] = None) -> Generator[Dict[str, Any], None, None]:
    """
    Generate rows of data based on schema and optional heuristics.

    Yields rows one-by-one to avoid loading large datasets into memory.

    Parameters:
    - num_rows (int): Number of rows to generate.
    - schema (Dict[str, str]): Column names and types.
    - heuristics (Dict[str, Dict], optional): Per-column distribution params (e.g., {'age': {'distribution': 'normal', 'mean': 30, 'std': 5}}).

    Yields:
    - Dict[str, Any]: A single row of generated data.
    """
    heuristics = heuristics or {}  # Default to empty dict if no heuristics provided.
    for _ in range(num_rows):  # Loop to generate each row.
        row = {}  # Initialize empty row dictionary.
        for col, type_ in schema.items():  # Iterate over each column in schema.
            if col in heuristics:  # Check for custom heuristics.
                dist = heuristics[col].get('distribution', 'uniform')  # Get distribution type.
                if dist == 'normal':  # Normal distribution example.
                    mean = heuristics[col].get('mean', 0)
                    std = heuristics[col].get('std', 1)
                    row[col] = np.random.normal(mean, std)  # Generate value.
                elif dist == 'poisson':  # Poisson distribution example.
                    lam = heuristics[col].get('lambda', 1)
                    row[col] = stats.poisson.rvs(lam)  # Generate value.
                # Add more distributions (e.g., lognormal, uniform) as needed.
            else:  # Use default generator based on type.
                generator = TYPE_MAP.get(type_, lambda: None)  # Fallback to None if type unknown.
                row[col] = generator()
        yield row  # Yield the completed row.