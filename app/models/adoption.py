from .db import db


class Adoption(db.Model):
    __tablename__ ="adoptions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey("animals.id"), nullable=False)
    message = db.Column(db.String, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "animal_id": self.animal_id,
            "message": self.message
        }


    users = db.relationship("User", back_populates="adoptions", cascade="all, delete")
    animals = db.relationship("Animal", back_populates="adoptions", cascade="all, delete")
