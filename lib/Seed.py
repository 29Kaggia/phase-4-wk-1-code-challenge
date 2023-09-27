from models import db, Restaurant, Pizza, RestaurantPizza


# Create sample restaurants
restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')

# Create sample pizzas
pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

# Add pizzas to restaurants
restaurant1.pizzas.append(pizza1)
restaurant1.pizzas.append(pizza2)
restaurant2.pizzas.append(pizza1)

# Commit the changes to the database
db.session.add(restaurant1)
db.session.add(restaurant2)
db.session.commit()

print('Seed data has been added to the database.')


