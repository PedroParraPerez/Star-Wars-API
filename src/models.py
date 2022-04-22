import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()







class Member(Base):
    __tablename__ = 'Member'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    def to_dict(self):
        return {}


        
class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Description = Column(String(250))
    
    Hair_color = Column(String(250))
    Skin_color = Column(String(250))
    Eye_color = Column(String(250))
    Birth_year = Column(String(250))
    Gender = Column(String(250))
    Height = Column(Integer())
    Mass = Column(Integer())
    

    # Relationship Planet
    planet_id = Column(Integer, ForeignKey('planet.id'))


    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Description = Column(String(250))
    Gravity = Column(String(250))
    Climate = Column(String(250))
    Terrain = Column(String(250))
    Diameter = Column(Integer())
    Surface_water = Column(Integer())
    Rotation_period = Column(Integer())
    Population = Column(Integer())
    Orbital_period = Column(Integer())
   
    Characters = relationship('Character')

    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')