
from json import dumps
from uuid import uuid4


def test_non_unique_id():
    payload = dumps{
        'fname': 'New',
        'lname': unique_last_name
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    assert_that(response.status).is_equal_to(409)