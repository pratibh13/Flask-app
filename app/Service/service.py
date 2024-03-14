from app.Database.database import db
from app.Entity.Project import Project
from app.Entity.Employee import Employee
 
# Project Service
class ProjectDAO(object):
    def get_projects(self):
        return Project.query.all()
    
 
    def delete_project_by_id(self, id):
        project = Project.query.get(id)
        db.session.delete(project)
        db.session.commit()
 
    def update_project(self, id, data):
        project = Project.query.get(id)
        project.name = data['name']
        db.session.commit()
        return project
    
    def get_project_by_id(self, id):
        return Project.query.filter_by(id=id).first()
 
    def create_project(self, data):
        
        project = Project(id=data["id"],name=data['name'])
        db.session.add(project)
        db.session.commit()
        return project
    
    def get_employees_for_project(self,project_id):
        employees=db.session.query(Employee).filter_by(project_id=project_id).all()
        return employees
    
# Employee Service
class EmployeeDAO(object):    
    def get_Employee(self):
        return Employee.query.all()
    
    def create_Employee(self, data):
        
        employee = Employee(id=data["id"],name=data['name'],position=data['position'],project_id=data["project_id"])
        db.session.add(employee)
        db.session.commit()
        return employee
 
    
    def delete_employee_by_id(self, id):
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
 
    def Update_employee_by_id(self, id, data):
        employee = Employee.query.get(id)
        employee.name = data['name']
        employee.position = data['position']
        db.session.commit()
        return employee
