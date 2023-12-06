"""
Python Flask REST API with MySQL CRUD
 
This program provides a basic structure for a Flask REST API with MySQL CRUD operations.
 
"""
 
from flask import Flask, request, jsonify
import mysql.connector
import logging
 
# Setting up logging to monitor performance and errors
logging.basicConfig(level=logging.INFO)
 
# MySQL database configuration
DB_HOST = 'localhost'
DB_USER = 'username'
DB_PASSWORD = 'password'
DB_NAME = 'database_name'
 
# Initialize Flask app
app = Flask(__name__)
 
# Initialize MySQL connection
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
 
# Create a cursor object to interact with the database
cursor = db.cursor()
 
 
@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Get all data from the database.
 
    Returns:
    list: List of data records.
 
    Example Usage:
    GET /api/data
    """
    try:
        logging.info("Fetching data from the database...")
        # Execute SQL query to fetch all data
        cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to fetch data from the database.'})
 
 
@app.route('/api/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    """
    Get data by ID from the database.
 
    Args:
    id (int): ID of the data record.
 
    Returns:
    dict: Data record.
 
    Example Usage:
    GET /api/data/1
    """
    try:
        logging.info(f"Fetching data with ID {id} from the database...")
        # Execute SQL query to fetch data by ID
        cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
        data = cursor.fetchone()
        if data:
            return jsonify(data)
        else:
            return jsonify({'error': 'Data not found.'})
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to fetch data from the database.'})
 
 
@app.route('/api/data', methods=['POST'])
def create_data():
    """
    Create a new data record in the database.
 
    Request Body:
    {
        "name": "John Doe",
        "age": 30
    }
 
    Returns:
    dict: Created data record.
 
    Example Usage:
    POST /api/data
    {
        "name": "John Doe",
        "age": 30
    }
    """
    try:
        logging.info("Creating a new data record...")
        # Get data from request body
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
 
        # Execute SQL query to insert data
        cursor.execute("INSERT INTO data (name, age) VALUES (%s, %s)", (name, age))
        db.commit()
 
        # Get the ID of the inserted record
        id = cursor.lastrowid
 
        # Fetch the inserted record from the database
        cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
        created_data = cursor.fetchone()
 
        return jsonify(created_data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to create data record.'})
 
 
@app.route('/api/data/<int:id>', methods=['PUT'])
def update_data(id):
    """
    Update an existing data record in the database.
 
    Args:
    id (int): ID of the data record to update.
 
    Request Body:
    {
        "name": "John Doe",
        "age": 35
    }
 
    Returns:
    dict: Updated data record.
 
    Example Usage:
    PUT /api/data/1
    {
        "name": "John Doe",
        "age": 35
    }
    """
    try:
        logging.info(f"Updating data with ID {id}...")
        # Get data from request body
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
 
        # Execute SQL query to update data
        cursor.execute("UPDATE data SET name = %s, age = %s WHERE id = %s", (name, age, id))
        db.commit()
 
        # Fetch the updated record from the database
        cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
        updated_data = cursor.fetchone()
 
        if updated_data:
            return jsonify(updated_data)
        else:
            return jsonify({'error': 'Data not found.'})
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to update data record.'})
 
 
@app.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    """
    Delete a data record from the database.
 
    Args:
    id (int): ID of the data record to delete.
 
    Returns:
    dict: Success message.
 
    Example Usage:
    DELETE /api/data/1
    """
    try:
        logging.info(f"Deleting data with ID {id}...")
        # Execute SQL query to delete data
        cursor.execute("DELETE FROM data WHERE id = %s", (id,))
        db.commit()
 
        return jsonify({'message': 'Data deleted successfully.'})
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to delete data record.'})
 
 
if __name__ == "__main__":
    app.run()
