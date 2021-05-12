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
        response = requests.get('https://api.petfinder.com/v2/organizations', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6IjZiZjFhZjNlZTQxNGFlNzY2ODA5NWI5YjEzMTdhNjA5MjQ3NzUzNTAyY2JiYTc4MTNjYjExMjNiNDk5NzU4MmU4ZDc0YjEwMjhmNTYyMWI4IiwiaWF0IjoxNjIwMzU2NjYxLCJuYmYiOjE2MjAzNTY2NjEsImV4cCI6MTYyMDM2MDI2MSwic3ViIjoiIiwic2NvcGVzIjpbXX0.cqNsC4odDlqpoiqA_3F4Mkcr8rIFj-EW-oUviiaH9j54CfipoDuGV5bxr-41zmzDUb56W6b6zZeEk6tDCGMbXQHqSh7F3xuA3VyT0ALb5DgtHED5QhIcC4Z501uO5SdEzyyFhZ4awVdE8mQm7XxVkE7-m9-QGoBhe02S9yxoNiZSuapekAeAw14XQqls3apwX0ThhfMc32rWpNF1zN-ucJz4JDhqFjEYF-Cqk2jyiWxCpSIasugz03Vpjc9HeeYdpRM6kseF-hI65LyramIxIem2GCQ32i92KRBrB_sP4z4QVY1JxWHg7tJZyOmZAsxRDwHe7dfsVvtB6P0BJ1NfyQ')).json()
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
        response = requests.get(f'https://api.petfinder.com/v2/organizations/{shelterIds[i]}', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6IjQwMWRjNzE5MmFiMTg2NTU4ODRiMmJmY2Q0ODQ3MDkyN2ZlYmQ3ZTAzNTU1OTZhMThjMWM1NDE3NTg2MzBjM2VhODZhNGE2ZTliNzgxMWYzIiwiaWF0IjoxNjIwODMyNzgxLCJuYmYiOjE2MjA4MzI3ODEsImV4cCI6MTYyMDgzNjM4MSwic3ViIjoiIiwic2NvcGVzIjpbXX0.WK0Bm6neqdT1It5Adxb_byQev5v9XZee9nQHt17O2ZEeZKoi_pw8mtld4T9tkP_9arsbkCtUnprcLZlZAkCt_gVlU6_rbfz5G2lBKSd-1MG0X4XGezqfYbnWjeGaVaaOaxpAoOyemPtU9_AL31DQTPyIWgqrp333li92T8sAFIkdJ_qitBFkt4FF7-LNW_GnVSVIXaZOrEGERu0q8uzywENbAOp8tDkY0w73Mrn_KdqnjfpK7mkMQjkDynXcwVoXxEMG9RDGt9vzzC7T-dcuen7OoleV5z97oUwFop4GOBKC2cZKCmA_RW46Vy78KTf1RB2ONpg4c2Tc0HIgdeSdmw')).json()
        item = response['organization']
        if item['address']['address1']:
            demo = Shelter(
                name = item['name'],
                address = item['address']['address1'] + ' ' + item['address']['city'] + ' ' + item['address']['state'] + ' ' + item['address']['postcode'] + ' ' + item['address']['country'],
                phone_number = item['phone'],
                office_hours = '9-5 ' + '9-5 ' + '9-5 ' + '9-5 ' + '9-5 ' + '12-4 ' + '12-4 ',
                email = item['email'],
                description = item['mission_statement'],
                image_url = item['photos'][0]['full'],
            )
        else:
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
