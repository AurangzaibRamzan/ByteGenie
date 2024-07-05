import pandas as pd
import re


# Standardize company_revenue
def convert_revenue_to_numeric(row):
    revenue = row["company_revenue"]
    if pd.isna(revenue):
        return None
    revenue = revenue.lower().replace(",", "").replace("usd", "")
    if "million" in revenue:
        return float(re.findall(r"\d+\.\d+|\d+", revenue)[0]) * 1e6
    if "billion" in revenue:
        return float(re.findall(r"\d+\.\d+|\d+", revenue)[0]) * 1e9
    return float(re.findall(r"\d+\.\d+|\d+", revenue)[0])
