import requests

API_URL='http://127.0.0.1:5000'

# Employee API Tests
def test_get_employee():
    r = requests.get(f'{API_URL}/Employee')
    assert r.status_code == 200

def test_post_Employee():
    payload = {
        "id": 0,
        "name": "Test Username",
        "position": "Test Position",
        "project_id": 1
    }
    r = requests.post(f'{API_URL}/Employee/', json=payload)    
    assert r.status_code == 201
    
def test_put_Employee():
    payload = {
        "id": 0,
        "name": "Test Username Changed",
        "position": "Test Position",
        "project_id": 1
    }
    id=0
    r = requests.put(f'{API_URL}/Employee/{id}', json=payload)    
    assert r.status_code == 200  

def test_delete_Employee():
    id=0
    r = requests.delete(f'{API_URL}/Employee/{id}')    
    assert r.status_code == 204       
    
    
    
# Project API test
def test_get_project():
    r = requests.get(f'{API_URL}/Employee/project')
    assert r.status_code == 200

def test_post_project():
    payload = {
        "id": 0,
        "name": "Test Project",
    }
    r = requests.post(f'{API_URL}/Employee/project', json=payload)    
    assert r.status_code == 201
    
def test_put_project():
    payload = {
        "name": "Test Project Changed",
    }
    id=0
    r = requests.put(f'{API_URL}/Employee/project/{id}', json=payload)    
    assert r.status_code == 200  

def test_delete_project():
    id=0
    r = requests.delete(f'{API_URL}/Employee/project/{id}')    
    assert r.status_code == 204  
  
def test_get_all_employees_for_project():
    id=1
    r = requests.get(f'{API_URL}/Employee/project/get_all_employees/{id}')
    assert r.status_code == 200