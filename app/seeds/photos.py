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

    photo71 = Photo(
        animal_id=36,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID36.jpg'
    )

    db.session.add(photo71)

    photo72 = Photo(
        animal_id=36,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID36-2.jpg'
    )

    db.session.add(photo72)

    photo73 = Photo(
        animal_id=36,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID36-3.jpg'
    )

    db.session.add(photo73)

    photo74 = Photo(
        animal_id=37,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID37.jpg'
    )

    db.session.add(photo74)

    photo75 = Photo(
        animal_id=37,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID37-2.jpg'
    )

    db.session.add(photo75)

    photo76 = Photo(
        animal_id=38,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID38.jpg'
    )

    db.session.add(photo76)

    photo77 = Photo(
        animal_id=39,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID39.jpg'
    )

    db.session.add(photo77)

    photo78 = Photo(
        animal_id=39,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID39-2.jpg'
    )

    db.session.add(photo78)

    photo79 = Photo(
        animal_id=40,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID40.jpg'
    )

    db.session.add(photo79)

    photo80 = Photo(
        animal_id=41,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID41.jpg'
    )

    db.session.add(photo80)

    photo81 = Photo(
        animal_id=41,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID41-2.jpg'
    )

    db.session.add(photo81)

    photo82 = Photo(
        animal_id=41,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID41-3.jpg'
    )

    db.session.add(photo82)

    photo83 = Photo(
        animal_id=42,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID42.jpg'
    )

    db.session.add(photo83)

    photo84 = Photo(
        animal_id=42,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID42-2.jpg'
    )

    db.session.add(photo84)

    photo85 = Photo(
        animal_id=42,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID42-3.jpg'
    )

    db.session.add(photo85)

    photo86 = Photo(
        animal_id=43,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID43.jpg'
    )

    db.session.add(photo86)

    photo87 = Photo(
        animal_id=43,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID43-2.jpg'
    )

    db.session.add(photo87)

    photo88 = Photo(
        animal_id=44,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID44.jpg'
    )

    db.session.add(photo88)

    photo89 = Photo(
        animal_id=44,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID44-2.jpg'
    )

    db.session.add(photo89)

    photo90 = Photo(
        animal_id=44,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID44-3.jpg'
    )

    db.session.add(photo90)

    photo91 = Photo(
        animal_id=45,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID45.jpg'
    )

    db.session.add(photo91)

    photo92 = Photo(
        animal_id=45,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID45-2.jpg'
    )

    db.session.add(photo92)

    photo93 = Photo(
        animal_id=45,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID45-3.jpg'
    )

    db.session.add(photo93)

    photo94 = Photo(
        animal_id=46,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID46.jpg'
    )

    db.session.add(photo94)

    photo95 = Photo(
        animal_id=46,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID46-2.jpg'
    )

    db.session.add(photo95)

    photo96 = Photo(
        animal_id=46,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID46-3.jpg'
    )

    db.session.add(photo96)

    photo97 = Photo(
        animal_id=47,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID47.jpg'
    )

    db.session.add(photo97)

    photo98 = Photo(
        animal_id=47,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID47-2.jpg'
    )

    db.session.add(photo98)

    photo99 = Photo(
        animal_id=47,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID47-3.jpg'
    )

    db.session.add(photo99)

    photo100 = Photo(
        animal_id=48,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID48.jpg'
    )

    db.session.add(photo100)

    photo101 = Photo(
        animal_id=48,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID48-2.jpg'
    )

    db.session.add(photo101)

    photo102 = Photo(
        animal_id=48,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID48-3.jpg'
    )

    db.session.add(photo102)

    photo103 = Photo(
        animal_id=49,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID49.jpg'
    )

    db.session.add(photo103)

    photo104 = Photo(
        animal_id=49,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID49-2.jpg'
    )

    db.session.add(photo104)

    photo105 = Photo(
        animal_id=50,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID50.jpg'
    )

    db.session.add(photo105)

    photo106 = Photo(
        animal_id=50,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID50-2.jpg'
    )

    db.session.add(photo106)

    photo107 = Photo(
        animal_id=51,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID51.jpg'
    )

    db.session.add(photo107)

    photo108 = Photo(
        animal_id=51,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID51-2.jpg'
    )

    db.session.add(photo108)

    photo109 = Photo(
        animal_id=51,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID51-3.jpg'
    )

    db.session.add(photo109)

    photo110 = Photo(
        animal_id=52,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID52.jpg'
    )

    db.session.add(photo110)

    photo111 = Photo(
        animal_id=52,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID52-2.jpg'
    )

    db.session.add(photo111)

    photo112 = Photo(
        animal_id=52,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID52-3.jpg'
    )

    db.session.add(photo112)

    photo113 = Photo(
        animal_id=53,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID53.jpg'
    )

    db.session.add(photo113)

    photo114 = Photo(
        animal_id=53,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID53-2.jpg'
    )

    db.session.add(photo114)

    photo115 = Photo(
        animal_id=53,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID53-3.jpg'
    )

    db.session.add(photo115)

    photo116 = Photo(
        animal_id=54,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID54.jpg'
    )

    db.session.add(photo116)

    photo117 = Photo(
        animal_id=54,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID54-2.jpg'
    )

    db.session.add(photo117)

    photo118 = Photo(
        animal_id=54,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID54-3.jpg'
    )

    db.session.add(photo118)

    photo119 = Photo(
        animal_id=55,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID55.jpg'
    )

    db.session.add(photo119)

    photo120 = Photo(
        animal_id=55,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID55-2.jpg'
    )

    db.session.add(photo120)

    photo121 = Photo(
        animal_id=55,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID55-3.jpg'
    )

    db.session.add(photo121)

    photo122 = Photo(
        animal_id=56,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID56.jpg'
    )

    db.session.add(photo122)

    photo123 = Photo(
        animal_id=56,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID56-2.jpg'
    )

    db.session.add(photo123)

    photo124 = Photo(
        animal_id=56,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID56-3.jpg'
    )

    db.session.add(photo124)

    photo125 = Photo(
        animal_id=57,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID57.jpg'
    )

    db.session.add(photo125)

    photo126 = Photo(
        animal_id=57,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID57-2.jpg'
    )

    db.session.add(photo126)

    photo127 = Photo(
        animal_id=57,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID57-3.jpg'
    )

    db.session.add(photo127)

    photo128 = Photo(
        animal_id=58,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID58.jpg'
    )

    db.session.add(photo128)

    photo129 = Photo(
        animal_id=58,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID58-2.jpg'
    )

    db.session.add(photo129)

    photo130 = Photo(
        animal_id=58,
        image_url='https://pet-python-project.s3.us-east-2.amazonaws.com/petID58-3.jpg'
    )

    db.session.add(photo130)

    db.session.commit()

def undo_photos():
    db.session.execute('TRUNCATE photos RESTART IDENTITY CASCADE;')
    db.session.commit()
