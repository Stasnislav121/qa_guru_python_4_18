import requests
from pytest_voluptuous import S
from requests import Response

from schemas.reqres import single_user_schema, delayed_response_schema, list_resources_schema, create_user_schema, \
    registration_successful_schema, registration_unsuccessful_schema


def test_single_user():
    url = "https://reqres.in/api/users/2"
    response: Response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == S(single_user_schema)
    assert response.json()['data']['id'] == 2


def test_single_user_not_found():
    url = "https://reqres.in/api/users/23"
    response: Response = requests.get(url)
    assert response.status_code == 404
    assert response.reason == "Not Found"
    assert response.json() == {}


def test_list_resource():
    url = "https://reqres.in/api/unknown"
    response: Response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['per_page'] == 6
    assert response.json()['total'] == 12
    assert response.json() == S(list_resources_schema)


def test_crete_user():
    url = "https://reqres.in/api/users"
    data_user = {"name": "morpheus", "job": "leader"}
    response: Response = requests.post(url, data=data_user)
    assert response.status_code == 201
    assert response.json() == S(create_user_schema)


def test_put_user():
    url = "https://reqres.in/api/users/3"
    data_user = {"name": "morpheus", "job": "leader"}
    response: Response = requests.put(url, data_user)
    assert response.status_code == 200
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "leader"


def test_patch_user():
    url = "https://reqres.in/api/users/2"
    data_user = {"name": "morpheus", "job": "zion resident"}
    response: Response = requests.patch(url, data_user)
    assert response.status_code == 200
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "zion resident"


def test_delete():
    url = "https://reqres.in/api/users?page=2"
    response: Response = requests.delete(url)
    assert response.status_code == 204
    assert response.reason == 'No Content'
    assert response.text == ''


def test_register_successful():
    url = "https://reqres.in/api/register"
    data_user = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response: Response = requests.post(url, data_user)
    assert response.status_code == 200
    assert response.json() == S(registration_successful_schema)
    assert response.json()['id'] == 4
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_register_unsuccessful():
    url = "https://reqres.in/api/register"
    data_user = {"email": "sydney@fife"}
    response: Response = requests.post(url, data_user)
    assert response.status_code == 400
    assert response.json() == S(registration_unsuccessful_schema)


def test_delayed_response():
    url = "https://reqres.in/api/users?delay=3"
    response: Response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == S(delayed_response_schema)
    assert response.json()['per_page'] == 6
    assert response.json()['total'] == 12
