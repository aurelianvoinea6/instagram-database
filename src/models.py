import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
  
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.userName,
            "email": self.email,
        }

class Follower(Base):
    __tablename__ = 'follower'
 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_from_id = Column(Integer, ForeignKey('user.id'))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_from_id": self.user_from_id,
        }
    

class Comments(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_text = Column(String(250), nullable=True)
   
    def serialize(self):
       return {
           "id": self.id,
           "author_id": self.user_id,
           "post_id": self.post_id,
           "comment_text": self.text,
       }

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String(250), nullable=False)
    type_media = Column(Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "url": self.url,
            "type_media": self.type_media,
        }



render_er(Base, 'diagram.png')