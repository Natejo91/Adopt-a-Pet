from .db import db


class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey("breeds.id"), nullable=False)
    description = db.Column(db.String, nullable=False)
    shelter_id = db.Column(db.Integer, db.ForeignKey("shelters.id"), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "breed_id": self.breed_id,
            "description": self.description,
            "shelter_id": self.shelter_id,
            "photos": [photo.to_dict() for photo in self.photos]
        }

    photos = db.relationship("Photo", back_populates="animals", cascade="all, delete")
    breeds = db.relationship("Breed", back_populates="animals", cascade="all, delete")
    shelters = db.relationship("Shelter", back_populates="animals", cascade="all, delete")
    favorite_animals = db.relationship("Favorite_Animal", back_populates="animals", cascade="all, delete")
