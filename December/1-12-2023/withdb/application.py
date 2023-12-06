from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

class Drink(db.Model):  #Used db.model for sql alchemy
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True, nullable=False)
    description=db.Column(db.String(120))     #It is a column with 120 characters

    def __repr__(self):
        return f"{self.name}-{self.description}"

with app.app_context():
    db.create_all()
    drink=Drink(name="Mango juice",description="Tastes like fresh mangoes")
    db.session.add(drink)
    db.session.commit()

    drinks = db.session.execute(db.select(Drink)).scalars()

@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/drinks')
def get_drinks():
    
    return {"drinks":"drink data"}

if __name__=="__main__":
    app.run(debug=True)