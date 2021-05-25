# from werkzeug.security import generate_password_hash
from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(
        first_name='Demo',
        last_name='lition',
        zipcode='46410',
        email='demo@aa.io',
        password='password',
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/noun_User_3918328.png'
    )

    db.session.add(demo)

    user1 = User(
        first_name='James',
        last_name='Robinson',
        zipcode='80011',
        email='james@gmail.com',
        password='password',
        image_url=None
    )

    db.session.add(user1)

    user2 = User(
        first_name='Maria',
        last_name='Landon',
        zipcode='29601',
        email='maria@gmail.com',
        password='password',
        image_url=None
    )

    db.session.add(user2)

    user3 = User(
        first_name='Daniel',
        last_name='Jones',
        zipcode='90001',
        email='daniel@gmail.com',
        password='password',
        image_url=None
    )

    db.session.add(user3)

    user4 = User(
        first_name='Ashley',
        last_name='Williams',
        zipcode='90045',
        email='ashley@gmail.com',
        password='password',
        image_url=None
    )

    db.session.add(user4)

    user5 = User(
        first_name='Andrew',
        last_name='Jackson',
        zipcode='10025',
        email='andrew@gmail.com',
        password='password',
        image_url=None
    )

    db.session.add(user5)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
