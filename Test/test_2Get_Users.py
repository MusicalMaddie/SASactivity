import requests
from assertpy import assert_that
import sys
import json
from config import BASE_URL
from Models.user import UserModel
from utils.printing import pretty_print
sys.path.append('/opt/homebrew/lib/python3.9/site-packages')


print("Starting Test 2")
response = ''
response2 = ''
responseUsersOnly = ''
response_json = ''
users_list = []


def func_get_all_users():
    global response
    global response2
    response = requests.get(BASE_URL+'/users?page=1')
    response2 = requests.get(BASE_URL+'/users?page=2')

    global response_json
    response_json = response.json()
    response2_json = response2.json()

    # iterate through page 1
    y = json.loads(json.dumps(response_json))
    x = y["data"]
    global responseUsersOnly
    responseUsersOnly = x
    print(responseUsersOnly)
    for peoples in x:
        f = UserModel(peoples['id'], peoples['email'], peoples['first_name'], peoples['last_name'], peoples['avatar'])
        users_list.append(f.full_name)

    # iterage through page 2
    y = json.loads(json.dumps(response2_json))
    x = y["data"]
    for peoples in x:
        f = UserModel(peoples['id'], peoples['email'], peoples['first_name'], peoples['last_name'], peoples['avatar'])
        users_list.append(f.full_name)
    pretty_print(users_list)

    return response


def test_status_code_get_list_of_users():
    func_get_all_users()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response2.status_code).is_equal_to(200)


def test_verify_response_get_all_users():
    func_get_all_users()
    assert_that(json.dumps(response_json['data'])).contains('tracey.ramos@reqres.in')
    assert_that(json.dumps(response_json['data'])).contains('Janet')
    assert_that(json.dumps(response_json['data'])).contains('Emma')


def test_report_number_of_users_returned():
    func_get_all_users()
    if response.status_code == 200:
        print('Total number of users listed: ' + str(len(users_list)))
