from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# import psycopg2       #Psycopg 2.
# from psycopg2.extras import RealDictCursor
# import psycopg
# from psycopg.rows import dict_row       # Psycopg 3.
# import time

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency. Every time a request is recieved a session is created an then closed.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# This is just for dicumentation and see how to retrieve data with psycopg.
# while True:
#     try:
#         conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='nicopostgres', 
#                             row_factory=dict_row)  # Map the columns and values
#         # conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='nicopostgres', 
#         #                        cursor_factory=RealDictCursor)  # Map the columns and values
#         cursor = conn.cursor()
#         print('Database connection was succesfull!')
#         break
#     except Exception as e:
#         print(f'Connecting to database failed. Error: {e}')
#         time.sleep(2)