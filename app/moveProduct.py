from app.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import functools
import sqlite3
from datetime import datetime

date = datetime.now()


bp = Blueprint('moveProduct', __name__, url_prefix='/moveproduct')


@bp.route('/')
def index():
    db = get_db()
    error = None

    products = db.execute(
        'SELECT product_id, product_name FROM product').fetchall()
    locations = db.execute(
        'SELECT location_id, location_name from location'
    ).fetchall()
    all_moves = db.execute(
        'SELECT * from productMovement'
    ).fetchall()
    return render_template('moveProduct/index.html', products=products, locations=locations, all=all_moves)


@bp.route('/add', methods=['GET', 'POST'])
def add():
    db = get_db()
    products = db.execute(
        'SELECT product_id, product_name FROM product').fetchall()
    locations = db.execute(
        'SELECT location_id, location_name from location'
    ).fetchall()

    if request.method == "POST":
        mov_id = request.form['mov_id']
        prod_name = request.form['product_name']
        to_loc = request.form['to_location']
        from_loc = request.form['from_location']
        qty = request.form['qty']

        error = None

        # print("Inside edit")
        # print(to_loc, from_loc)

        try:
            prod_id_ = db. execute(
                'SELECT product_id from product WHERE product_name =?', (prod_name,)).fetchall()
            to_loc_id_ = db. execute(
                'SELECT location_id from location WHERE location_name = ?', (to_loc,)).fetchall()
            from_loc_id_ = db. execute(
                'SELECT location_id from location WHERE location_name = ?', (from_loc,)).fetchall()
            # print(prod_id_)
            # print(to_loc_id_)

            prod_id = ''.join([str(p[0]) for p in prod_id_])
            to_loc_id = ''.join([str(t[0]) for t in to_loc_id_])
            from_loc_id = ''.join([str(f[0]) for f in from_loc_id_])

            if to_loc_id in [None, '', ' '] and from_loc_id in [None, '', ' ']:
                error = "Either enter from location or to location"
                
            if error is not None:
                flash(error)
            else:
                db.execute('INSERT INTO productMovement (movement_id, time_stamp, from_location, to_location, product_id, qty) VALUES (?, ?, ?, ?, ?, ?)',
                        (mov_id, date, from_loc_id, to_loc_id, prod_id, qty))
                db.commit()
        except sqlite3.Error as e:
            print(e.args[0])

        return redirect(url_for('moveProduct.index'))
    return render_template('moveProduct/index.html', products=products, locations=locations)
