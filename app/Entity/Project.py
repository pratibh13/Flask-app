from app.Database.database import db

class Project(db.Model):
     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(100))
     
     def __repr__(self):
        return f"Project {self.id}:{self.name}"