from datetime import datetime

import flask
from flask import request  # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify  # übersetzt python-dicts in json
from flask import g
import sqlite3

DATABASE = '/Users/sven.d2/Desktop/2023.09.26_tisch_reservierung/tischreservierung-o/database.db'
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


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"


@app.route('/tables', methods=['GET'])
def get_tables():
    query_parameters = request.args

    start = query_parameters.get('start')
    end = query_parameters.get('end')

    if start is None:
        start = datetime.min.strftime('%Y-%m-%d %H:%M:%S')

    if end is None:
        end = datetime.max.strftime('%Y-%m-%d %H:%M:%S')

    reservations = get_db().execute('''
        SELECT tische.tischnummer, tische.anzahlPlaetze, reservierungen.zeitpunkt FROM tische 
        LEFT JOIN reservierungen ON tische.tischnummer = reservierungen.tischnummer 
        WHERE (zeitpunkt >= ? AND zeitpunkt <= ?) AND storniert is FALSE;
        ''', [start, end]).fetchall()

    return jsonify({'tables': reservations})


app.run(port=3001)
