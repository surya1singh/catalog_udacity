from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique = True)
    password = Column(String(250), nullable=True)
    gconnect = Column(Integer, nullable=True)


engine = create_engine('sqlite:///users.db')


Base.metadata.create_all(engine)
