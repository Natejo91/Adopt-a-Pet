from app.models import db, Shelter
from faker import Faker

faker = Faker()

def seed_shelters():
    shelter1 = Shelter(
        name = "Animal Care Center",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )
    db.session.add(shelter1)

    shelter2 = Shelter(
        name = "Green Pastures",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter2)

    shelter3 = Shelter(
        name = "For Pet's Sake",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter3)

    shelter4 = Shelter(
        name = "Besty Beasties",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter4)

    shelter5 = Shelter(
        name = "The Bark Station",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter5)

    shelter6 = Shelter(
        name = "Maw and Paw",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter6)


    shelter7 = Shelter(
        name = "On the Growl",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter7)

    shelter8 = Shelter(
        name = "Paws and Pooches",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter8)

    shelter9 = Shelter(
        name = "Waggamuffins",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter9)

    shelter10 = Shelter(
        name = "Balls of Fluff",
        address = faker.address(),
        phone_number = faker.numerify('(###) ### ####'),
        email = faker.email(),
        office_hours = "Monday 11AM-4PM, Tuesday 11AM-6:30PM, Wednesday 11AM-5PM, Thursday 11AM-6:30PM, Friday 11AM-5PM, Saturday 11AM-5PM, Sunday 11AM-4PM",
        description = faker.sentences(4),
        image_url= None
    )

    db.session.add(shelter10)

    db.session.commit()


def undo_shelters():
    db.session.execute('TRUNCATE shelters RESTART IDENTITY CASCADE;')
    db.session.commit()
