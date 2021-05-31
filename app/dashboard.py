import functools
import sqlite3

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('dashboard', __name__, url_prefix='/')


@bp.route('/')
def index():
    db = get_db()
    error = None

    products = db.execute(
        'SELECT product_id, product_name FROM product').fetchall()
    locations = db.execute(
        'SELECT location_id, location_name from location'
    ).fetchall()

    # print(products)
    dash = []
    try:
        for p_id in [p[0] for p in products]:
            prod_name = db.execute(
                'SELECT product_name FROM product WHERE product_id = ?', (p_id,)).fetchone()

            for l_id in [l[0] for l in locations]:
                loc_name = db.execute(
                    'SELECT location_name FROM location WHERE location_id = ?', (l_id,)).fetchone()

                qty_from_loc = db.execute(
                    'SELECT SUM(mp.qty) FROM productMovement as mp WHERE mp.product_id = ? AND mp.from_location = ?', (p_id, l_id)).fetchone()

                qty_to_loc = db.execute(
                    'SELECT SUM(mp.qty) FROM productMovement as mp WHERE mp.product_id = ? AND mp.to_location = ?', (p_id, l_id)).fetchone()

                if qty_from_loc[0] in [None, '', ' ']:
                    qty_from_loc = (0,)
                if qty_to_loc[0] in [None, '', ' ']:
                    qty_to_loc = (0,)

                net_qty = qty_to_loc[0] - qty_from_loc[0]
                if net_qty != 0 and net_qty > 0:
                    dash.append([prod_name, loc_name, net_qty])

    except sqlite3.Error as e:
        flash(e.args[0])

    return render_template('dashboard/dashboard.html', dash=dash)
