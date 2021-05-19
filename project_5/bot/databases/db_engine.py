from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///databases/database.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

'''СПИСОК ВСЕХ ЮЗЕРОВ'''
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_id = Column(Integer)
    status = Column(String)
    count = Column(Integer, default=0)
    message_id = Column(String)
    message_id_2 = Column(String)
    question_1 = Column(Integer) # question_1
    question_2 = Column(Integer) # question_2
    question_3 = Column(Integer) # question_3
    question_4 = Column(Integer) # question_4
    question_5 = Column(String) # question_5
    question_6 = Column(String) # question_6
    question_7 = Column(String) # question_7
    question_8 = Column(String) # question_8
    question_9 = Column(String) # question_9
    question_10 = Column(String) # question_10
    question_11 = Column(String) # question_11
    question_12 = Column(String) # question_12
    question_13 = Column(String) # question_13
    question_14 = Column(String) # question_14
    question_15 = Column(String) # question_15
    question_16 = Column(String) # question_16
    question_17 = Column(String) # question_17
    question_18 = Column(String) # question_18
    question_19 = Column(String) # question_19
    question_20 = Column(String) # question_20
    question_21 = Column(String) # question_21
    question_22 = Column(String) # question_22
    interview = relationship('Interview', backref='users')

'''РЕЗУЛЬТАТЫ ВСЕХ ОПРОСОВ'''
class Interview(Base):
    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True)
    db_id = Column(Integer, ForeignKey('users.id'))
    # username = Column(String, ForeignKey('users.username'))
    # user_id = Column(String, ForeignKey('users.user_id'))
    # db_id = Column(Integer)
    # username = Column(String)
    # user_id = Column(Integer)
    question_1 = Column(Integer)
    question_2 = Column(Integer)
    question_3 = Column(Integer)
    question_4 = Column(Integer)
    question_5 = Column(String)
    question_6 = Column(String)
    question_7 = Column(String)
    question_8 = Column(String)
    question_9 = Column(String)
    question_10 = Column(String)
    question_11 = Column(String)
    question_12 = Column(String)
    question_13 = Column(String)
    question_14 = Column(String)
    question_15 = Column(String)
    question_16 = Column(String)
    question_17 = Column(String)
    question_18 = Column(String)
    question_19 = Column(String)
    question_20 = Column(String)
    question_21 = Column(String)
    question_22 = Column(String)
    # user = relationship('User', back_populates = 'interviews')

metadata = Base.metadata
metadata.create_all(engine)