from flask import Flask, request, jsonify
import sqlite3
import logging

app = Flask(__name__)


@app.route('/employee', methods=['GET','POST'])
def posts():

    if request.method == 'GET':
      
        conn = sqlite3.connect('empdatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emp')
        data = cursor.fetchall()
        conn.close()
 
        result = [{'id': row[0], 'name': row[1], 'address':row[2], 'city':row[3], 'salary':row[4] } for row in data]
        return jsonify(result)

    elif request.method == 'POST':
        data = request.get_json()

        name = data.get('name')
        address = data.get('address')
        city= data.get('city')
        salary=data.get('salary')

        if not name or not address or not city or not salary:
            return jsonify({'error': 'name address city and salary are required'}), 400

        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO emp (name, addr, city, salary) VALUES (?, ?, ?, ?)', (name, address, city, salary))

        connection.commit()
        connection.close()

        return jsonify({'message': 'Employee created successfully, '+ name}), 201


@app.route('/employee/<int:emp_id>',methods=['PUT'])
def postdata(emp_id):
    data = request.get_json()

    name = data.get('name')
    address = data.get('address')
    city= data.get('city')
    salary=data.get('salary')

    if not name or not address or not city or not salary:
        return jsonify({'error': 'name address city and salary are required'}), 400

    connection = sqlite3.connect('empdatabase.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
    existing_emp = cursor.fetchone()

    if existing_emp is None:
        return jsonify({'error': 'Employee not found'}), 404

   
    new_name = data.get('name', existing_emp[1])
    new_address = data.get('address', existing_emp[2])
    new_city=data.get('city',existing_emp[3])
    new_salary=data.get('salary',existing_emp[3])
    
    cursor.execute('UPDATE emp SET name = ?, addr = ?, city=?, salary=? WHERE id = ?', (new_name, new_address, new_city,new_salary, emp_id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Employee updated successfully '+ name}), 200



@app.route('/del_employee/<int:emp_id>', methods=['DELETE'])
def delete_emp_route(emp_id):
    connection = sqlite3.connect('empdatabase.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
    data = cursor.fetchone()

    if data:
        cursor.execute('DELETE FROM emp WHERE id = ?', (emp_id,))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Employee deleted successfully'})
    else:
        connection.close()
        return jsonify({'message': 'Improper ID'}), 404
    


@app.route('/employee/<int:emp_id>',methods=['GET'])
def get_spec_emp(emp_id):
    conn = sqlite3.connect('empdatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
    data = cursor.fetchall()
    conn.close()
    
    
    result = [{'id': row[0], 'name': row[1], 'address':row[2], 'city':row[3], 'salary':row[4] } for row in data]

    if not result:
        return jsonify({'error': 'Employee not found'}), 404
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

