from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///example.db",isolation_level='AUTOCOMMIT')
session = sessionmaker(bind=engine)
Base = declarative_base()