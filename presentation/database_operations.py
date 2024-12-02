import os
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the path to the input file
file_path = r"C:\Users\jakub\PycharmProjects\data\macro\pl\cpiypl.m.txt"

# SQLAlchemy setup
Base = declarative_base()


# Define a model
class CPIYPL(Base):
    __tablename__ = 'cpiypl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)


# Create an SQLite database using SQLAlchemy
DATABASE_URL = "sqlite:///../database/data.sqlite3"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# Function to read data from the file
def load_data_from_file(path):
    # Ensure the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")

    # Read the data from the file (assuming it's whitespace delimited)
    data = pd.read_csv(file_path, sep=',',
                       header='infer',
                       usecols=['<DATE>', '<CLOSE>'],
                       parse_dates=['<DATE>'])
    return data
# Load data into DataFrame

data_frame = load_data_from_file(file_path)

# Insert data into the database
for index, row in data_frame.iterrows():
    record = CPIYPL(date=row['<DATE>'], value=row['<CLOSE>'])
    session.add(record)

# Commit the transaction
session.commit()

# # Close the session
session.close()
