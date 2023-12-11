from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def delete_item(item_id):
    connection = sqlite3.connect('empdatabase.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM emp WHERE id = ?', (item_id,))
    connection.commit()
    connection.close()


@app.route('/posts', methods=['GET','POST'])
def posts():

    if request.method == 'GET':
        # Fetch all posts from the database'
        conn = sqlite3.connect('empdatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emp')
        data = cursor.fetchall()
        conn.close()
        # return jsonify(data)
        # Convert the data to a list of dictionaries
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

        return jsonify({'message': 'Post created successfully, '+ name}), 201


@app.route('/posts/<int:item_id>',methods=['PUT'])
def postdata(item_id):
    data = request.get_json()

    name = data.get('name')
    address = data.get('address')
    city= data.get('city')
    salary=data.get('salary')

    if not name or not address or not city or not salary:
        return jsonify({'error': 'name address city and salary are required'}), 400

    connection = sqlite3.connect('empdatabase.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM emp WHERE id = ?', (item_id,))
    existing_emp = cursor.fetchone()

    if existing_emp is None:
        return jsonify({'error': 'Employee not found'}), 404

    # Update user data
    new_name = data.get('name', existing_emp[1])
    new_address = data.get('address', existing_emp[2])
    new_city=data.get('city',existing_emp[3])
    new_salary=data.get('salary',existing_emp[3])
    # Use cursor.execute to perform the UPDATE query
    cursor.execute('UPDATE emp SET name = ?, addr = ?, city=?, salary=? WHERE id = ?', (new_name, new_address, new_city,new_salary, item_id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Employee updated successfully '+ name}), 200



@app.route('/del_posts/<int:item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    delete_item(item_id)
    return jsonify({'message': 'Item deleted successfully'})




if __name__ == '__main__':
    app.run(debug=True)

