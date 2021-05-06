from .db import db


class Favorite_Animal(db.Model):
    __tablename__ = "favorite_animals"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "animal_id": self.animal_id,
            "favorite_animal": [animal.to_dict() for animal in self.animals if self.animal_id in animal]
        }

    users = db.relationship("User", back_populates="favorite_animals")
    animals = db.relationship("Animal", back_populates="favorite_animals")
