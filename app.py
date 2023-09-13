from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lydia@localhost:5432/records_app" 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.staff import Staff 
from models.record import Record

@app.route("/")
def home():
  return "This is the home page!"