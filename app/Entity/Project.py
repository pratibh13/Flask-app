from app.Database.database import db

class Project(db.Model):
     
     __tablename__='project'
     
     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(100))
     