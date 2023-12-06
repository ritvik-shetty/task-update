from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data1.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db = SQLAlchemy(app)

class Drink(db.Model):  #Used db.model for sql alchemy
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True, nullable=False)
    description=db.Column(db.String(120))     #It is a column with 120 characters

    def __repr__(self):
        return f"{self.name}-{self.description}"
    
