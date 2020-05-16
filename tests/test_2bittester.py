invalid_dates_payload = {
    "bookingdates": {
        "checkin": "",
        "checkout": ""
    },
    "depositpaid": False,
    "firstname": "gleek",
    "lastname": "zorp",
    "roomid": 1,
    "email": "yourmom@email.com",
    "phone": "phone number"
}

payload = {
    "bookingdates": {
        "checkin": "2020-05-08",
        "checkout": "2020-05-13"},
    "depositpaid": False,
    "firstname": "gleek",
    "lastname": "zorp",
    "roomid": 1,
    "email": "yourmom@email.com",
    "phone": "phone number"
}

URL = 'https://automationintesting.online/booking/'


def test_make_a_booking(api):
    response = api.post(URL, json=payload, headers={'content-type', 'application/xml'})
    assert response.ok
