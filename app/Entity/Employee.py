from app.Database.database import db

class Employee(db.Model):
     
     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(100), nullable=False)
     position=db.Column(db.String(100), nullable=False)
     project_id=db.Column(db.Integer,nullable=True)
     
     def __repr__(self):
        return f"Employee {self.id}:{self.name}:{self.position}:{self.project_id}"
        