#!/usr/bin/python3
"""
This module has one class:
State - inherited from Base.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    class is linked to the states table
    Attributes:
        id: Integer, primary key
        name: String
    """
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
