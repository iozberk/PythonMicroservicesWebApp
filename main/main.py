from dataclasses import dataclass
from flask import Flask
from flask_migrate import Migrate
import flask_sqlalchemy

from sqlalchemy import UniqueConstraint


app_flask_app = Flask(__name__)

app_flask_app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db_mysql/main'

db_mysql = flask_sqlalchemy.SQLAlchemy(app_flask_app)

migrate = Migrate(app_flask_app, db_mysql)

@dataclass
class Product(db_mysql.Model):
    id: int
    title: str
    image: str

    id = db_mysql.Column(db_mysql.Integer, primary_key=True, autoincrement=False)
    title = db_mysql.Column(db_mysql.String(200))
    image = db_mysql.Column(db_mysql.String(200))


@dataclass
class ProductUser(db_mysql.Model):
    id = db_mysql.Column(db_mysql.Integer, primary_key=True)
    user_id = db_mysql.Column(db_mysql.Integer)
    product_id = db_mysql.Column(db_mysql.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')



@app_flask_app.route("/")
def hello():
  return "Hello World!!!"

if __name__ == "__main__":
    app_flask_app.run(debug=True, host='0.0.0.0')   