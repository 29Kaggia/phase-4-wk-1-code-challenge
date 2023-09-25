# phase-4-wk-1-code-challenge
# Flask Code Challenge - Pizza Restaurants
#author: Lewis Kaggia

This Flask project implements a RESTful API for managing pizza restaurants and their menus. The API allows users to interact with restaurants, pizzas, and their relationships.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Routes](#api-routes)
- [Contributing](#contributing)
- [License](#license)

## Description

In this project, we've built a Flask-based API for a Pizza Restaurant domain. The main functionalities of this API include managing restaurants, pizzas, and their relationships. Users can perform operations such as retrieving restaurant details, deleting restaurants along with their associated menu items, listing pizzas, and creating new menu items (RestaurantPizza).

## Features

- **Restaurant Management:** Create, read, and delete restaurants.
- **Pizza Management:** List available pizzas.
- **Menu Management:** Add menu items (RestaurantPizza) to restaurants.
- **Data Validation:** Implement data validations, including price range and name length restrictions.

## Getting Started

Follow the instructions below to set up and run this Flask project locally.

### Prerequisites

Make sure you have the following prerequisites installed on your system:

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/pizza-restaurants-api.git
   ```

2. Change to the project directory:

   ```bash
   cd pizza-restaurants-api
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows (Command Prompt):

     ```bash
     venv\Scripts\activate
     ```

   - On Windows (PowerShell):

     ```bash
     .\venv\Scripts\Activate.ps1
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once the project is set up, you can run the Flask application and use the API as follows:

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Access the API using a tool like [Postman](https://www.postman.com/) or your preferred method for making HTTP requests.

## API Routes

The following routes are available in the API:

- `GET /restaurants`: Retrieve a list of all restaurants.
- `GET /restaurants/:id`: Retrieve details of a specific restaurant by ID.
- `DELETE /restaurants/:id`: Delete a restaurant by ID, along with its associated menu items.
- `GET /pizzas`: List available pizzas.
- `POST /restaurant_pizzas`: Create a new menu item (RestaurantPizza) associated with a restaurant.

Detailed API documentation and usage examples can be found in the project's source code.

## Contributing

We welcome contributions to this project. If you'd like to contribute, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file to include any additional information or details specific to your project. A well-documented README helps users and contributors understand your project and how to use it effectively.