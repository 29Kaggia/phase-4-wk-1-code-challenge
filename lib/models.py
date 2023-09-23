from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')


    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters.")
        return name

class RestaurantPizza(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      price = db.Column(db.Float, nullable=False)
      restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
      pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
      restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
      pizza = db.relationship('Pizza', back_populates='pizza_restaurants')

      @validates('price')
      def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30.")
        return price
