import json

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from services.app import get_completed_data_from_gsheets as get_data
from services.sql_functions import manipulate_with_data_from_sheet_and_db as manipulate_data
from data.constants import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Deliveries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_id = db.Column(db.Integer)
    order_num = db.Column(db.String(50))
    date = db.Column(db.String(10))
    usd_price = db.Column(db.Float)
    rub_price = db.Column(db.Float)

    def __int__(self, d_id, order_num, date, usd_rate, rub_price):
        self.d_id = d_id
        self.order_num = order_num
        self.date = date
        self.usd_price = usd_rate
        self.rub_price = rub_price


class DeliverySchema(ma.Schema):
    class Meta:
        fields = ('id', 'd_id', 'order_num', 'date', 'usd_price', 'rub_price')


delivery_schema = DeliverySchema()
deliveries_schema = DeliverySchema(many=True)


@app.route("/api/get-statistics")
def get_statistics():

    with open('test.json', encoding='utf-8') as file:
        google_sheets_data = json.load(file)

    manipulate_data(
        session=db.session,
        model=Deliveries,
        schema=deliveries_schema,
        query=Deliveries.query.all(),
        data=google_sheets_data
    )
    delivery_data = Deliveries.query.all()
    result = deliveries_schema.dump(delivery_data)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
