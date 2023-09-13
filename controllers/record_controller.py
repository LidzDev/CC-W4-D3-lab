from flask import Blueprint, render_template, request, redirect
from models.record import Record
from models.staff import Staff
from app import db

records_blueprint = Blueprint("records", __name__)

@records_blueprint.route("/records")
def list_records():
    records = Record.query.all()
    return render_template("index.jinja", title="Vintage Records", records=records)

@records_blueprint.route("/records/<int:id>")
def show_one_record(id):
    record_to_show = Record.query.get(id)
    return render_template("show_one_record.jinja", title=f"Vintage {record_to_show.record_name}", record=record_to_show)


@records_blueprint.route("/records/add")
def show_add_page():
    return render_template("add_record.jinja", title="Add a record to Vintage Records stock")

@records_blueprint.route("/records", methods=["POST"])
def save_record():
    record_name = request.form["record_name"]
    artist_name = request.form["artist_name"]
    price = request.form["price"]
    record_to_be_saved = Record(record_name=record_name, artist_name=artist_name, price=price, staff_associated_id=1)
    db.session.add(record_to_be_saved)
    db.session.commit()
    return redirect("/records")

@records_blueprint.route("/records/<int:id>", methods=["POST"])
def update_record(id):
    redirect_string = "/records/" + str(id)
    return redirect(redirect_string)