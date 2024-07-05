
## Database

### database schema
I use SQLite due to its lightweight nature and ease of management for small datasets. SQLAlchemy ORM defines the models for Company, Event, and People in the `/models/` directory.

### The challenges you faced in working with this data
No major challenges were encountered in working with this data.

### How would you improve the database design if you had more time to work on it?
- Create a full join table to optimize LLM model results
- Conduct thorough data analysis to define appropriate data types

## API

### main steps and motivation for any data engineering/processing on the raw data before making it available to the API
Before making data available via the API, we perform the following steps:

1. Convert date columns to datetime
2. Fill missing values with NaN
3. Standardize data:
   - Email addresses
   - Number of employees
   - Company revenue
   - Industry field

The data cleaning script is located at:

```scripts/load_data_from_csv.py```

### the main functionalities of the API

1. Loads data from CSV files
2. Cleans and standardizes the data
3. Saves processed data to SQLite
4. Provides a route for LLM-based text-to-query conversion

### the key challenges you faced in solving the problem

No significant challenges were faced in implementing the API

### how would you improve the backend, if you had more time to work on it?

- Conduct more thorough CSV analysis for enhanced data cleaning
- Explore methods to increase text-to-query accuracy:
  - Refine prompt engineering
  - Test alternative models (e.g., Claude)
  - Implement embedding with vector databases

# setup

1. Install dependencies:

```pip3 install -r requirements.txt```

2. Run the application:

```python3 app.py```

Run pre-commit hooks

```pre-commit run --all-files```
