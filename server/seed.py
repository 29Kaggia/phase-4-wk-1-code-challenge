from model import db, Restaurant, Pizza, RestaurantPizza
from app import app
def sample_data():
     with app.app_context():
        Pizza.query.delete()
        Restaurant.query.delete()
        db.create_all()


        # Create sample restaurants
        restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
        restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')

        # Create sample pizzas
        pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
        pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

        # Commit the changes to the database
        db.session.add(restaurant1)
        db.session.commit()
        db.session.add(restaurant2)
        db.session.commit()

        db.session.add(pizza1)
        db.session.commit()
        db.session.add(pizza2)
        db.session.commit()

        print('Seed data has been added to the database.')

if __name__ == '__main__':
    sample_data()

