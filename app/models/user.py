from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    zipcode = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(255), nullable = False, unique = True)
    hashed_password = db.Column(db.String(255), nullable = False)
    image_url = db.Column(db.String(2000))

    favorite_animals = db.relationship("Favorite_Animal", back_populates="users", cascade="all, delete")
    adoptions = db.relationship("Adoption", back_populates="users", cascade="all, delete")

    @property
    def password(self):
        return self.hashed_password


    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "zipcode": self.zipcode,
            "image_url": self.image_url,
            "favorite_animals": {favorite_animal.animal_id: favorite_animal.animal_id for favorite_animal in self.favorite_animals}
    }
