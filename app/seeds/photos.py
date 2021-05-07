from app.models import db, Photo


def seed_photos():

    photo = Photo(
        animal_id=1,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID1.jpg'
    )

    db.session.add(photo)

    photo1 = Photo(
        animal_id=2,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID2.jpg'
    )

    db.session.add(photo1)

    photo2 = Photo(
        animal_id=3,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID3.jpg'
    )

    db.session.add(photo2)

    photo3 = Photo(
        animal_id=4,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID4.jpg'
    )

    db.session.add(photo3)

    photo4 = Photo(
        animal_id=5,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID5.jpg'
    )

    db.session.add(photo4)

    photo5 = Photo(
        animal_id=6,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID6.jpg'
    )

    db.session.add(photo5)

    photo6 = Photo(
        animal_id=7,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID7.jpg'
    )

    db.session.add(photo6)

    photo7 = Photo(
        animal_id=8,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID8.jpg'
    )

    db.session.add(photo7)

    photo8 = Photo(
        animal_id=8,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID8-2.jpg'
    )

    db.session.add(photo8)

    photo9 = Photo(
        animal_id=8,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID8-3.jpg'
    )

    db.session.add(photo9)

    photo10 = Photo(
        animal_id=9,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID9.jpg'
    )

    db.session.add(photo10)

    photo11 = Photo(
        animal_id=9,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID9-2.jpg'
    )

    db.session.add(photo11)

    photo12 = Photo(
        animal_id=9,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID9-3.jpg'
    )

    db.session.add(photo12)

    photo13 = Photo(
        animal_id=10,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID10.jpg'
    )

    db.session.add(photo13)

    photo14 = Photo(
        animal_id=10,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID10-2.jpg'
    )

    db.session.add(photo14)

    photo15 = Photo(
        animal_id=10,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID10-3.jpg'
    )

    db.session.add(photo15)

    photo16 = Photo(
        animal_id=11,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID11.jpg'
    )

    db.session.add(photo16)

    photo17 = Photo(
        animal_id=11,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID11-2.jpg'
    )

    db.session.add(photo17)

    photo18 = Photo(
        animal_id=11,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID11-3.jpg'
    )

    db.session.add(photo18)

    photo19 = Photo(
        animal_id=12,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID12.jpg'
    )

    db.session.add(photo19)

    photo20 = Photo(
        animal_id=12,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID12-2.jpg'
    )

    db.session.add(photo20)

    photo21 = Photo(
        animal_id=12,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID12-3.jpg'
    )

    db.session.add(photo21)

    photo22 = Photo(
        animal_id=13,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID13.jpg'
    )

    db.session.add(photo22)

    photo23 = Photo(
        animal_id=13,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID13-2.jpg'
    )

    db.session.add(photo23)

    photo24 = Photo(
        animal_id=13,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID13-3.jpg'
    )

    db.session.add(photo24)

    photo25 = Photo(
        animal_id=14,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID14.jpg'
    )

    db.session.add(photo25)

    photo26 = Photo(
        animal_id=14,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID14-2.jpg'
    )

    db.session.add(photo26)

    photo27 = Photo(
        animal_id=14,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID14-3.jpg'
    )

    db.session.add(photo27)

    photo28 = Photo(
        animal_id=15,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID15.jpg'
    )

    db.session.add(photo28)

    photo29 = Photo(
        animal_id=15,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID15-2.jpg'
    )

    db.session.add(photo29)

    photo30 = Photo(
        animal_id=15,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID15-3.jpg'
    )

    db.session.add(photo30)

    photo31 = Photo(
        animal_id=16,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID16.jpg'
    )

    db.session.add(photo31)

    photo32 = Photo(
        animal_id=17,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID17.jpg'
    )

    db.session.add(photo32)

    photo33 = Photo(
        animal_id=18,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID18.jpg'
    )

    db.session.add(photo33)

    photo34 = Photo(
        animal_id=19,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID19.jpg'
    )

    db.session.add(photo34)

    photo35 = Photo(
        animal_id=19,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID19-2.jpg'
    )

    db.session.add(photo35)

    photo36 = Photo(
        animal_id=20,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID20.jpg'
    )

    db.session.add(photo36)

    photo37 = Photo(
        animal_id=20,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID20-2.jpg'
    )

    db.session.add(photo37)

    photo38 = Photo(
        animal_id=20,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID20-3.jpg'
    )

    db.session.add(photo38)

    photo39 = Photo(
        animal_id=20,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID20-4.jpg'
    )

    db.session.add(photo39)

    photo40 = Photo(
        animal_id=21,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID21.jpg'
    )

    db.session.add(photo40)

    photo41 = Photo(
        animal_id=22,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID22.jpg'
    )

    db.session.add(photo41)

    photo42 = Photo(
        animal_id=23,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID23.jpg'
    )

    db.session.add(photo42)

    photo43 = Photo(
        animal_id=24,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID24.jpg'
    )

    db.session.add(photo43)

    photo44 = Photo(
        animal_id=24,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID24-2.jpg'
    )

    db.session.add(photo44)

    photo45 = Photo(
        animal_id=25,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID25.jpg'
    )

    db.session.add(photo45)

    photo46 = Photo(
        animal_id=25,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID25-2.jpg'
    )

    db.session.add(photo46)

    photo47 = Photo(
        animal_id=25,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID25-3.jpg'
    )

    db.session.add(photo47)

    photo48 = Photo(
        animal_id=26,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID26.jpg'
    )

    db.session.add(photo48)

    photo49 = Photo(
        animal_id=26,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID26-2.jpg'
    )

    db.session.add(photo49)

    photo50 = Photo(
        animal_id=26,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID26-3.jpg'
    )

    db.session.add(photo50)

    photo51 = Photo(
        animal_id=27,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID27.jpg'
    )

    db.session.add(photo51)

    photo52 = Photo(
        animal_id=27,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID27-2.jpg'
    )

    db.session.add(photo52)

    photo53 = Photo(
        animal_id=27,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID27-3.jpg'
    )

    db.session.add(photo53)

    photo54 = Photo(
        animal_id=28,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID28.jpg'
    )

    db.session.add(photo54)

    photo55 = Photo(
        animal_id=28,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID28-2.jpg'
    )

    db.session.add(photo55)

    photo56 = Photo(
        animal_id=28,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID28-3.jpg'
    )

    db.session.add(photo56)

    photo57 = Photo(
        animal_id=29,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID29.jpg'
    )

    db.session.add(photo57)

    photo58 = Photo(
        animal_id=30,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID30.jpg'
    )

    db.session.add(photo58)

    photo59 = Photo(
        animal_id=30,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID30-2.jpg'
    )

    db.session.add(photo59)

    photo60 = Photo(
        animal_id=30,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID30-3.jpg'
    )

    db.session.add(photo60)

    photo61 = Photo(
        animal_id=31,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID31.jpg'
    )

    db.session.add(photo61)

    photo62 = Photo(
        animal_id=32,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID32.jpg'
    )

    db.session.add(photo62)

    photo63 = Photo(
        animal_id=32,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID32-2.jpg'
    )

    db.session.add(photo63)

    photo64 = Photo(
        animal_id=32,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID32-3.jpg'
    )

    db.session.add(photo64)

    photo65 = Photo(
        animal_id=33,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID33.jpg'
    )

    db.session.add(photo65)

    photo66 = Photo(
        animal_id=33,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID33-2.jpg'
    )

    db.session.add(photo66)

    photo67 = Photo(
        animal_id=34,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID34.jpg'
    )

    db.session.add(photo67)

    photo68 = Photo(
        animal_id=34,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID34-2.jpg'
    )

    db.session.add(photo68)

    photo69 = Photo(
        animal_id=35,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID35.jpg'
    )

    db.session.add(photo69)

    photo70 = Photo(
        animal_id=35,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID35-2.jpg'
    )

    db.session.add(photo70)



    db.session.commit()

def undo_photos():
    db.session.execute('TRUNCATE photos RESTART IDENTITY CASCADE;')
    db.session.commit()
