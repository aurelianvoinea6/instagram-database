import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
  
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    posts = relationship('Post')

class Image(Base):
    __tablename__ = 'image'
 
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String(250), nullable=False)
    size = Column(String(250), nullable=False)
    person = relationship('Post', back_populates='image')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    date = Column(String(250), nullable=False)
    likes = Column(String(250), nullable=True)
    image = relationship('Image', uselist=False, back_populates='post')

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship('Person')

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')