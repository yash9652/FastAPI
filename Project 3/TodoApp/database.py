from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:yashRGUKT9652@localhost/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:yashRGUKT9652@127.0.0.6:3306/todoapplicationdatabase'

#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
#engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
