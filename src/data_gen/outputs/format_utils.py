# Utilities for output formatting, e.g., converting data to specific formats
def data_to_df(data: List[Dict[str, Any]]) -> 'pd.DataFrame':
    import pandas as pd
    return pd.DataFrame(data)