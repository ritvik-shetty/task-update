from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log",filemode='a' , format='%(asctime)s,%(name)s:%(levelname)s:%(message)s')
# logger=logging.getLogger(__name__)


app = Flask(__name__)


SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Employee API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/getemployee', methods=['GET'])
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

@app.route('/postemployee', methods=['POST'])
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

@app.route('/putemployee/<int:emp_id>',methods=['PUT'])
def postdata(emp_id):
    app.logger.info(f"User requested a PUT request for employee-id:{emp_id} ")
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


@app.route('/employee/<int:emp_id>', methods=['DELETE'])
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

