import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)


class People(Base):
    __tablename__ = 'People'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    bith_year = Column(Integer, nullable=False)
    gender = Column(String(250))
    homeworld_planet = Column(Integer, ForeignKey(Planet.id))
    planet = relationship(Planet)

class Vehicle(Base):
    __tablename__ = "Vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(Integer)
    pilots_id = Column(Integer, ForeignKey(People.id))
    pilots = relationship(People)

class Pilots(Base):
    __tablename__ = "Pilots"
    id = Column(Integer, primary_key=True)
    id_people = Column(Integer, ForeignKey(People.id))
    people = relationship(People)
    id_vehicle = Column(Integer, ForeignKey(Vehicle.id))
    vehicle = relationship(Vehicle)
    

class User(Base):
    __tablename__ = 'User'
    # Definimos las columnas de la tabla Planet
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(Integer, nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Fav(Base):
    __tablename__ = 'Fav'
    
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey(User.id))
    user = relationship(User)
    id_planet = Column(Integer, ForeignKey(Planet.id))
    planet = relationship(Planet)
    id_people = Column(Integer, ForeignKey(People.id))
    people = relationship(People)
    id_vehicle = Column(Integer, ForeignKey(Vehicle.id))
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
