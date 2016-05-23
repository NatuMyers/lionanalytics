import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class DeceptronItem(Base):
    __tablename__ = 'DeceptronItem'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        # returns object data in easily serlizeable format
        return {
            'name': self.name,
            'textRaw': self.name,
            'textDigest': self.name,
            'id': self.id
            }

engine = create_engine('sqlite:///deceptron.db')

Base.metadata.create_all(engine)
