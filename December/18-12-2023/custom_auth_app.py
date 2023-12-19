from flask import Flask, request

app = Flask(__name__)

# Dummy tokens for demonstration purposes
tokens = {'user1': 'token1', 'user2': 'token2'}

@app.route('/protected', methods=['GET'])
def protected_resource():
    token = request.headers.get('Authorization')

    if token and token in tokens.values():
        # Authorized access
        return {'message': 'Access granted'}
    else:
        return {'message': 'Unauthorized'}, 401

if __name__ == '__main__':
    app.run(debug=True)
