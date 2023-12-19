from flask import Flask,jsonify,request,make_response
import jwt
import datetime
from functools import wraps



app = Flask(__name__)

app.config['SECRET_KEY']='thisisthesecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=request.args.get('token')  #http://127.0.0.1:5000/route?token=dawaa3etgg334343dfsfs

        if not token:
            return jsonify({'message':'Token not present'}) ,403    

        
        try:
            data=jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'Token is invalid'}),403

        return f(*args, **kwargs)
    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message':'Anyone can view'})


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message':'Can only be viewed by people with valid tokenss'})

@app.route('/login')   
def login():
    auth=request.authorization

    if auth and auth.password == 'password':
            token = jwt.encode({'user': auth.username, 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=15)},app.config['SECRET_KEY'])

            return jsonify({'token':token})
    return make_response('Could not verify!',401, {'WWW-Authenticate':'Basic realm ="Login Required"'})


if __name__ == '__main__':
    app.run(debug=True)