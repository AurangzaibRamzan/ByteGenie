import pandas as pd


def generate_email(row):
    if (
        pd.isna(row["first_name"])
        or pd.isna(row["last_name"])
        or pd.isna(row["email_pattern"])
    ):
        return None

    first_name = row["first_name"].lower()
    last_name = row["last_name"].lower()
    first_initial = first_name[0]
    last_initial = last_name[0]
    pattern = row["email_pattern"]
    base_url = row["homepage_base_url"]

    email = (
        pattern.replace("[first_initial]", first_initial)
        .replace("[last_initial]", last_initial)
        .replace("[first]", first_name)
        .replace("[last]", last_name)
        .replace(".", "")
        + "@"
        + base_url
    )
    return email
