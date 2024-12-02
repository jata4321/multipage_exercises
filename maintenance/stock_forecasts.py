from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from presentation.database_operations import CPIYPL
import os

# Path to your SQLite database
database_path = "sqlite:///../database/data.sqlite3"

# Create an SQLAlchemy engine
engine = create_engine(database_path)
Session = sessionmaker(bind=engine)
session = Session()

# Replace `YourModel` with the appropriate SQLAlchemy model class
def fetch_data(session=session):
    # Use ORM query methods, assuming models are defined
    return session.query(CPIYPL).all()


# Fetch data
data = fetch_data()

# Use Streamlit to display the data
print(data)