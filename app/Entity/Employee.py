from app.Database.database import db

class Employee(db.Model):
     
     __tablename__='employee'
     
     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(100), nullable=False)
     position=db.Column(db.String(100), nullable=False)
     project_id=db.Column(db.Integer,nullable=True)
     

        