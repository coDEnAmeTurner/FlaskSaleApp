import hashlib

from flask import json, request

from theapp import app
from theapp.models import Category, Product, User


def load_categories():
    return Category.query.all()


def load_products(q, category_id, page):
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))

    if page:
        page_size = app.config['PAGE_SIZE']
        start = (int(page) - 1) * page_size
        query = query.slice(start, start + page_size)

    return query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)


def count_product():
    return Product.query.count()


def get_user_by_id(id):
    return User.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()