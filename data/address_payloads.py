from faker import Faker


fake = Faker("en_US")

def build_address_payload():
    payload = {
        "address": {
            "fullName": {
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
            },
            "company": fake.company(),
            "taxInfo": {
                "id": None,
                "type": None,
            },
            "addressLine1": "4537 Monte Mar Drive",
            "addressLine2": "45",
            "street": {
                "name": None,
                "number": f"+1{fake.numerify(text='##########')}",
            },
            "city": "El Dorado Hills",
            "country": "USA",
            "subdivision": "CA",
            "zipCode": "95762",
            "phoneNumber": None,
            "location": {
                "latitude": 38.6382313,
                "longitude": -121.0728334,
            },
        },
        "setAsDefault": False,
    }

    return payload
