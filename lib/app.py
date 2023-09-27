from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzeria.db'
db = SQLAlchemy(app)
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
  
    return jsonify(restaurants_data)

# Route: GET /restaurants/:id
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):

    restaurant = next((r for r in restaurants_data if r['id'] == id), None)
    if restaurant:
       
        restaurant['pizzas'] = pizzas_data
        return jsonify(restaurant)
    else:
        return jsonify({"error": "Restaurant not found"}), 404


# Route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    return '', 204


# Route: GET /pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():

    return jsonify(pizzas_data)

# Route: POST /restaurant_pizzas
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
   
    return jsonify({"id": 1, "name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"}), 201

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
