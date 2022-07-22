import logging
import os
import time

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_cors import CORS, cross_origin

from services.main import get_completed_data_from_gsheets as get_data
from services.sql_functions import manipulate_with_data_from_sheet_and_db as manipulate_data


# time.sleep(5)
logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%Y-%m/%dT%H:%M:%S',
                    filename='./log/logfile.log', level=logging.DEBUG)

app = Flask(__name__)
# cors = CORS(app)

app.config['SECRET_KEY'] = "gsheetssecret"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@postgres:5432/{os.environ['POSTGRES_DB']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Deliveries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_id = db.Column(db.Integer)
    order_num = db.Column(db.String(50))
    date = db.Column(db.String(12))
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


deliveries_schema = DeliverySchema(many=True)


@app.route("/health")
def check_health():
    """
        Create table and check server health.
        If there is a need to delete table from DB, uncomment these 2 lines before run
        In a perfect scenario you'll see { status: "OK" } on the screen
    """
    # db.session.query(Deliveries).delete()
    # Deliveries.__table__.drop()
    try:
        logging.info(u'creating tables ----- START')
        db.create_all()
        logging.info(u'tables created ----- OK')
    except Exception as e:
        logging.error(u'tables NOT created ----- ERROR %s', e)

    return jsonify({"status": "OK"})


@app.route("/api")
def get_statistics():
    """
        Main process of the application
        First of all we getting delivery data from Google Sheets table
        Then, using method "manipulate_data" were making one request to central bank
        to get actual USD rate, extend the data with an additional parameter and put it into the db table
        After all, we send the data to front-end app to display it graphically
    """
    try:
        logging.error(u'getting data ----- START')

        google_sheets_data = get_data()
        logging.error(u'data gotten ----- OK')
    except Exception as e:
        logging.error(u'getting data ----- ERROR %s', e)

    try:
        logging.error(u'start data manipulation ----- START')
        manipulate_data(
            session=db.session,
            model=Deliveries,
            schema=deliveries_schema,
            query=Deliveries.query.all(),
            data=google_sheets_data
        )
        logging.error(u'data manipulation ----- OK')
    except Exception as e:
        logging.error(u'data manipulation ----- ERROR %s', e)
    delivery_data = Deliveries.query.all()
    result = deliveries_schema.dump(delivery_data)
    return jsonify(result)
