# PUT
# URL
# Path - Bookinf ID
# Token - Auth
# Payload
import allure
import pytest
import requests  # pip install requests

base_url = "https://restful-booker.herokuapp.com"

@allure.title("verify that create booking, put request, verify that totalprice is updated")
@allure.id("Integration_scenario_TC#1")
def test_put_request_postive(create_token, create_booking):

    cookie = cookies(create_token)
    headerss = header(cookie)
    json_payload = payload()

    put_response = updateBooking(create_booking, headerss, json_payload)
    assert put_response.status_code == 200
    data = put_response.json()
    print(data)
    print(put_response.url)
    assert data["totalprice"] == 1993

    get_response = getBooking(create_booking)
    assert get_response.status_code == 200
    get_response_data = get_response.json()
    print(get_response_data)
    print(get_response.url)
    assert get_response_data["totalprice"] == json_payload["totalprice"]

@allure.title("verify that create booking, patch request, verify that firstname is updated")
@allure.id("Integration_scenario_TC#2")
def test_delete(create_token, create_booking):

    cookie = cookies(create_token)
    headerss = header(cookie)
    json_payload = new_payload()

    patch_response = partialupdateBooking(create_booking, headerss, json_payload)
    assert patch_response.status_code == 200
    print(patch_response.url)
    patch_response_data = patch_response.json()
    print(patch_response_data)
    assert patch_response_data["firstname"] == "Hitha"

@allure.title("verify that create booking, patch request, verify that firstname is updated")
@allure.id("Integration_scenario_TC#3")
def test_get(create_booking, create_token):

    cookie = cookies(create_token)
    headerss = header(cookie)
    json_payload = payload()
    #create booking
    get_res = requests.post(url=base_url + f'/booking', json=json_payload)
    assert get_res.status_code == 200
    get_res_data = get_res.json()
    print(get_res_data)
    print(get_res.url)
    bookindId = get_res_data["bookingid"]
    print(bookindId)
    #get booking by booking id
    res = requests.get(url=base_url + f'/booking/{str(bookindId)}')
    assert res.status_code == 200
    data = res.json()
    print(data)
    print(res.url)
    #delete booking
    del_response = deleteBooking(bookindId, headerss)
    assert del_response.status_code == 201
    print(del_response.url)
    del_response_data = del_response.content
    print(del_response_data)
    #get deleted booking
    get_res = getBooking(bookindId)
    assert get_res.status_code == 404
    print(get_res.content)

@allure.title("Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.")
@allure.id("Integration_scenario_TC#4")
def test_get_all_booking_ids(create_token):
    cookie = cookies(create_token)
    headerss = header(cookie)
    json_payload = new_payload()

    get_res =requests.get(url=base_url+f'/booking')
    assert get_res.status_code == 200

    get_res_id = requests.get(url=base_url+f'/booking/{str(12)}')
    print(get_res_id.url)
    print(get_res_id.content)
    assert get_res_id.status_code == 200

    update_res = requests.patch(url=base_url+f'/booking/{str(19)}',headers=headerss,json=json_payload)
    assert update_res.status_code == 200
    update_res_data = update_res.json()
    assert update_res_data["firstname"] == "Hitha"

    get_res = requests.get(url=base_url + f'/booking/{str(19)}')
    assert get_res.status_code == 200
    print(get_res.content)

@allure.title("Create a BOOKING, Delete It")
@allure.id("Integration_scenario_TC#5")
def test_create_delete(create_token):
    cookie = cookies(create_token)
    headerss = header(cookie)
    json_payload = payload()
    #create booking
    # get_res = requests.post(url=base_url + f'/booking', json=json_payload)
    get_res = postBooking(json_payload)
    assert get_res.status_code == 200
    get_res_data = get_res.json()
    print(get_res_data)
    print(get_res.url)
    bookindId = get_res_data["bookingid"]
    print(bookindId)
    #delete it
    del_response = deleteBooking(bookindId, headerss)
    assert del_response.status_code == 201
    print(del_response.url)
    del_response_data = del_response.content
    print(del_response_data)
    # get deleted booking
    get_res = getBooking(bookindId)
    assert get_res.status_code == 404
    print(get_res.content)

@allure.title("Invalid Creation - enter a wrong payload or Wrong JSON.")
@allure.id("Integration_scenario_TC#6")
def test_invalid_creation():
    data = {
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
    res = requests.post(url=base_url+f'/booking', json=data)
    assert res.status_code == 200

@allure.title("Trying to Update on a Delete ID -> 404")
@allure.id("Integration_scenario_TC#7")
def test_delete_id(create_booking,create_token):
    cookie = cookies(create_token)
    headerss = header(cookie)
    json_payload = new_payload()
    update_res = partialupdateBooking(create_booking, headerss, json_payload)
    assert update_res.status_code == 200

    delete_res = deleteBooking(create_booking,headerss)
    assert delete_res.status_code == 201

    get_res =getBooking(create_booking)
    assert get_res.status_code == 404



def updateBooking(create_booking, header, payload):
    return requests.put(url=base_url + f'/booking/{str(create_booking)}', headers=header, json=payload)


def getBooking(create_booking):
    return requests.get(url=base_url + f'/booking/{str(create_booking)}')


def header(cookie):
    return {
        "Content-Type": "application/json",
        "Cookie": cookie
    }


def cookies(create_token):
    return "token=" + create_token


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


def partialupdateBooking(create_booking, header, new_payload):
    return requests.patch(url=base_url + f'/booking/{str(create_booking)}', headers=header, json=new_payload)


def new_payload():
    return {
        "firstname": "Hitha"
    }


def postBooking(payload):
    return requests.post(url=base_url + f'/booking', json=payload)


def deleteBooking(create_booking, header):
    return requests.delete(url=base_url + f'/booking/{str(create_booking)}', headers=header)
