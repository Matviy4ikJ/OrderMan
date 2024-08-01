from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app import app

engine = create_engine(app.config['DB_NAME'], echo=True)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    ...


def create_db():
    Base.metadata.create_all(engine)


def del_db():
    Base.metadata.drop_all(engine)
