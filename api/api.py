from datetime import datetime

import flask
from flask import request  # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify  # übersetzt python-dicts in json
from flask import g
import sqlite3

DATABASE = '/Users/sven.d2/Desktop/tischreservierung-o/database.db'
app = flask.Flask(__name__)
app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def to_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d-%H-%M')


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"


@app.route('/tables', methods=['GET'])
def get_tables():
    query_parameters = request.args

    start = query_parameters.get('start', default=datetime.now(), type=to_date)
    end = query_parameters.get('end', default=datetime.now(), type=to_date)

    tables = get_db().execute('SELECT * FROM tische;').fetchall()
    reservations = get_db().execute('SELECT * FROM reservierungen;').fetchall()

    return jsonify({'start': start.isoformat(), 'end': end.isoformat(), 'tables': tables,
                    'reservations': reservations})


app.run(port=3001)
