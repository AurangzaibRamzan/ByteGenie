import pandas as pd
from utils.database_connection import engine
from models.base import Base
from models.people_info import PeopleInfo
from models.event_info import EventInfo
from models.company_info import CompanyInfo
import numpy as np  # Import NumPy for handling NaN val

from utils.standardize_data.generate_email import generate_email
from utils.standardize_data.convert_revenue_to_numeric import convert_revenue_to_numeric
from utils.standardize_data.standardize_employees import standardize_employees
from utils.standardize_data.standardize_industry import standardize_industry


def load_data_from_csv():
    # Create all tables
    Base.metadata.create_all(engine, checkfirst=True)

    try:
        # Load the CSV files into dataframes
        people_df = pd.read_csv("content/people_info.csv")
        events_df = pd.read_csv("content/event_info.csv")
        company_df = pd.read_csv("content/company_info.csv")

        # Convert date columns to datetime
        events_df["event_start_date"] = pd.to_datetime(
            events_df["event_start_date"], errors="coerce"
        )
        events_df["event_end_date"] = pd.to_datetime(
            events_df["event_end_date"], errors="coerce"
        )

        # Fill missing values
        people_df.fillna(np.nan, inplace=True)
        events_df.fillna(np.nan, inplace=True)
        company_df.fillna(np.nan, inplace=True)

        # standardize_data
        people_df["email"] = people_df.apply(generate_email, axis=1)
        company_df["n_employees"] = company_df.apply(standardize_employees, axis=1)
        company_df["company_revenue"] = company_df.apply(
            convert_revenue_to_numeric, axis=1
        )
        company_df["company_industry"] = company_df.apply(standardize_industry, axis=1)

        # Import data into the database
        people_df.to_sql("people_info", engine, if_exists="replace", index=False)
        events_df.to_sql("event_info", engine, if_exists="replace", index=False)
        company_df.to_sql("company_info", engine, if_exists="replace", index=False)

        print("Data imported successfully!")
    except Exception as e:
        print("An error occurred:", e)
