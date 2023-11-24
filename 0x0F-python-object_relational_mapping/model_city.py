#!/usr/bin/python3
'''
    This script defines a City class to work with
    MySQLAlchemy ORM.
'''

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''
        Defines the City class inherits from Base
    '''
    __tablename__ = 'cities'

    id = Column(
                Integer,
                primary_key=True)
    name = Column(
                  String(128),
                  nullable=False)
    state_id = Column(
                      Integer,
                      ForeignKey('states.id'),
                      nullable=False)
