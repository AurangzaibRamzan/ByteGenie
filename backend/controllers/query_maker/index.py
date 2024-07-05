from utils.text_to_sql import text_to_sql
from sqlalchemy.exc import SQLAlchemyError
from utils.database_connection import session
from fastapi import HTTPException


async def query_maker(query):
    try:
        sql_query = text_to_sql(query)
        session_query = session.execute(sql_query)
        column_names = session_query.keys()
        results = session_query.fetchall()
        data = [dict(zip(column_names, row)) for row in results]
        return {"data": data, "sql_query": sql_query}
    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
