from sqlalchemy import create_engine, inspect, text
from utils.database_connection import engine  # Assuming you have a database connection setup here
from utils.openai_conntection import connect_open_ai

def get_schema_with_relations():
    inspector = inspect(engine)
    schema = []

    relationships = {
        'people_info': [('homepage_base_url', 'company_info', 'homepage_base_url')],
        'company_info': [('event_url', 'event_info', 'event_url')],
        'event_info': []
    }

    for table_name in inspector.get_table_names():
        schema.append(f"Table: {table_name}")
        schema.append("Columns:")
        for column in inspector.get_columns(table_name):
            schema.append(f"  - {column['name']} ({column['type']})")
        
        if table_name in relationships:
            schema.append("Relationships:")
            for rel in relationships[table_name]:
                schema.append(f"  - {rel[0]} references {rel[1]}({rel[2]})")
        
        schema.append("")

    return "\n".join(schema)

def generate_query(prompt, schema):
    openai = connect_open_ai()  # Connect to OpenAI
    messages = [
        {"role": "system", "content": "You are a SQLite query generate and provides only SQL queries. Given a schema with table relationships and a natural language prompt, your task is to generate the appropriate SQLite query. Use joins when necessary based on the relationships provided. use like in query if searching something to get more result"},
        {"role": "user", "content": f"Here's the schema of the database, including relationships:\n\n{schema}\n\nBased on this schema, generate a SQLite query for the following prompt:\n\n{prompt}"}
    ]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        n=1,
        temperature=0.7,
    )
    return text(response.choices[0].message.content.strip('sql```\n').strip())

def text_to_sql(prompt):
    schema = get_schema_with_relations()
    query = generate_query(prompt, schema)
    return query


