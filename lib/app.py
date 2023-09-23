from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzeria.db'
db = SQLAlchemy(app)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='pizza_restaurants')

# Wrap the creation of database tables inside an application context
with app.app_context():
    db.create_all()


# Create the Flask application
app = Flask(__name__)

restaurants_data = [
    {
        "id": 1,
        "name": "Dominion Pizza",
        "address": "Good Italian, Ngong Road, 5th Avenue"
    },
    {
        "id": 2,
        "name": "Pizza Hut",
        "address": "Westgate Mall, Mwanzi Road, Nrb 100"
    }
]

pizzas_data = [
    {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
]

# Route: GET /restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    # Replace this with your actual data retrieval from the database
    return jsonify(restaurants_data)

# Route: GET /restaurants/:id
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    # Replace this with your actual data retrieval from the database
    restaurant = next((r for r in restaurants_data if r['id'] == id), None)
    if restaurant:
        # Sample data for restaurant pizzas (you can replace this with your database queries)
        restaurant['pizzas'] = pizzas_data
        return jsonify(restaurant)
    else:
        return jsonify({"error": "Restaurant not found"}), 404

# Route: DELETE /restaurants/:id
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    # Implement restaurant deletion logic here
    # Return an empty response body and the appropriate HTTP status code
    return '', 204  # Successful deletion

# Route: GET /pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    # Replace this with your actual data retrieval from the database
    return jsonify(pizzas_data)

# Route: POST /restaurant_pizzas
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    # Implement restaurant pizza creation logic here
    # Return the appropriate response based on success or validation errors
    return jsonify({"id": 1, "name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"}), 201

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
