import json

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship

from theapp import db, app

from flask_login import UserMixin


class Category(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, default=0)
    image = Column(Text(4294000000), default='https://res.cloudinary.com/dymtveeni/image/upload/v1712461337/noimage_hk8501.webp')

    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100))
    avatar = Column(Text(4294000000),  default='https://res.cloudinary.com/dymtveeni/image/upload/v1712461337/noimage_hk8501.webp')
    username = Column(String(100), unique=True)
    password = Column(String(50))

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Laptop')
        # db.session.add_all([c1, c2, c3])
        # with open('data/products.json', encoding='utf-8') as f:
        #     products = json.load(f)
        #     for p in products:
        #         prod = Product(**p)
        #         db.session.add(prod)
        import hashlib
        u = User(name='admin', username='admin', avatar='https://res.cloudinary.com/dymtveeni/image/upload/v1712467816/lyk_nlvby9.webp',
                 password=str(hashlib.md5("123456".encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
