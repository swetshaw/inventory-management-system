import functools
import sqlite3

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('location', __name__, url_prefix='/location')


@bp.route('/')
def index():
    db = get_db()
    error = None

    locations = db.execute(
        'SELECT location_id, location_name FROM location').fetchall()
    if locations is None:
        error = "No locations added in database"
    return render_template('location/index.html', locations=locations)


@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        location_name = request.form['location_name']
        loc_id = request.form['location_id']
        error = None

        if not location_name:
            error = 'Location name is missing'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE location SET location_name = ? WHERE location_id = ?', (location_name, loc_id))
            db.commit()
            return redirect(url_for('location.index'))

    return render_template('location/location.html')


@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        location_id = request.form['location_id']
        location_name = request.form['location_name']

        error = None

        if not (location_id or location_name):
            error = 'location name or id missing'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO location (location_id, location_name) VALUES (?, ?)',
                       (location_id, location_name))
            db.commit()
        return redirect(url_for('location.index'))

    return render_template('location/index.html')
