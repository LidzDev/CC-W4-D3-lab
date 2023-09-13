from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/records_app" 
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lydia@localhost:5432/records_app" 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.staff import Staff 
from models.record import Record
from controllers.record_controller import records_blueprint

app.register_blueprint(records_blueprint)

@app.route("/")
def home():
  return "This is the home page!"