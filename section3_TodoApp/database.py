from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib
import pyodbc

"""

# sqlite3
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})
"""

"""
# Postgres
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:test1234@localhost/TodoApplicationDatabase'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
"""

"""
# mysql
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:!Test1234!@localhost:3306/TodoApplicationDatabase'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
"""


# Azure SQL DB
params = urllib.parse.quote_plus\
    (r'Driver={ODBC Driver 18 for SQL Server};Server=tcp:jaketest001.database.windows.net,1433;Database=TestDB;Uid=xxxx;Pwd=xxxxx!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
SQLALCHEMY_DATABASE_URL = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

