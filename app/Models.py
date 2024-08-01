from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Pizza(Base):
    __tablename__ = 'Pizzas'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    ingredients: Mapped[str] = mapped_column(String(200))
    price: Mapped[int]


class Users(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    password: Mapped[str] = mapped_column(String(50))
    is_admin: Mapped[bool] = mapped_column(default=False)

