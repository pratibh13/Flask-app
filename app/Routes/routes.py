from flask_restx import  Resource, fields,Api
from app import app

ns = Api(app,version='1.0', title='Employee API',
    description='A simple EmployeeMVC API',
)
api = ns.namespace('Employee', description='Employee operations')



from app.Service.service import ProjectDAO,EmployeeDAO
 
project_model = api.model('Project', {
    'id': fields.Integer(readOnly=True, description='The Project unique id'),
    'name': fields.String(readOnly=True, description='The Project name'),
 
})
 
employee_model=api.model('Employee',{
    'id': fields.Integer(readOnly=True, description='The Employee unique id'),
    'name': fields.String(readOnly=True, description='The Employee name'),
    'position': fields.String(readOnly=True, description='The Employee position'),
    'project_id': fields.Integer(readOnly=True, description='The Project unique id'),
}) 
 

project_employee_model = api.model('Project', {
    'id': fields.Integer(description='The project unique identifier'),
    'name': fields.String(description='The project name'),
    'employees': fields.List(fields.Nested({
        'id': fields.Integer(description='The employee unique identifier'),
        'name': fields.String(description='The employee name'),
        'position': fields.String(description='The employee position')
    }), description='List of employees working on the project')
})
 
 
project_service = ProjectDAO()
employee_Service=EmployeeDAO()
 
@api.route("/project")
class Projects(Resource):
    @api.doc('Project_List')
    @api.marshal_list_with(project_model)
    def get(self):
        return project_service.get_projects(), 200
 
    @api.doc('Create_Project')
    @api.expect(project_model)
    @api.marshal_with(project_model, code=201)
    def post(self):
        return project_service.create_project(api.payload), 201
    
 
@api.route("/")
class Employee(Resource):
    @api.doc('Employee_List')
    @api.marshal_list_with(employee_model)
    def get(self):
        return employee_Service.get_Employee(), 200
 
    @api.doc('Create_Employee')
    @api.expect(employee_model)
    @api.marshal_with(employee_model, code=201)
    def post(self):
        return employee_Service.create_Employee(api.payload), 201
    
    
 
 
@api.route("/<int:id>")
@api.param('id', 'The Employee identifier')
@api.response(404, 'Employee not found')
class Employee(Resource): 
    
    @api.doc('Delete_employee_by_id')
    @api.response(204, 'Employee deleted')
    def delete(self, id):
        employee_Service.delete_employee_by_id(id)
        return '', 204
 
    @api.doc('Update_Employee_by_id')
    @api.expect(employee_model)
    @api.marshal_with(employee_model)
    def put(self, id):
        return employee_Service.Update_employee_by_id(id, api.payload)
 
 
@api.route("/project/<int:id>")
@api.param('id', 'The project identifier')
@api.response(404, 'Project not found')
class Project(Resource):
    @api.doc('Get_project_by_id')
    @api.marshal_with(project_model)
    def get(self, id):
        return project_service.get_project_by_id(id)
 
    @api.doc('Delete_project_by_id')
    @api.response(204, 'Project deleted')
    def delete(self, id):
        project_service.delete_project_by_id(id)
        return '', 204
 
    @api.doc('Update_project_by_id')
    @api.expect(project_model)
    @api.marshal_with(project_model)
    def put(self, id):
        return project_service.update_project(id, api.payload)


@api.route("/project/get_all_employees/<int:id>")
@api.param('id', 'The project identifier')
@api.response(404, 'Project or employees of the project not found')
class projectEmployees(Resource):
    @api.marshal_with(project_employee_model)
    def get(self, id):
        project = project_service.get_project_by_id(id)
        if project:
            employees = project_service.get_employees_for_project(id)
            project.employees = employees
            return project
        else:
            api.abort(404, f"Project {id} not found")