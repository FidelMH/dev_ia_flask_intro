from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

# Set up the database engine
engine = create_engine("sqlite+pysqlite:///database.db", echo=True)  
Base = declarative_base()  # define a base class for all models

class Blog(Base):
    __tablename__ = "blogs"  # table name in the database

    id = Column(Integer)  # primary key column
    title = Column(String, nullable=False)  # username column
    body = Column(String)  # age column

# Create all tables defined by models
Base.metadata.create_all(engine)