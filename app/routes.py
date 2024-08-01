from sqlalchemy import select

from db import Session
from app import app
from flask import Flask, render_template
from app.Models import Pizza


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu/')
def menu():
    with Session() as session:

        if session.query(Pizza).count() == 0:
            pizzas = [
                {"name": "Маргарита", "ingredients": "Томатний соус, Моцарела, Базилік", "price": "120 грн"},
                {"name": "Пепероні", "ingredients": "Томатний соус, Моцарела, Пепероні", "price": "150 грн"},
                {"name": "Чотири сири", "ingredients": "Моцарела, Горгонзола, Пармезан, Фета", "price": "180 грн"},
                {"name": "Гавайська", "ingredients": "Томатний соус, Моцарела, Шинка, Ананас", "price": "160 грн"},
                {"name": "Вегетаріанська", "ingredients": "Томатний соус, Моцарела, Овочі", "price": "140 грн"}
            ]

            for pizza in pizzas:
                new_pizza = Pizza(name=pizza['name'], ingredients=pizza['ingredients'], price=pizza['price'])
                session.add(new_pizza)
            session.commit()

        pizza2 = session.execute(select(Pizza)).scalars().all()

    return render_template('menu.html', pizza2=pizza2)


@app.errorhandler(404)
def er404(e):
    return render_template('errors/error404.html'), 404


@app.errorhandler(500)
def er500(e):
    return render_template('errors/error500.html'), 500

