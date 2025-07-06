# Inventory CRUD API
A simple inventory management system built with Flask and SQLAlchemy.
## Features
- Create, read, update and delete (CRUD) inventory items
- JSON-based REST API
- SQLAlchemy for ORM
- Modular Flask app structure
## Technologies Used
- Python 3.12
- Flask
- SQLAlchemy
- Flask-Migrate (optional)
- SQLite or other RDBMS
## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Fullestcommerce/CRUIDapi-1
   cd inventory-api
2. Install dependencies:
    pip install -r requirements.txt
3. Run:
    flask run
## API
    | Method | Endpoint      | Description       |
    | ------ | ------------- | ----------------- |
    | GET    | `/items`      | Get all items     |
    | GET    | `/items/<id>` | Get a single item |
    | POST   | `/items`      | Create a new item |
    | PUT    | `/items/<id>` | Update an item    |
    | DELETE | `/items/<id>` | Delete an item    |
## Example requests
    POST /items
    Content-Type: application/json
    {
        "name": "Router",
        "description": "Cisco X1000",
        "quantity": 10,
        "location": "Storage"
    }
## License 
    This project is for educational purposes and can be reused freely.
    credits - FULLESTCOMMERCE
