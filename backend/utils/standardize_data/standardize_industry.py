import pandas as pd
import re


def standardize_industry(row):
    industry = row["company_industry"]
    if pd.isna(industry):
        return industry
    return re.sub(r"[^a-z\s]", "", industry.lower().strip())
