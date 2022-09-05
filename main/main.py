from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@admin'
CORS(app)

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200), unique=True, nullable=False)
    image = db.Column(db.String(200), unique=True, nullable=False)

class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)    