from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log",filemode='a' , format='%(asctime)s,%(name)s:%(levelname)s:%(message)s')
# logger=logging.getLogger(__name__)


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)


def get_user(username):
    conn = sqlite3.connect('empdatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# def get_emp_name(name):
#     conn = sqlite3.connect('empdatabase.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM emp WHERE name = ?', (name,))
#     employee = cursor.fetchone()
#     conn.close()
#     return employee


# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    existing_user = get_user(username)
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    conn = sqlite3.connect('empdatabase.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User registered successfully'}), 201


# Route for user login and token generation
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = get_user(username)

    if user and user[2] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/employee', methods=['GET'])
def get():
    try:
        conn = sqlite3.connect('empdatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emp')
        data = cursor.fetchall()
        conn.close()
        app.logger.info("Data fetched sucessfully from the database")
        result = [{'id': row[0], 'name': row[1], 'address':row[2], 'city':row[3], 'salary':row[4] } for row in data]
        return jsonify(result)
    except Exception as obj:
        logging.error("Exception Information",exc_info=True)

@app.route('/employee', methods=['POST'])
@jwt_required()
def posts():
    app.logger.info("User requested a POST request")
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    city= data.get('city')
    salary=data.get('salary')
    if not name or not address or not city or not salary:
        return jsonify({'error': 'name address city and salary are required'}), 400
    try:
        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO emp (name, addr, city, salary) VALUES (?, ?, ?, ?)', (name, address, city, salary))
        connection.commit()
        connection.close()
        app.logger.info("Data put sucessfully into the database")
        return jsonify({'message': 'Employee created successfully, '+ name}), 201
    
    except Exception as obj:
        logging.error("Exception Information",exc_info=True)

@app.route('/employee/<int:emp_id>',methods=['PUT'])
@jwt_required()
def putdata(emp_id):
    app.logger.info(f"User requested a PUT request for employee-id:{emp_id} ")
    current_user = get_jwt_identity()
    # employee=get_emp_name(emp_id)
    
    # if (current_user==employee):

    data = request.get_json()

    name = data.get('name')
    address = data.get('address')
    city= data.get('city')
    salary=data.get('salary')

    if not name or not address or not city or not salary:
        return jsonify({'error': 'name address city and salary are required'}), 400

    try:
        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
        existing_emp = cursor.fetchone()

        if existing_emp is None:
            app.logger.info("Data is not present in the database")
            return jsonify({'error': 'Employee not found'}), 404

   
        new_name = data.get('name', existing_emp[1])
        new_address = data.get('address', existing_emp[2])
        new_city=data.get('city',existing_emp[3])
        new_salary=data.get('salary',existing_emp[3])

        cursor.execute('UPDATE emp SET name = ?, addr = ?, city=?, salary=? WHERE id = ?', (new_name, new_address, new_city,new_salary, emp_id))
        connection.commit()
        connection.close()
        app.logger.info("Data updated sucessfully into the database")
        return jsonify({'message': 'Employee updated successfully '+ name}), 200

    except Exception as obj:
            logging.error("Exception Information",exc_info=True)


@app.route('/del_employee/<int:emp_id>', methods=['DELETE'])
@jwt_required()
def delete_emp_route(emp_id):
    app.logger.info(f"User requested a DELETE request for employee-id:{emp_id}")
    try:
        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
        data = cursor.fetchone()

        if data:
            cursor.execute('DELETE FROM emp WHERE id = ?', (emp_id,))
            connection.commit()
            connection.close()
            app.logger.info("Data deleted sucessfully from the database")
            return jsonify({'message': 'Employee deleted successfully'})
        else:
            connection.close()
            app.logger.info("Data is not present in the database")
            return jsonify({'message': 'Improper ID'}), 404
    
    except Exception as obj:
            logging.error("Exception Information",exc_info=True)

@app.route('/employee/<int:emp_id>',methods=['GET'])
@jwt_required()
def get_spec_emp(emp_id):
    app.logger.info(f"User requested a GET request for employee-id:{emp_id} ")
    try:
        conn = sqlite3.connect('empdatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
        data = cursor.fetchall()
        conn.close()

        result = [{'id': row[0], 'name': row[1], 'address':row[2], 'city':row[3], 'salary':row[4] } for row in data]

        if not result:
            app.logger.info("Employee not found in the database")
            return jsonify({'error': 'Employee not found'}), 404

        app.logger.info("Data fetched sucessfully from the database")
        return jsonify(result)
    
    except Exception as obj:
            logging.error("Exception Information",exc_info=True)


if __name__ == '__main__':
    app.run(debug=True)

