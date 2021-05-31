import functools
import sqlite3

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('product', __name__, url_prefix='/product')


@bp.route('/')
def index():
    db = get_db()
    error = None

    products = db.execute(
        'SELECT product_id, product_name FROM product').fetchall()
    if products is None:
        error = "No products added in database"
        flash(error)
    return render_template('product/index.html', products=products)


@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        prod_id = request.form['product_id']
        product_name = request.form['product_name']
        error = None

        if not product_name:
            error = 'Product name is missing'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE product SET product_name = ? WHERE product_id = ?', (product_name, prod_id))
            db.commit()
            return redirect(url_for('product.index'))

    return render_template('product/index.html')


@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        product_id = request.form['product_id']
        product_name = request.form['product_name']

        error = None

        if not (product_id or product_name):
            error = 'product name or id missing'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO product (product_id, product_name) VALUES (?, ?)',
                       (product_id, product_name))
            db.commit()
        return redirect(url_for('product.index'))

    return render_template('product/index.html')
