from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/flasksaledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 3
app.secret_key = 'iouashdfeiuh qaiuesriuoafesal iusfoiuasueir fgo8uih asoi fho8aipushe rf989843w67987t3456789ion nbhdxgfrt bvc'

db = SQLAlchemy(app)

login = LoginManager(app)
