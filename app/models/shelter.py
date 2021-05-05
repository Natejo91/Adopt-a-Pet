from .db import db


class Shelter(db.Model):
    __tablename__ = "shelters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(14), nullable=False)
    office_hours = db.Column(db.String(200))
    description = db.Column(db.String(2000), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number,
            "office_hours": self.office_hours,
            "description": self.description
        }


    animals = db.relationship("Animal", back_populates="shelters", cascade="all, delete")
