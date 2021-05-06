from app.models import db, Shelter
import requests
import json


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def shelters_id():
    for i in range(15):
        response = requests.get('https://api.petfinder.com/v2/organizations', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6IjVjZTAyZmYxNDQ1OTA4ZmM5ZTg5NzM0Yzk4NWJiODY5YTU2ZTJiZWY2MTEwYmQxZDgxY2M0Y2QwYjU3NTYxZDUwNzNkMTI0ZjM2M2JiY2RmIiwiaWF0IjoxNjIwMjUyNDE2LCJuYmYiOjE2MjAyNTI0MTYsImV4cCI6MTYyMDI1NjAxNiwic3ViIjoiIiwic2NvcGVzIjpbXX0.fhJS9JcdIq3PMLCr4AHwOIEuQYi97x84W3OAfohcgIUO8Ck6AImAlo6ATrxWTmtQWtT2mzRlff-eLVs57IgEmjmLUwC8jnrLwl7L3YCXOhzsKKcqIm6ipkfzeTB-5jOU4Dvtj61qBarjaQxicpna-FukiVLDONqbT1DLin9rfUnraMJOyZ-yMbu-vn1kzwwOSS0ltJ1_MEMhyNC4gF7hNBIB_LodBHGYwlcoK35CcDT1cfafiWfbhQCM4oZLKHiGz2pqH90DDqpKF6MOcYe5vpCAm9v6xuks-L6G_OIHMGmym96qsAqUxb3jVTVQDkemq-LK-aBjF2wL3dS8poys5w')).json()
        print(response['organizations'][i]['id'])

# print(shelters_id())


shelterIds = [
    'CO316',
    'IN220',
    'OH401',
    'TX420',
    'MO556',
    'IA233',
    'IN200',
    'IN40',
    'TX1920',
    'CA458',
    'WI40',
    'PA546',
    'OH129',
    'NM80',
    'AL254',
    'OR208'
]

def seed_shelters():
    i = 0
    while i < len(shelterIds) -1:
        response = requests.get(f'https://api.petfinder.com/v2/organizations/{shelterIds[i]}', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6ImY1Mzc1ZWIyMmMyNTliMzA1ZWYwY2JmMjAxODBjZjc4Mzk4MjRiMmI5YjlmNzcxYjA0ZTExODgzMjVhM2U0OGJhNTkzZTZmMTBlZTcxM2JiIiwiaWF0IjoxNjIwMzIxNDE4LCJuYmYiOjE2MjAzMjE0MTgsImV4cCI6MTYyMDMyNTAxOCwic3ViIjoiIiwic2NvcGVzIjpbXX0.bVWziWC6xhEkBsg8uNSoEtQIoazVJ9EtDQSZ2dh14tZclsz5SvUqfmo-Hxx-mYJ4otyTQlTvSXaXmdljIluP1mrCeT30sOXjn4sSdz7lLBZAgoq0oMKj3shHplIjo1U62K6OzzlDorlzHJL2qliBmt7CBDimW9zeg2OZu-L4u_t8OA2yJsTUNXcyCdw73zCGMuahZCuHejYWloelsTt7fmxE98CC_H9KrjsiTUlLzEDRuj0KX8YHxOlHaQ4aMQaOT0TSkz9qZzRF5TXMovIN7PMNfKnkbJnFq-XxF9kp8uNdaBztzAFfNt5hToCrO243Hxyg8fK6V7gnIxrRNbnYjg')).json()
        item = response['organization']
        demo = Shelter(
            name = item['name'],
            address = item['address']['city'] + ' ' + item['address']['state'] + ' ' + item['address']['postcode'] + ' ' + item['address']['country'],
            phone_number = item['phone'],
            office_hours = '9-5 ' + '9-5 ' + '9-5 ' + '9-5 ' + '9-5 ' + '12-4 ' + '12-4 ',
            email = item['email'],
            description = item['mission_statement'],
            image_url = item['photos'][0]['full'],
        )
        db.session.add(demo)
        i += 1
    db.session.commit()
# seed_shelters()
# print(seed_shelters())
def undo_shelters():
    db.session.execute('TRUNCATE shelters RESTART IDENTITY CASCADE;')
    db.session.commit()
