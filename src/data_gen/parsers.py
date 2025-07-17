# parsers.py: Module for inferring data schemas from various sources.
# Supports SQL DDL parsing and sample file inference.
# This is a core module for schema extraction, used by CLI, API, and web components.

import sqlparse
import pandas as pd
from typing import Dict, Any

def infer_from_ddl(ddl_str: str) -> Dict[str, str]:
    """
    Parse a SQL DDL string to extract column names and types.

    This function uses sqlparse to tokenize and extract column definitions
    from a CREATE TABLE statement.

    Parameters:
    - ddl_str (str): The SQL DDL string (e.g., "CREATE TABLE test (id INT, name VARCHAR)").

    Returns:
    - Dict[str, str]: A dictionary mapping column names to their data types.

    Raises:
    - ValueError: If the DDL is invalid or cannot be parsed.
    """
    try:
        # Parse the DDL statement.
        parsed = sqlparse.parse(ddl_str)[0]
        columns = {}  # Dictionary to hold column name-type pairs.
        in_columns = False  # Flag to track if we're inside the column definition section.
        for token in parsed.tokens:
            # Detect start of column list.
            if str(token).strip() == '(':
                in_columns = True
            # Detect end of column list.
            elif str(token).strip() == ')':
                in_columns = False
            # Extract column name and type if inside columns and token is an identifier.
            elif in_columns and isinstance(token, sqlparse.sql.Identifier):
                parts = str(token).split()  # Split into name and type.
                if len(parts) >= 2:
                    name = parts[0].strip('`')  # Clean column name.
                    type_ = parts[1]  # Data type.
                    columns[name] = type_
        return columns
    except Exception as e:
        raise ValueError(f"Invalid DDL: {e}")

def infer_from_sample(file_path: str) -> Dict[str, Any]:
    """
    Infer schema from a sample file (currently supports CSV).

    Uses Pandas to read the file and extract column names and types.

    Parameters:
    - file_path (str): Path to the sample file.

    Returns:
    - Dict[str, Any]: Dictionary of column names to Pandas dtype strings.

    Raises:
    - ValueError: If the file cannot be read or inferred.
    """
    try:
        # Read the CSV file into a DataFrame.
        df = pd.read_csv(file_path)  # Extend for other formats if needed (e.g., pd.read_excel).
        # Convert dtypes to string for consistency.
        return {col: str(dtype) for col, dtype in df.dtypes.items()}
    except Exception as e:
        raise ValueError(f"Could not infer from sample: {e}")