import requests
from assertpy import assert_that
from Models.user import UserModel
from config import BASE_URL
from utils.printing import pretty_print

response_json = ''
testUser2 = UserModel(0, '1', '1', '1', 'none')


def func_response(i):

    response = requests.get(BASE_URL+'/users/'+str(i))
    global response_json
    response_json = response.json()

    user_data = response_json['data']
    global testUser2
    if response.status_code == 200:
        testUser2 = UserModel(user_data['id'], user_data['email'], user_data['first_name'], user_data['last_name'], user_data['avatar'])
    return response


def test_get_single_test_user():
    func_response(2)
    pretty_print(func_response(2))
    assert_that(testUser2.first_name).contains('Janet')
    assert_that(testUser2.email).contains('janet.weaver@reqres.in')
    assert_that(testUser2.id).is_equal_to(2)


def test_verify_formatted_json_returned_for_valid_user():
    assert_that(testUser2.first_name).contains('Janet')
    assert_that(testUser2.email).contains('janet.weaver@reqres.in')
    assert_that(testUser2.id).is_equal_to(2)


def test_response_for_invalid_user_requested():
    response = requests.get(BASE_URL+'/users/-1')
    assert_that(response.status_code).is_equal_to(404)



