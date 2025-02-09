import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    terrain = Column(String(250), nullable=False)
   

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    usuario = relationship("Usuario")
    character = relationship("Character")


class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    usuario = relationship("Usuario")
    planet = relationship("Planet")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
