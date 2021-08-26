from fastapi.testclient import TestClient

from main import app
from modules.patients.utils import convert_to_lowercase_naming
from modules.table import exports

client = TestClient(app)


def test_root_view():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello world!'}


def test_get_patient_signatures_by_id():
    """Case #1: patient found"""
    data = exports.get_data_from_table('NSCLC378')
    response = client.get('/api/patients/NSCLC378')
    assert response.status_code == 200
    assert response.json() == data.dict(by_alias=True)
    """Case #2: inclide fields"""
    fields = 'MHCI,MHCII,Coactivation_molecules,T_cell_traffic,M1_signatures'
    fields_list = convert_to_lowercase_naming(fields.split(','))
    response = client.get(f'/api/patients/NSCLC378?is_include=true&fields={fields}')
    assert response.status_code == 200
    assert response.json() == data.dict(by_alias=True, include=set(fields_list))
    """Case #3: exclude fields"""
    response = client.get(f'/api/patients/NSCLC378?is_include=false&fields={fields}')
    assert response.status_code == 200
    assert response.json() == data.dict(by_alias=True, exclude=set(fields_list))
    """Case #4: Patient not found"""
    response = client.get('/api/patients/NSCLC37')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Patient not found.'}
