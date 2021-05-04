from .db import db


class Photo(db.Model):
    __tablename__ = "photos"

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey("animals.id"))
    image_url = db.Column(db.String(2000))


    def to_dict(self):
        return {
            "id": self.id,
            "animal_id": self.animal_id,
            "image_url": self.image_url
        }


    animals = db.relationship("Animal", back_populates="photos", cascade="all, delete")
