#!/usr/bin/python3
"""
This module has one class:
City - inherited from Base.
"""


from model_state import State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    This class is linked to the cities table.
    Attributes:
        id: Integer, required, primary key
        name: String, required
        state_id: Integer, Foreign Key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey(State.id))
