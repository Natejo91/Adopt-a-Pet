from .db import db


class Shelter(db.Model):
    __tablename__ = "shelters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    office_hours = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    image_url = db.Column(db.String(2000))


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email,
            "office_hours": self.office_hours,
            "description": self.description,
            "image_url": self.image_url
        }


    animals = db.relationship("Animal", back_populates="shelters", cascade="all, delete")
