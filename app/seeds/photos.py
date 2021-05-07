from app.models import db, Photo


def seed_photos():
    photo1 = Photo(
        animal_id=2,
        image_url='https://pet-python-project.s3.amazonaws.com/petID2.jpg'
    )

    db.session.add(photo1)

    # photo2 = Photo(
    #     animal_id=3
    #     image_url=''
    # )

    # db.session.add(photo2)

    # photo3 = Photo(
    #     animal_id=4
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51248858/1/?bust=1620345773'
    # )

    # db.session.add(photo3)

    # photo4 = Photo(
    #     animal_id=5
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51415665/1/?bust=1620273651'
    # )

    # db.session.add(photo4)

    # photo5 = Photo(
    #     animal_id=6
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51330219/1/?bust=1620324163'
    # )

    # db.session.add(photo5)

    # photo6 = Photo(
    #     animal_id=7
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51398045/1/?bust=1620230349'
    # )

    # db.session.add(photo6)

    # photo7 = Photo(
    #     animal_id=8
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51373700/1/?bust=1620038172'
    # )

    # db.session.add(photo7)

    # photo8 = Photo(
    #     animal_id=8
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51373700/2/?bust=1620038170'
    # )

    # db.session.add(photo8)

    # photo9 = Photo(
    #     animal_id=8
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51373700/3/?bust=1620038171'
    # )

    # db.session.add(photo9)

    # photo10 = Photo(
    #     animal_id=9
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51434757/1/?bust=1620297374'
    # )

    # db.session.add(photo10)

    # photo11 = Photo(
    #     animal_id=9
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51434757/2/?bust=1620297374'
    # )

    # db.session.add(photo11)

    # photo12 = Photo(
    #     animal_id=9
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51434757/3/?bust=1620297375'
    # )

    # db.session.add(photo12)

    # photo13 = Photo(
    #     animal_id=10
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51303715/1/?bust=1619778956'
    # )

    # db.session.add(photo13)

    # photo14 = Photo(
    #     animal_id=10
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51303715/2/?bust=1619778951'
    # )

    # db.session.add(photo14)

    # photo15 = Photo(
    #     animal_id=10
    #     image_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/51303715/3/?bust=1619778956'
    # )

    # db.session.add(photo15)

    # photo15 = Photo(
    #     animal_id=
    #     image_url=''
    # )

    # db.session.add(photo15)\

    db.session.commit()

def undo_photos():
    db.session.execute('TRUNCATE photos RESTART IDENTITY CASCADE;')
    db.session.commit()
