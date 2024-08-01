import requests
import json

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

# Create a booking
def create_booking():
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=data)
    if response.status_code == 200:
        print("Booking created successfully!")
        return response.json()["bookingid"]
    else:
        print(f"Failed to create booking: {response.status_code} {response.text}")
        return None

# Update a booking
def update_booking(booking_id, token):
    data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    url = f"{BASE_URL}/booking/{booking_id}"
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Booking updated successfully!")
    else:
        print(f"Failed to update booking: {response.status_code} {response.text}")

# Get a booking
def get_booking(booking_id):
    url = f"{BASE_URL}/booking/{booking_id}"
    response = requests.get(url, headers={"Accept": "application/json"})
    if response.status_code == 200:
        print("Booking details:")
        print(response.json())
    else:
        print(f"Failed to get booking: {response.status_code} {response.text}")

# Delete a booking
def delete_booking(booking_id, token):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    url = f"{BASE_URL}/booking/{booking_id}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 201:
        print("Booking deleted successfully!")
    else:
        print(f"Failed to delete booking: {response.status_code} {response.text}")

# Authenticate to get the token
def authenticate():
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=data)
    if response.status_code == 200:
        return response.json()["token"]
    else:
        print(f"Failed to authenticate: {response.status_code} {response.text}")
        return None

def main():
    # Step 1: Authenticate and get token
    token = authenticate()
    if not token:
        return

    # Step 2: Create a booking
    booking_id = create_booking()
    if not booking_id:
        return

    # Step 3: Update the booking
    update_booking(booking_id, token)

    # Step 4: Get the booking details
    get_booking(booking_id)

    # Step 5: Delete the booking
    delete_booking(booking_id, token)

    # Step 6: Try to get the deleted booking
    get_booking(booking_id)

if __name__ == "__main__":
    main()
