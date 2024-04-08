import math

from flask import render_template, request, redirect
from flask_login import login_user

from dao import load_categories, load_products, get_product_by_id, count_product, get_user_by_id, auth_user
from theapp import app, login
from theapp import admin

@app.route('/')
def home():
    q = request.args.get('q')
    category_id = request.args.get('category_id')
    page = request.args.get('page')

    products = load_products(q, category_id, page)
    return render_template('index.html', products=products, pages=math.ceil(count_product()/app.config['PAGE_SIZE']))


@app.route('/products/<id>')
def details(id):
    product = get_product_by_id(id)
    return render_template('product-details.html', product=product)

@login.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)


@app.route("/admin-login", methods=['post'])
def process_admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    u = auth_user(username=username, password=password)
    if u:
        login_user(user=u)

    return redirect('/admin')


@app.context_processor
def common_attributes():
    return {
        'categories': load_categories()
    }


if __name__ == '__main__':
    app.run(debug=True)
