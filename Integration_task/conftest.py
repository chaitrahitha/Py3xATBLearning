import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"
@pytest.fixture()
def create_token():
    # token
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking():
    # Booking ID
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    print(booking_id)
    return booking_id

@pytest.fixture()
def payload():
    return {
        "firstname": "Pramod",
        "lastname": "Dutta",
        "totalprice": 1993,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": ["Breakfast", "Dinner"]
    }

@pytest.fixture()
def new_payload():
    return {
        "firstname": "Hitha"
    }


@pytest.fixture()
def invalid_data():
    return {
        "firstname": "",
        "lastname": "蹄铁",
        "totalprice": 1993,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": ["Breakfast", "Dinner"]
    }


@pytest.fixture()
def cookies(create_token):
    return "token=" + create_token


@pytest.fixture()
def header(cookies):
    return {
        "Content-Type": "application/json",
        "Cookie": cookies
    }

# @pytest.fixture()
# def update_booking(create_booking, header, payload):
#     return requests.put(url=base_url + f'/booking/{str(create_booking)}', headers=header, json=payload)