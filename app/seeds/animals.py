import requests
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
response = requests.get('https://api.petfinder.com/v2/animals/', auth=BearerAuth('')).json()
print(response['animals'][0]['id'])


def seed_products():
    i = 1
    while i < len(listIds) -1:
        response = requests.get(f'https://openapi.etsy.com/v2/listings/{listIds[i]}/?api_key=9i7i1vu4xhs80233snqp1t4y')
        data = response.json()
        listings = data['results']
        for item in listings:
            demo = Product(
                name=item["title"],
                store_id=(i/20)+1,
                price=item["price"],
                quantity=item["quantity"],
                description=item["description"],
            )
            db.session.add(demo)
        i += 1
    db.session.commit()

def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
