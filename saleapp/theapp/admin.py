from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user

from theapp import app, db
from theapp.models import Category, Product

admin = Admin(app, name='E-commerce Website', template_mode='bootstrap4')


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'image', 'category_id']
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class MyCategoryView(ModelView):
    column_list = ['id', 'name', 'products']

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(LogoutView(name='Log out'))
