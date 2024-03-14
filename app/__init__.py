from flask import Flask
app = Flask(__name__)

from app.Database.database import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/projects'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
    
from app.Routes import routes
