from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def delete_item(item_id):
    connection = sqlite3.connect('data2.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (item_id,))
    connection.commit()
    connection.close()


@app.route('/posts', methods=['GET','POST'])
def posts():

    if request.method == 'GET':
        # Fetch all posts from the database'
        conn = sqlite3.connect('data2.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        data = cursor.fetchall()
        conn.close()
        # return jsonify(data)
        # Convert the data to a list of dictionaries
        result = [{'id': row[0], 'name': row[1], 'address':row[2], 'city':row[3], 'pin':row[4] } for row in data]
        return jsonify(result)

    elif request.method == 'POST':
        data = request.get_json()

        name = data.get('name')
        address = data.get('address')
        city= data.get('city')
        pin=data.get('pin')

        if not name or not address or not city or not pin:
            return jsonify({'error': 'name address city and pin are required'}), 400

        connection = sqlite3.connect('data2.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)', (name, address, city, pin))

        connection.commit()
        connection.close()

        return jsonify({'message': 'Post created successfully, '+ name}), 201


@app.route('/del_posts/<int:item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    delete_item(item_id)
    return jsonify({'message': 'Item deleted successfully'})




if __name__ == '__main__':
    app.run(debug=True)

