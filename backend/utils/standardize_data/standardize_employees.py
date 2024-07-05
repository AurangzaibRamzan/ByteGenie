import pandas as pd
import re


# Standardize n_employees
def standardize_employees(row):
    n_employees = row["n_employees"]
    if pd.isna(n_employees):
        return None

    # Remove any '+' sign
    n_employees = (
        str(n_employees).replace("+", "").replace(",", "").replace("employees", "")
    )

    # Check if there is a '-' in the string
    if "-" in n_employees:
        # Split by '-' and convert each part to integer
        parts = [float(x) for x in n_employees.split("-")]
        return int(max(parts))
    # If no '-', directly convert to integer
    return int(float(n_employees))
