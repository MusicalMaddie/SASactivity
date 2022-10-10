import requests
from assertpy.assertpy import assert_that
from config import BASE_URL

response = ''


def func(x):
    assert(1 == 1)


def test_delete_a_user():
    global response
    response = requests.delete(BASE_URL+'/api/users/2')
    assert_that(response.status_code).is_equal_to(204)


def test_verify_proper_response_is_received():
    global response
    assert_that(response.status_code).is_equal_to(204)

