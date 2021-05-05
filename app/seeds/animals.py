import requests
import json
form app.models import (db, Animal)



class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def animals_id():
    for i in range(20):
        response = requests.get('https://api.petfinder.com/v2/animals?type=dog', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6IjhjMDM5NDY1NDNkOTQzYTBjZTRjZWFiY2NmZDEyMTY2YWMzMGI3ZWVlMzBjNDY5ZDYzYWEyNzI0YmQyNmMwM2M0MjViMjYzZjk1MTJiOTQ3IiwiaWF0IjoxNjIwMjI4MzAxLCJuYmYiOjE2MjAyMjgzMDEsImV4cCI6MTYyMDIzMTkwMSwic3ViIjoiIiwic2NvcGVzIjpbXX0.CXv3af2ekjKQ51STwPXjbJwS41hWA4jq97pLjmFDBFzWe_fBcw2FnuqlL37rLXeFo7W5PwiTEXBjaag2O9x8bVTjJ5JoFDiTjtuFpyrkXzV7be0BrNP4DxjtmBZWrEzlj3nz_wZueb7OuvCPtVK1IC-lNImi0lM68LmqtdA6_oQkgqGXZ8OvSW-lYUfbf6GkZou1BID-n_7XgSrJCgPLDyHfn4d3B2NBfhqkkFxTy9TZG2pPqZrzHUUvhXnQa6YSwkW34BA0kp7Fsg95CUlbbtLmen_68uATh6hR5co0lMpchOzJbf2ae_F_Hm0PeYtY4QQose3RESfQFXbQfcPsbg')).json()
        print(response['animals'][i]['id'])

print(animals_id())

listIds = [
    51437750,
    51437808,
    51437837,
    51437664,
    51437840,
    51437833,
    51437836,
    51437827,
    51437828,
    51437825,
    51437822,
    51437818,
    51437819,
    51437820,
    51437821,
    51437809,
    51437811,
    51437813,
    51437814,
    51437807,
    51437697,
    51437634,
    51437750,
    51437808,
    51437837,
    51437840,
    51437833,
    51437836,
    51437827,
    51437828,
    51437829,
    51437825,
    51437822,
    51437818,
    51437819,
    51437820,
    51437821,
    51437809,
    51437811,
    51437813,
    51437857,
    51437859,
    51437697,
    51437634,
    51437750,
    51437808,
    51437837,
    51437840,
    51437833,
    51437836,
    51437827,
    51437828,
    51437829,
    51437825,
    51437822,
    51437818,
    51437819,
    51437820,
    51437821,
    51437809,
]


def seed_products():
    i = 1
    while i < len(listIds) -1:
        response = requests.get(f'https://api.petfinder.com/v2/animals/{listIds[i]}', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6IjhjMDM5NDY1NDNkOTQzYTBjZTRjZWFiY2NmZDEyMTY2YWMzMGI3ZWVlMzBjNDY5ZDYzYWEyNzI0YmQyNmMwM2M0MjViMjYzZjk1MTJiOTQ3IiwiaWF0IjoxNjIwMjI4MzAxLCJuYmYiOjE2MjAyMjgzMDEsImV4cCI6MTYyMDIzMTkwMSwic3ViIjoiIiwic2NvcGVzIjpbXX0.CXv3af2ekjKQ51STwPXjbJwS41hWA4jq97pLjmFDBFzWe_fBcw2FnuqlL37rLXeFo7W5PwiTEXBjaag2O9x8bVTjJ5JoFDiTjtuFpyrkXzV7be0BrNP4DxjtmBZWrEzlj3nz_wZueb7OuvCPtVK1IC-lNImi0lM68LmqtdA6_oQkgqGXZ8OvSW-lYUfbf6GkZou1BID-n_7XgSrJCgPLDyHfn4d3B2NBfhqkkFxTy9TZG2pPqZrzHUUvhXnQa6YSwkW34BA0kp7Fsg95CUlbbtLmen_68uATh6hR5co0lMpchOzJbf2ae_F_Hm0PeYtY4QQose3RESfQFXbQfcPsbg')).json()
        animal = response['animal']
        for item in animal:
            demo = Animal(
                name=item["name"],
                store_id=(i/20)+1,
                price=item["price"],
                quantity=item["quantity"],
                description=item["description"],
            )
            db.session.add(demo)
        i += 1
    db.session.commit()

def undo_products():
    db.session.execute('TRUNCATE animals RESTART IDENTITY CASCADE;')
    db.session.commit()
