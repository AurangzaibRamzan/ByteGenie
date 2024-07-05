from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a SQLite database
engine = create_engine('sqlite:///database/events.db', echo=False, connect_args={'check_same_thread': False})

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
