from flask import Flask
app = Flask(__name__)

from app.Database.database import db
import config
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
from app.Entity import Project,Employee 
with app.app_context():
    db.create_all()     
from app.Routes import routes
