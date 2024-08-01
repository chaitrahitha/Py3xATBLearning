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
def test_put_request_positive(create_token, create_booking,header,payload):
    put_response = update_booking(create_booking,header,payload)
    assert put_response.status_code == 200
    data = put_response.json()
    print(data)
    print(put_response.url)
    assert data["totalprice"] == 1993

    get_response = get_booking(create_booking)
    assert get_response.status_code == 200
    get_response_data = get_response.json()
    print(get_response_data)
    print(get_response.url)
    assert get_response_data["totalprice"] == payload["totalprice"]

@allure.title("verify that create booking, patch request, verify that firstname is updated")
@allure.id("Integration_scenario_TC#2")
def test_delete(create_token, create_booking,header,new_payload):

    patch_response = partial_update_booking(create_booking, header, new_payload)
    assert patch_response.status_code == 200
    print(patch_response.url)
    patch_response_data = patch_response.json()
    print(patch_response_data)
    assert patch_response_data["firstname"] == "Hitha"

@allure.title("verify that create booking, patch request, verify that firstname is updated")
@allure.id("Integration_scenario_TC#3")
def test_get(create_booking,header,payload):
    #create booking
    get_res = post_booking(payload)
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
    del_response = delete_booking(bookindId, header)
    assert del_response.status_code == 201
    print(del_response.url)
    del_response_data = del_response.content
    print(del_response_data)
    #get deleted booking
    get_res = get_booking(bookindId)
    assert get_res.status_code == 404
    print(get_res.content)

@allure.title("Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.")
@allure.id("Integration_scenario_TC#4")
def test_get_all_booking_ids(header,new_payload):
    get_res =requests.get(url=base_url+f'/booking')
    assert get_res.status_code == 200
    # print(get_res.content)

    get_res_id = requests.get(url=base_url+f'/booking/{str(32)}')
    print(get_res_id.url)
    print(get_res_id.content)
    assert get_res_id.status_code == 200

    update_res = requests.patch(url=base_url+f'/booking/{str(32)}',headers=header,json=new_payload)
    assert update_res.status_code == 200
    update_res_data = update_res.json()
    assert update_res_data["firstname"] == "Hitha"

    get_res = requests.get(url=base_url + f'/booking/{str(32)}')
    assert get_res.status_code == 200
    print(get_res.content)

@allure.title("Create a BOOKING, Delete It")
@allure.id("Integration_scenario_TC#5")
def test_create_delete(header,payload):

    #create booking
    get_res = post_booking(payload)
    assert get_res.status_code == 200
    get_res_data = get_res.json()
    print(get_res_data)
    print(get_res.url)
    bookindId = get_res_data["bookingid"]
    print(bookindId)
    #delete it
    del_response = delete_booking(bookindId, header)
    assert del_response.status_code == 201
    print(del_response.url)
    del_response_data = del_response.content
    print(del_response_data)
    # get deleted booking
    get_res = get_booking(bookindId)
    assert get_res.status_code == 404
    print(get_res.content)

@allure.title("Invalid Creation - enter a wrong payload or Wrong JSON.")
@allure.id("Integration_scenario_TC#6")
def test_invalid_creation(invalid_data):
    res = requests.post(url=base_url+f'/booking', json=invalid_data)
    assert res.status_code == 200

@allure.title("Trying to Update on a Delete ID -> 404")
@allure.id("Integration_scenario_TC#7")
def test_delete_id(create_booking,header,new_payload):
    update_res = partial_update_booking(create_booking, header, new_payload)
    assert update_res.status_code == 200

    delete_res = delete_booking(create_booking,header)
    assert delete_res.status_code == 201

    get_res = get_booking(create_booking)
    assert get_res.status_code == 404


def get_booking(create_booking):
    return requests.get(url=base_url + f'/booking/{str(create_booking)}')


def update_booking(create_booking, header, payload):
    return requests.put(url=base_url + f'/booking/{str(create_booking)}', headers=header, json=payload)


def partial_update_booking(create_booking, header, new_payload):
    return requests.patch(url=base_url + f'/booking/{str(create_booking)}', headers=header, json=new_payload)


def post_booking(payload):
    return requests.post(url=base_url + f'/booking', json=payload)


def delete_booking(create_booking, header):
    return requests.delete(url=base_url + f'/booking/{str(create_booking)}', headers=header)
