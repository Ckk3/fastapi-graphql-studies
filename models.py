from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy.ext.declarative import declarative_base
import env

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = env.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, )

# First Model
class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

