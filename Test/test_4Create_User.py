import requests
import json
from assertpy import assert_that
from json import dumps
from config import BASE_URL, USERNAME, PASSWORD
from utils.printing import pretty_print
from uuid import uuid4

created_user_response = ''
response_json = ''
example_json = json.dumps({'createdAt': '2022-10-10T00:46:16.434Z', 'id': '113'})


def func(x):

    assert(1 == 1)


def test_create_new_user():
    unique_email = f'User {str(uuid4())}'
    payload = dumps({
        'email': unique_email,
        'password': 'testpassword'
    })
    response = requests.post(url=BASE_URL+'/users', data=payload)
    global response_json
    response_json = response.json()
    pretty_print(response_json)
    assert_that(response.status_code).is_equal_to(201)


def test_response_verify_expected_json_attributes_when_user_created():
    y = json.loads(json.dumps(response_json))
    pretty_print('ID created by submission:'+y["id"])
    assert_that(response_json).contains('createdAt')
    assert_that(response_json).contains_key('id')
