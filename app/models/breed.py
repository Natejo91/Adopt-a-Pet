from .db import db


class Breed(db.Model):
    __tablename__ = "breeds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    image_url = db.Column(db.String(2000))


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image_url": self.image_url
        }


    animals = db.relationship("Animal", back_populates="breeds", cascade="all, delete")
