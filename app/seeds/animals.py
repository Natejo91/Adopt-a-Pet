# import requests
# import json
from app.models import (db, Animal)


def seed_animals():
    #animals from shelter CO316
    #51438327
    animal1 = Animal(
        type='Dog',
        name='Benji',
        age='Senior',
        gender='Male',
        breed_id=168,
        description='Benji is a sweet gent who charms everyone he meets. His former owner gave him up reluctantly, after 11 years, because of her own illness. She described him as a wonderful companion and said, I love him with all my heart. People at the shelter describe Benji as gentle and friendly. He came to DFL with severe dental problems, which have been addressed, and has a medical issue that will need to be explored by your own vet',
        shelter_id=1
    )

    db.session.add(animal1)

    #51194602
    animal2 = Animal(
        type='Dog',
        name='Billy',
        age='Adult',
        gender='Male',
        breed_id=15,
        description='Want an enthusiastic exercise partner for all hours of the day? Want a companion who just wants to play? Want someone who will do anything not for a Klondike bar, but for a treat? Then you\'ve met your match in Billy! Billy is chock-full of energy and goofiness and ready to go at all times. Due to his size and the aforementioned energy, he needs to be in a home with kids 12 and older-- and preferably with a patient (and strong!) owner who is already physically active so he can slot himself right in with no problems! Billy will also need to live in a pitbull-friendly community. Come meet him today!',
        shelter_id=1
    )

    db.session.add(animal2)

    #51382895
    animal3 = Animal(
        type='Dog',
        name='Cresent',
        age='Young',
        gender='Male',
        breed_id=15,
        description='Sometimes great things DO come in big packages and there\'s no better example of that than Crescent! Crescent has a sweet face, a strong love of treats and an affectionate demeanor-- once he gets to know you, of course. He\'s not so sure about strangers, but if you bring the whole family in to meet him, then no one will be a stranger anymore and he can start to put his best paw forward! Even better, he\'s housebroken and has no history of escape or destruction! He will need a home without other pets, and without children under the age of 13, so he can have all of your love all to himself.',
        shelter_id=1
    )

    db.session.add(animal3)

    #51248858
    animal4 = Animal(
        type='Dog',
        name='Lime',
        age='Adult',
        gender='Male',
        breed_id=45,
        description='Lime is a super sweetheart who loves people, pets, peanut butter, exercise and action! He can jump at least 5 feet in the air (frisbee, anyone?) He\'s playful, energetic, housetrained, very strong and knows sit (a well-behaved boy). He likes to run with his person, has good endurance and speed and is mostly uninterested in pedestrians and bicyclists. He needs regular physical and mental activities and exercise for his soul and to reduce any desire to escape looking for fun. Chew toys and strong bones are good, too. He takes medication for skin allergies to keep him comfortable and healthy and will need this for his lifetime. If you\'re a very active, affectionate person looking for a loving, fun, four-legged friend to play with, here he is! (One caveat, though, Lime apparently doesn\'t like water.)',
        shelter_id=1
    )

    db.session.add(animal4)

    #51415665
    animal5 = Animal(
        type='Dog',
        name='Chaz',
        age='Young',
        gender='Male',
        breed_id=105,
        description='Chaz is an intelligent guy who knows it! We don\'t know if he\'s ever really lived indoors but he\'s been adapting quickly. We\'ve found out he loves to run, get massages and eat treats! At first he was fearful of the shelter, but once he got comfortable, he\'s very high energy and needs someone to keep up with him! He\'s playful, curious, sweet and friendly; a real outdoors boy who likes to sniff everything. If you\'re active and can give Chaz a total minimum of two hours a day of daily enrichment, exercise and positive reinforcement training, and you live in a home with a secured fenced yard (he\'s a door darter because he loves outdoors so much), you two could be great buddies! Kids age 12 or older.',
        shelter_id=1
    )

    db.session.add(animal5)

    #51330219
    animal6 = Animal(
        type='Dog',
        name='Ava',
        age='Adult',
        gender='Female',
        breed_id=83,
        description='Meet Ava, a 4-year-old spayed female German Shepherd. Ava is a beautiful girl who has some very specific behavioral needs for her forever home. She can\'t go home with children under 12, and she needs to meet your whole family, including any current pet dogs, before you adopt. She\'s still working on her housetraining, and not escaping, so your family should be prepared to be patient with that.',
        shelter_id=1
    )

    db.session.add(animal6)

    #51398045
    animal7 = Animal(
        type='Dog',
        name='Bella',
        age='Young',
        gender='Female',
        breed_id=14,
        description='Bella is a nervous girl, who hasn\'t had much training. She has leash reactivity towards people and other animals, and will pull/bark/lunge at others on leash; though reportedly did live well with another dog. Bella will not enjoy places like dog parks or doggie daycare, and she will need to avoid those. Due to her fear seen in the shelter, she should meet any possible new dog friend before adoption. She was noted to have a lot of separation anxiety, resulting in destruction. She should not live in a home with any shared walls, or in apartment complexes; she would do best in a quiet home with a yard. She needs to meet everyone in the home before adoption, and may do best without small children. She would benefit from an active owner, willing to use positive reinforcement only.',
        shelter_id=1
    )

    db.session.add(animal7)

    #animals from shelter IN220
    #51373700
    animal8 = Animal(
        type='Dog',
        name='Thumbelina',
        age='Young',
        gender='Female',
        breed_id=131,
        description='Thumbelina is a friendly young hound who loves to bounce around the yard and play! She is still a puppy, so she does jump up when excited and might accidentally knock down tiny children, but we\'d expect her to be friendly with humans of all sizes. She has been a great addition to our playgroups and can keep up with the big dogs no problem. She loves to be chased and hardly seems to notice if the big guys knock her down! Thumbelina has been friendly with all the humans she has met here at the shelter and is sure to be adopted quickly, so be sure to come meet this little lady soon!',
        shelter_id=2
    )

    db.session.add(animal8)

    #51434757
    animal9 = Animal(
        type='Dog',
        name='King',
        age='Young',
        gender='Male',
        breed_id=54,
        description='King is a good-looking, extra large man looking for a forever home. This guy has spent his life roaming a 100-acre farm and will be in need of a dedicated owner willing to work on obedience and leash training. Unfortunately from his time outside he has tested positive Lyme disease. He will require a course of medication to overcome this and make sure he is healthy for years to come post-adoption. Please inquire about meeting him today! He would love to meet you!',
        shelter_id=2
    )

    db.session.add(animal9)

    #51303715
    animal10 = Animal(
        type='Dog',
        name='Cherokke Rose',
        age='Adult',
        gender='Female',
        breed_id=29,
        description='Cherokee Rose is a return case that lived in a home for several years before coming back to us due to changed behavior around their children. We noticed that she was underweight and had a lump on her hind foot. After a visit to our vet, we discovered that Cherokee\'s lump was cancerous and removed it. We are currently assessing medical options going forward for her, which staff would be happy to discuss with interested adopters. She currently wears a bandage on her foot and a cone, but she\'s still perky and eager to see her people! She is a very sweet dog who absolutely loves to cuddle with her person; she\'d be a perfect work from home companion! Cherokee has been known to climb fences and make grand escapes, so she would need supervision or to be on leash while outdoors. She is selective about other dogs and seems content to just do her own thing.',
        shelter_id=2
    )

    db.session.add(animal10)

    #51277191
    animal11 = Animal(
        type='Dog',
        name='Monster Truck',
        age='Adult',
        gender='Male',
        breed_id=16,
        description='Monster Truck is ready to rock your world. He showed up at the shelter extremely thin and in rough shape. After some weeks of TLC and lots of yummy food, he is starting to feel like himself again. He\'s eager to meet new people and an expert at catching treats. He has been in our dog playgroups, and coexists well with most dogs. He\'s not a big player, but enjoys being around the other dogs and engages in some gentle-dainty play. He is heartworm positive and is currently receiving daily medication to prepare for his heartworm treatment. The shelter will cover this treatment in full. Please come meet this guy today! He\'s ready for a loving forever home.',
        shelter_id=2
    )

    db.session.add(animal11)

    #51176135
    animal12 = Animal(
        type='Dog',
        name='William',
        age='Senior',
        gender='Male',
        breed_id=16,
        description='William is the most handsome of elder gentlemen, with his gentle smile and curious head tilt. He is a very friendly guy and simply goes with the flow. He enjoys snacks very much and is currently underweight, so he gets two whole meals a day! William does well around other dogs around his size or larger, but he does think that smaller dogs are something fun to chase. He also has some joint issues, so his best match is a gentle dog that isn\'t into rough playing. William can be a little spicy at times and will poke at his dog friends, but it\'s all in good fun! He is quite content to lie on a comfy bed and snooze for much of the day, but a few walks and time in the yard are great too. We believe that William may be partially or entirely deaf--not such a bad thing, because it means he can snooze even if his neighbors are noisy!',
        shelter_id=2
    )

    db.session.add(animal12)

    #51256521
    animal13 = Animal(
        type='Dog',
        name='Diesel',
        age='Adult',
        gender='Male',
        breed_id=45,
        description='Diesel is a very energetic dog who loves to roll and tumble with the best of them. He really likes to hop up and say hello every chance he gets. He responds well to direction and respects people\'s demands. He can be a little nervous initially, but he warms up and becomes a goofy puppy dog. He loves to run around and play chase with some dogs. He does seem to be a little particular about the dogs he enjoys playing with. He is very housetrained and really enjoys his walks outside.',
        shelter_id=2
    )

    db.session.add(animal13)

    #51158287
    animal14 = Animal(
        type='Dog',
        name='Duke',
        age='Adult',
        gender='Male',
        breed_id=105,
        description='Duke is a very happy guy who has tons of exuberant energy! He likes to run and leap through the yard, and is starting to figure out what to do with toys. He is super, super food motivated and already knows how to sit and lie down. Duke is eager to learn if you\'ve got snacks! He does like to jump up when he\'s excited and he\'s a big dude, so he might be too much for small children. Duke has attended playgroup here and likes to hang out with the other dogs. He does sometimes display some inappropriate play styles of the mounting variety, so he would be best matched to a tolerant dog. He is eager to learn and listens well to his doggy pals.',
        shelter_id=2
    )

    db.session.add(animal14)


    #animals from shelter OH401
    #49974858
    animal15 = Animal(
        type='Dog',
        name='Hobo',
        age='Senior',
        gender='Male',
        breed_id=105,
        description='I am a sweet, friendly, quiet boy, and I get along with cats and other dogs, as long as they are friendly and not really high energy. A really pushy, dominant dog might scare me and a high energy dog might knock me over. I don\'t really play with other dogs but enjoy their company.',
        shelter_id=3
    )

    db.session.add(animal15)

    #45278151
    animal16 = Animal(
        type='Dog',
        name='2 Chocolate Labs',
        age='Adult',
        gender='Male',
        breed_id=105,
        description='Two beautiful labs that must be adopted together! Hopefully we can find a great home for the two!',
        shelter_id=3
    )

    db.session.add(animal16)

     #45278170
    animal17 = Animal(
        type='Dog',
        name='2 Yellow Labs',
        age='Adult',
        gender='Female',
        breed_id=105,
        description='Two beautiful labs that must be adopted together! Hopefully we can find a great home for the two!',
        shelter_id=3
    )

    db.session.add(animal17)

    #45278177
    animal18 = Animal(
        type='Dog',
        name='Josie',
        age='Adult',
        gender='Female',
        breed_id=105,
        description='Wonderful black lab that has only been at our shelter for 2 weeks. He is very popular with everyone and loves to take walks outside.',
        shelter_id=3
    )

    db.session.add(animal18)


    #animals from shelter TX420
    #50170195
    animal19 = Animal(
        type='Cat',
        name='Rachel',
        age='Adult',
        gender='Female',
        breed_id=222,
        description='Look, I have blue eyes, and I sure know I\'m pretty! Very calm and quiet cat, gorgeous coat, very well behaved.',
        shelter_id=4
    )

    db.session.add(animal19)

    #50170204
    animal20 = Animal(
        type='Cat',
        name='Archer',
        age='Adult',
        gender='Male',
        breed_id=222,
        description='Quiet, sweet boy full of purrs. Very calm, affectionate, likes being held.Quiet, sweet boy full of purrs. Very calm, affectionate, likes being held.',
        shelter_id=4
    )

    db.session.add(animal20)

    #50170197
    animal21 = Animal(
        type='Cat',
        name='Sasha',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='Fluffy fluff with little affectionate chirps, loves her chin and face skritched, and walks around like a pretty princess with her tail in the air, occasionally shaking it at you when she\'s very happy. Loves to explore and does not like staying put in one room. So far has not really taken to other cats, but is also not overly aggressive towards them.',
        shelter_id=4
    )

    db.session.add(animal21)

    #50170178
    animal22 = Animal(
        type='Cat',
        name='Brillo',
        age='Adult',
        gender='Male',
        breed_id=173,
        description='I\'m a little baby with an active personality and lots of love!',
        shelter_id=4
    )

    db.session.add(animal22)

    #50170203
    animal23 = Animal(
        type='Cat',
        name='Kai',
        age='Adult',
        gender='Male',
        breed_id=173,
        description='Cuddly, adventurous kitten, loves to snuggle up and purr.',
        shelter_id=4
    )

    db.session.add(animal23)

    #50170180
    animal24 = Animal(
        type='Cat',
        name='Roanna',
        age='Adult',
        gender='Female',
        breed_id=174,
        description='Lovey, sweet, fluff! Loves attention and ear scritches.',
        shelter_id=4
    )

    db.session.add(animal24)


    #animals from shelter MO556
    #50318244
    animal25 = Animal(
        type='Cat',
        name='Arbuckle',
        age='Adult',
        gender='Male',
        breed_id=173,
        description='We don\'t know how they find us but they do! Arbuckle showed up in our neighborhood a few months ago and we started feeding him on our porch. He has a nice warm home out there but he is nervous about coming in our house since we have three cats and three dogs but they walk right past him and he does not mind. He tested negative for FIV/Fleuk. He is a big lump of love and we would like to find him a home of his own. He does have a notched ear.',
        shelter_id=5
    )

    db.session.add(animal25)

    #45957982
    animal26 = Animal(
        type='Cat',
        name='Tilden',
        age='Kitten',
        gender='Male',
        breed_id=173,
        description='Tilden is much an adorable little guy. He is always up for a snuggle and a tustle. Very sweet kitten, loves to give affection and full of energy. He spends his days chillin in the sun and hanging with his littermates Trista and Tertius.',
        shelter_id=5
    )

    db.session.add(animal26)

    #45957974
    animal27 = Animal(
        type='Cat',
        name='Trista',
        age='Kitten',
        gender='Female',
        breed_id=173,
        description='Trisha is such a sweetie. She loves attention. Trisha is ready to find her permanent home',
        shelter_id=5
    )

    db.session.add(animal27)

    #46124576
    animal28 = Animal(
        type='Cat',
        name='Dreamy',
        age='Young',
        gender='Female',
        breed_id=173,
        description='Little miss Dreamy came to us with pneumonia, anemia, unable to walk and was underweight by 2 pounds. She is completely healthy now and loves nothing more than to be held and petted. She loves to play with her toys too. She will be spayed soon, probably in October.',
        shelter_id=5
    )

    db.session.add(animal28)

    #45572309
    animal29 = Animal(
        type='Cat',
        name='Raven',
        age='Kitten',
        gender='Female',
        breed_id=173,
        description='Raven is still very young and loves to get into trouble!',
        shelter_id=5
    )

    db.session.add(animal29)

    #45572231
    animal30 = Animal(
        type='Cat',
        name='Piper',
        age='Kitten',
        gender='Female',
        breed_id=173,
        description='Introducing Piper! She is so adorable and quite a little snuggle bug. Super soft and loves to play! Ready for her furever home! Sher is a Siamese mix: she is cream with light tan spots and seal points. She is FIV/Fleuk negative. Feisty but loving too! Fee includes spy, microchip, rabies and fvrcp vaccines, flea treatment and basic worming.',
        shelter_id=5
    )

    db.session.add(animal30)

    #SKIPPED SEEDING ANIMALS FOR IA233
    #animals from shelter IN200
    #35951366
    animal31 = Animal(
        type='Cat',
        name='Moonflower',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='Moonflower needs to find a very special home! She was originally found as an outside cat, but could no longer remain that way because she had medical issues. Moonflower needs to find a home with someone who can help express her bladder multiple times a day. This is not as hard as it may sound! If you are interested in Moonflower, ask us to teach you how to take care of her! Thank you for your interest in adopting a cat from FACE. The adoption fee is $25 for an adult cat over one year of age. They are all spayed/neutered, fully vaccinated, tested for Feline Leukemia and FIV, and micro-chipped. You can find an adoption application at http://facespayneuter.org/adoptions/cat-adoption-application/ or if you have specific questions you can email us at adopt@faceanimalclinic.org.',
        shelter_id=7
    )

    db.session.add(animal31)

    #51193613
    animal32 = Animal(
        type='Cat',
        name='Pancake',
        age='Adult',
        gender='Male',
        breed_id=173,
        description='Pancake is a sweet and calm boy who has been looking for his forever home for quite a while now. He loves bird watching, getting brushed, treats, chasing the laser pointer and getting all the pets and scritches! Pancake doesn\'t like loud noises, so he would do best in a quiet home. It might take a little while for you to gain his trust, but once you do he will be your best friend. Pancake is around 8-9 years old, neutered, microchipped, vaccinated and tested negative for FIV and FeLV. If you are interested in meeting Pancake please complete our adoption application at https://facespayneuter.org/',
        shelter_id=7
    )

    db.session.add(animal32)

    #49516548
    animal33 = Animal(
        type='Cat',
        name='Bug',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='Bug is a sweet 5 year old girl who loves attention and pets. She is very affectionate and calm and enjoys relaxing with her foster family. She gets along well with the other cats in her foster home and does well with calm, well-behaved dogs. Bug has some allergies that result in fur loss, so she eats a special diet to keep things under control. Bug is spayed, up to date on vaccines, microchipped, and FeLV/FIV negative. If you are interested in adopting Bug please complete our application at facespayneuter.org',
        shelter_id=7
    )

    db.session.add(animal33)

    #47073275
    animal34 = Animal(
        type='Cat',
        name='String Bean Dean',
        age='Adult',
        gender='Male',
        breed_id=173,
        description="Hi there, I'm String Bean Dean, and I'm going to \"be real\" right off the bat. Despite my adorable face, I'm a shy dude who takes a bit before feeling comfortable in my surroundings. You see I was raised on the street, and while you can take the cat out of the street, you can't always take the street out of the cat. I'm a bit of a nervous type and am not a fan of hands coming at my face. However, if you let me, I love to rub all over your head and face, and if you talk nice to me I playfully roll around on the floor. I'm also a fan of toys and love shredding my play mice. And while I like my personal space, as I've become more comfortable with my foster family I let them give me some good rub downs. I'm okay with low energy dogs who respect my space. In terms of cats I can be picky; I would do best as an only cat or in a home with one or two older male cats; in fact, I'm quite fond of my foster mom's older male cat and follow him around like a lost puppy. So essentially, I'm looking for a unicorn adopter--I need someone who understands my quirks and will love me despite of them. I know you're out there so I'm keeping my paws crossed that our paths will cross.",
        shelter_id=7
    )

    db.session.add(animal34)

    #48025850
    animal35 = Animal(
        type='Cat',
        name='Erin',
        age='Adult',
        gender='Female',
        breed_id=173,
        description="Erin is as sweet and cuddly as they come! She loves to hang out with her foster mom and is very affectionate. Erin is 5 years old and is front declawed. She would prefer to be the only pet in the home, but sharing space with one other pet might ok for her. She is spayed, microchipped, tested negative for FeLV and FIV, and vaccinated. If you are interested in adopting please complete our application found at facespayneuter.org",
        shelter_id=7
    )

    db.session.add(animal35)

    #48755177
    animal36 = Animal(
        type='Cat',
        name='Callie',
        age='Adult',
        gender='Female',
        breed_id=173,
        description="Meet Callie! After spending several months with a foster, this beautiful girl is ready to join a wonderful forever family! Callie was a community cat who was displaced when it became unsafe for her to stay where she was. This very sweet, very shy girl has needed lots of time and patience to learn how to feel safe and comfortable in her foster home. Once her trust is won, wow! The wait has totally been worth it! Callie is such a sweet and loving girl. She gives head boops, nose kisses, and full body snuggles, with a purr that can’t be beat! She loves chasing around her plastic spring toys and batting around stuffed mice. She’s a gentle spirit and dislikes lots of commotion. Callie is curious but gets spooked easily, which is why she needs a family that can respect her need for extra patience, space, and understanding. Callie has so much love to give to humans lucky enough to earn her trust! She loves wet food at bedtime, Temptation treats, and all the head scratches and kisses you can give.",
        shelter_id=7
    )

    db.session.add(animal36)


    #44344566
    animal37 = Animal(
        type='Cat',
        name='Chloe',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='Chloe Babe is nominated for "best head boop" and "best super hero mask" here at the FACE Clinic resident awards ceremony. She is a super loving cat and wants nothing more than for you to pet her. She has issues urinating on her own so she is looking for someone that can help express her bladder twice daily. She is very easy to care for and will show you how grateful she is to have a person around. She gets along great with other cats and loves all people. She is a joy to be around and will brighten even the cloudiest day with her sweet purr and radiant cheer. Chloe is spayed/neutered, FELV/FIV tested, microchipped, and up to date on vaccinations. If interested in meeting or adopting this animal please fill out an adoption application at facespayneuter.org.',
        shelter_id=7
    )

    db.session.add(animal37)


    #44344566
    animal38 = Animal(
        type='Cat',
        name='Chloe',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='Chloe Babe is nominated for "best head boop" and "best super hero mask" here at the FACE Clinic resident awards ceremony. She is a super loving cat and wants nothing more than for you to pet her. She has issues urinating on her own so she is looking for someone that can help express her bladder twice daily. She is very easy to care for and will show you how grateful she is to have a person around. She gets along great with other cats and loves all people. She is a joy to be around and will brighten even the cloudiest day with her sweet purr and radiant cheer. Chloe is spayed/neutered, FELV/FIV tested, microchipped, and up to date on vaccinations. If interested in meeting or adopting this animal please fill out an adoption application at facespayneuter.org.',
        shelter_id=7
    )

    db.session.add(animal38)


    #animals from shelter IN45
    #51243994
    animal39 = Animal(
        type='Dog',
        name='Xena',
        age='Young',
        gender='Female',
        breed_id=105,
        description='Everyone say hello to Xena? She is a beautiful 1 year old Lab Mix that would love to be your new bestie?? Although she has lots of energy which is awesome for all of those adventures you have planned this year! She also loves belly rubs, is working on her commands & knows how to "sit." Schedule an appointment to meet Xena! https://warrickhumanesociety.org/adoption-info/',
        shelter_id=8
    )

    db.session.add(animal39)


    #51073558
    animal40 = Animal(
        type='Dog',
        name='Nico',
        age='Young',
        gender='Male',
        breed_id=45,
        description='Meet Nico! Nico is a one year old mix breed (we may see some boxer in there)! He is super friendly with everyone! If you\’re interested in meeting Nico, please submit an application on our website!',
        shelter_id=8
    )

    db.session.add(animal40)


    #50837409
    animal41 = Animal(
        type='Dog',
        name='Jasmine',
        age='Young',
        gender='Female',
        breed_id=45,
        description='Meet Jasmine! Jasmine is a 2-3 year old boxer mix. She is very friendly and very high energy. She would probably do best in a home with another dog that meets her energy level so they can play! If you\'re interested in meeting Jasmine, please submit an application on our website!',
        shelter_id=8
    )

    db.session.add(animal41)

    #animals from shelter TX1920
    #49699018
    animal42 = Animal(
        type='Dog',
        name='Leela',
        age='Adult',
        gender='Female',
        breed_id=83,
        description='You will meet the most wonderful dog you will ever meet. Leela love all human and dogs at all size. Leela was adopted from Harris county a couple of years ago. But the family adopted her and then just keep her outside in the back yard never spend time with her, taking care of her. Leela was heartworm positive when she was adopted but the family never treated her. You would think since she spend all her time alone in the back yard she would be timid when she meet you but she is opposite she yearn for human touch, she yearn for her family to spend time with her, snuggle together, sitting outside enjoyed the sun or just sitting next to each other. When you meet Leela you would not think she is 8 years old. She is still full of energy, love to run chase ball or just sitting outside with you. Leela is German Shepard mix with Norwegian Elkhound. Leela is spay, microchip, up today with all her vaccine and she is being treated for heartworm. Leela is now ready for furever home.',
        shelter_id=9
    )

    db.session.add(animal42)

    #48021772
    animal43 = Animal(
        type='Dog',
        name='Haiti',
        age='Young',
        gender='Female',
        breed_id=150,
        description='Haiti is a 2-year-old Stafford-shire terrier mix with a big heart and a big personality. She loves people, cuddling, playing with toys, and going for walks. Her ideal home is one where she can be the \'only child. Haiti was rescued from the euthanize list from Harris county. She was picking up as a stray and was severe neglect. Haiti is a little ball of fire. She love to play but she is dog selective who she like and dislike, so she would benefit from more behavioral training. Haiti is such a sweet, caring girl who wants nothing more than to be close to her person and cuddle. Spending time with her human is her daily goal. She has proved herself to be quite the love bug, and sometime her face expressions would makes you laugh so hard. She has the biggest smile and the most expressive precious face. Haiti needs someone who can love her, and be patient with her. She is such a great girl. She just needs extra care and love. All her vaccinations up to date, she is spayed and microchip.',
        shelter_id=9
    )

    db.session.add(animal43)

    #48021772
    animal44 = Animal(
        type='Dog',
        name='Leela',
        age='Young',
        gender='Female',
        breed_id=150,
        description='You will meet the most wonderful dog you will ever meet. Leela love all human and dogs at all size. Leela was adopted from Harris county a couple of years ago. But the family adopted her and then just keep her outside in the back yard never spend time with her, taking care of her. Leela was heartworm positive when she was adopted but the family never treated her. You would think since she spend all her time alone in the back yard she would be timid when she meet you but she is opposite she yearn for human touch, she yearn for her family to spend time with her, snuggle together, sitting outside enjoyed the sun or just sitting next to each other. When you meet Leela you would not think she is 8 years old. She is still full of energy, love to run chase ball or just sitting outside with you. Leela is German Shepard mix with Norwegian Elkhound. Leela is spay, microchip, up today with all her vaccine and she is being treated for heartworm. Leela is now ready for furever home.',
        shelter_id=9
    )

    db.session.add(animal44)

    #47323951
    animal45 = Animal(
        type='Dog',
        name='Monte',
        age='Young',
        gender='Male',
        breed_id=6,
        description='Hello to my future fur-ever home! My name is Monte, and I am still super curious about the world around me, but that is because I am still young at heart. My foster mom say I am a sweet boy who also loves to be close to my foster family. Before Angels Four Paws rescue me, I wonder the street everyday looking for foods. Then, I ended up with my current foster because she feed me everyday and I knew she will not harm me. I love to play with my foster brother! If you scratch just behind my ears, that\'s the spot, and I\'ll literally fall to the ground. I used to be very skinny, and they say it is because of my poor diet before I was saved. My foster mom has been taking really good care of me, and now I\'m not skinny, or hungry anymore. My foster mom says I\'m a smart boy and have learned a lot with her help. I learned to trust human again. I\'m so excited to get to meet my forever family.  I heard being adopted was a wonderful thing! I hope I get to meet you soon!!!',
        shelter_id=9
    )

    db.session.add(animal45)

    #46510065
    animal46 = Animal(
        type='Dog',
        name='Shelby',
        age='Puppy',
        gender='Female',
        breed_id=38,
        description='Meet Shelby. She is 2 year old. Shelby needs a patient adopter that will give her some time and training just like her sister. Shelby is more timid then her other sisters and brother. She really needs a family who can really be patience with her give her the time she needs to feel comfortable to come out of her shell. She never bites but will often run from you and hide. She is still learning to be a dog with a human family who will love her and treated her as a part of the family. Shelby scare of human touch all because of her pass. It is so sad to see how scare they are when you try to love on them. She would do best with low key dogs. Sophie needs that special someone willing to work with her, help her gain her confidence and teach her that people can be good and trustworthy. Shelby, her sibling and mom always wondering the street looking for foods until they were rescue by a sweet kind heart elder lady. It break my heart when I gave her a biscuit she hold it not sure what to do with it. She watch my other dogs and seeing them eating it enjoying it, then she start to enjoy her biscuit. But I know their future have chance since the day they come into my rescue. Sophie is now ready for her furever family and being a part of the family as a member not as a piece of property.',
        shelter_id=9
    )

    db.session.add(animal46)

    #43469245
    animal47 = Animal(
        type='Dog',
        name='Zeus',
        age='Young',
        gender='Male',
        breed_id=16,
        description='Zeus and his mate were pick up on the side of the road. I believed they were dump. Nina his mate come in and about to have her puppies. Harris county was trying desperately trying to get help for them. I was contacted by a friend about their situation. I pulled Zeus, Nina and her puppies out of the shelter. Unfortunately, only two of her puppies survive and Nina pass away from serious infection. Zeus is a sweet beautiful boy. He gets along with other dogs, and love to be around human. Zeus love to cuddle and be around you as much as he can. Zeus is neuter, up to day with vaccine and microchip. I am looking for a very special family for Zeus because of his condition.',
        shelter_id=9
    )

    db.session.add(animal47)

    #46508475
    animal48 = Animal(
        type='Dog',
        name='Sophie',
        age='Puppy',
        gender='Female',
        breed_id=18,
        description='Meet Sophie. She is 2 year old. Sophie needs a patient adopter that will give her some time and training. She never bites but will often run from you and hide. She is still learning to be a dog with a human family who will love her and treated her as a part of the family. Sophie does well with other dogs, but she does get overwhelmed with large packs. She would do best with low key dogs. Sophie needs that special someone willing to work with her, help her gain her confidence and teach her that people can be good and trustworthy. Sophie, her sibling and mom always wondering the street looking for foods until they were rescue by a sweet kind heart elder lady. It break my heart when I gave her a biscuit she hold it not sure what to do with it. She watch my other dogs and seeing them eating it enjoying it, then she start to enjoy her biscuit. But I know their future have chance since the day they come into my rescue. Sophie is now ready for her furever family and being a part of the family as a member not as a piece of property.',
        shelter_id=9
    )

    db.session.add(animal48)

    #48104651
    animal49 = Animal(
        type='Dog',
        name='Roadie',
        age='Puppy',
        gender='Male',
        breed_id=18,
        description='Meet Roadie. He is 9 months old. Roadie has three sisters and one brother. He is full of energy and love to play. Just like his siblings Roadie needs a patient adopter that will give him some time and training. He is still learning to be a dog with a human family who will love him and treated him as a part of the family. Roadie never knows how it feels to be pet or to be with a human who will not hurt him in some way. It is really sad puppy should know how it feels to belong or love by human. Roadie does well with other dogs, but he does get overwhelmed with large packs or small yappy dog. Roadie sibling and mom always wondering the street looking for foods until they were rescue by a sweet kind heart elder lady. I know their future have chance since the day they come into my rescue. Roadie is now ready for his furever home , and to build precious memories with his new human family.',
        shelter_id=9
    )

    db.session.add(animal49)

    #49698076
    animal50 = Animal(
        type='Dog',
        name='Colton',
        age='Puppy',
        gender='Male',
        breed_id=18,
        description='Get ready to meet the ball of fire. Colton is full of energy to run up to you kiss you, sitting next to you or on your lap, and then get up and run out chasing squirrel. Colton family give him because they no longer want to take care of him and his siblings. A friend contacted me about Colton and his sibling. The two older dogs were going to be drop off at shelter to have put down since they no longer want to take care of old dogs. And Colton was going to the pound as well since they no longer want to take care of any pets in the family. How do you wake up one day and say HEY I do not want any of my family members anymore because that is who they are family members? Colton is now neuter, up today with vaccines and microchip. Colton is ready for his new family who will love him, taking care of him and Colton will be a part of the family. When Colton first meet you, he will bark his head off but only to say hello. He is not a known bite case he will bark and then come up to you smell you wag his tail and then kiss you to death.',
        shelter_id=9
    )

    db.session.add(animal50)

    #40522316
    animal51 = Animal(
        type='Dog',
        name='Blue',
        age='Young',
        gender='Male',
        breed_id=105,
        description='Hi there! My name is Blue. I have a family before but now I don\'t. I am not sure why one day my dad put me in the back of his truck and drove around town. And when he finally stops he left me at this very scary place. There are so many of us in this building and I was terrified. But soon a nice lady came took me out of that horrible place. I was adopted when I was a pup. We have a good time and I was a good dog but my family dumps me. I am a handsome boy and a good boy but right now I am just still scare but if you give me time I will love you and be your new best friend. He is nervous about all the changes he has been through lately. He wants badly to have a friend to dote on him but earning his trust will take a little time and patience. But blue is ready to be someone\'s best friend. I am shy at first but I will warm up to you. I am ready to find my new furever home won\'t you make my dream come true????? The Angels LOVE me very much and want only the best for me. I am a love and very sweet boy, so won\'t YOU consider taking me into your home forever and ever - making my dream come true! I will lick your face and be your best friend - very willing to please and learn. I have been with Angels Four Paw for over 6 months now and it is time for me to find my own forever family again.',
        shelter_id=9
    )

    db.session.add(animal51)


    #animals from shelter CA458
    #50496617
    animal52 = Animal(
        type='Cat',
        name='Earl Grey',
        age='Adult',
        gender='Male',
        breed_id=173,
        description='My name is Earl Grey. I am a male gray domestic short haired cat. I was born in 2009. I am looking for a new home because my owner passed away. I was already neutered. I am now current on my vaccinations, FELV/FIV tested (negative to both) and microchipped. I was born outside and lived out on the streets for the first two years of my life. I decided street life was not my thing until a kind woman took me in and gave me a wonderful home. Unfortunately, she passed away and her family was going to throw me back outside. That\'s when Second Chance 4 Pets Network stepped in and rescued me. I would do best in YOUR home. I love everyone! I need a human that is willing to hear my life story because I am a huge talker! I am kid tested and mother approved. I am not a fan of dogs, but with proper introduction and patience, I could learn to coexist with a canine. I may be a mature cat, but I still love to play with a good catnip cigar. I am a very affectionate kitty just looking for a warm couch pillow to nap on. Adopt me and find out what a wonderful kitty I really am!',
        shelter_id=10
    )

    db.session.add(animal52)

    #50293810
    animal53 = Animal(
        type='Cat',
        name='Louise',
        age='Kitten',
        gender='Female',
        breed_id=173,
        description='My name is Louise. I am a female black & white domestic medium haired kitten. My siblings (Thelma & Myles) and I were born March 11, 2020. We were rescued from a home in Walkerton, IN. I have been spayed, vaccinated, FELV/FIV tested (negative to both) and microchipped. Like my sister Thelma, I have very distinct markings on my face and have the cutest gray fur tufts behind my ears. I have an affectionate, lovable personality to go along with my looks. I really love belly rubs. Rub my belly and I am yours! I am very playful. I love to climb cat trees and play in the cat tunnels. I also love back rides and will jump on my foster mom\'s back when she is scooping litter or feeding me. Thelma and I go together like cookies and cream. We are inseparable. We play together, snuggle together and get into mischief together! We are a bonded pair and need to be adopted out together.',
        shelter_id=10
    )

    db.session.add(animal53)

    #50654966
    animal54 = Animal(
        type='Cat',
        name='Murr',
        age='Adult',
        gender='Male',
        breed_id=173,
        description='My name is Murr. I am an orange tabby and white domestic short haired cat. My sisters (Bette & Joan) and I were born on October 16, 2019. Cleocatra was our mom. She was pregnant with us when she was rescued from a local kill shelter. I have been neutered, vaccinated, FELV/FIV tested (negative to both) and microchipped. I can be shy at first, but once I am comfortable around you, I can be friendly, lovable and a purr machine. I like snuggling with you at bedtime too. Until I get relaxed around you, I prefer coming up to you. I would do best in a quiet home with no dogs. Active dogs make me very nervous, but I do get along with cats. I would like it if I could be adopted with Norm. We have been together in our foster home and are buddies. I could go to another home as long as there was another easy going cat for companionship and my adopter is willing to be patient with me.',
        shelter_id=10
    )

    db.session.add(animal54)

    #50654785
    animal55 = Animal(
        type='Cat',
        name='Norm',
        age='Adult',
        gender='Male',
        breed_id=173,
        description='My name is Norm. I am a brown tabby and white domestic short haired cat. I was born August 2, 2019. I was rescued from a local kill shelter. I have been neutered, vaccinated, FELV/FIV tested (negative to both) and microchipped. I am the perfect cat. I am lovable, friendly, playful, a purr machine, and a good snuggler. I get along with both cats and dogs too. I love attention and like to supervise especially if you are trying to pay bills or read. I like to get right in the way to help you! I am an all around easy going kitty and should adjust fairly quickly to my new home. It would be cool if I could get adopted out with Murr because we have been together since we were first rescued and are good buddies.',
        shelter_id=10
    )

    db.session.add(animal55)

    #51412287
    animal56 = Animal(
        type='Cat',
        name='Copper',
        age='Adult',
        gender='Male',
        breed_id=174,
        description='My name is Copper. I am a male orange mackerel tabby domestic medium haired cat. My siblings (Mischief, Rowan & Hudson) and I were born March 14, 2018. Mischief and I were adopted out together and returned because of the owners\' health problems. I have been neutered, vaccinated, FELV/FIV tested (negative to both) and microchipped. I can be a real sweetheart who just loves to lay on you. I even sleep with my foster mom at night and snuggle with her. And then there are times when I can be very spunky.. I have been known to have a temper and will let you know when I don\'t want to be messed with. I can even be an ankle biter on occasion. You just have to let me know that I am not the boss of the house! I have a dominant personality and would do best in a home as the only cat or with a very mellow cat. And I can be in a home with dogs. I like dogs and get along well with them. Looking for a cat that is spunky and feisty yet lovable too, consider making me yours.',
        shelter_id=10
    )

    db.session.add(animal56)

    #51047697
    animal57 = Animal(
        type='Cat',
        name='Star',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='My name is Star. I am a female tortoiseshell domestic short haired cat. My sisters (Baby & Sweetie) and I were born September 23, 2018. We were found in the woods behind a home in Schererville, IN. I have been spayed, vaccinated, FELV/FIV tested (negative to both) and microchipped. I am a little shy at first, but once you start petting me, I quickly warm up and want to be your friend. I absolutely love to play, and I really enjoy hanging out on the cat tree in my foster home. I get along with cats and don\'t even mind the dog in my foster home, but I would do better in a home without younger children. I am looking for a home that is relaxed and quiet. A home where I will be loved for the wonderful feline that I am.',
        shelter_id=10
    )

    db.session.add(animal57)

    #50496646
    animal58 = Animal(
        type='Cat',
        name='Barn Mouse',
        age='Kitten',
        gender='Male',
        breed_id=173,
        description='My name is Barn Mouse. I am a male tabby and white domestic short haired kitten. I was born the middle of April 2020. I was born into a feral colony. I became gravely ill after my neuter and almost died. Thank goodness a human came to my rescue and got me the medical attention I needed to get well. I have been neutered, vaccinated, FELV/FIV tested (negative to both) and microchipped. I have had a rough start to life but am starting to trust humans. I prefer kids and women over men. I can be super sweet once I relax and warm up to you. I love chicken treats and canned food. I will follow you around the house until you give me some treats. I can definitely be a beggar mouse! I am a little on the smaller side which could be from being malnourished when I was younger. I am a good eater now and am making up for lost time. If you are patient and willing to give me time to relax and trust you, I could make a good pet. I just need a chance.',
        shelter_id=10
    )

    db.session.add(animal58)

    #50414597
    animal59 = Animal(
        type='Cat',
        name='Lavender',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='My name is Lavender. I am a female brown mackerel tabby domestic short haired cat. I was born in April 2017. I was rescued from a local kill shelter. I have been spayed, vaccinated, FELV/FIV tested (negative to both) and microchipped. I am a real sweetheart, a good girl, and I really enjoy when you rub my head and give me a good kitty massage. I have a quiet, mellow personality and would be perfect for someone looking for a companion cat. Someone to watch TV with or read a book with. I am okay with other cats but like being on my own. I would prefer being either the only cat in the home or with another mellow, laidback kitty. And a home without a dog. Not a fan of dogs. Looking for a cat to share your couch with? A cat that is quiet and mellow and not wild and crazy like a kitten? I would be a great choice',
        shelter_id=10
    )

    db.session.add(animal59)

    #50435750
    animal60 = Animal(
        type='Cat',
        name='Shirley',
        age='Adult',
        gender='Female',
        breed_id=173,
        description='My name is Shirley. I am a female brown mackerel tabby domestic short haired cat. My siblings (Laverne & Carmine) and I were born September 1, 2018. We were rescued as bottle feeders. I have been spayed, vaccinated, FELV/FIV tested (negative to both) and microchipped. I am a friendly girl and people oriented. I enjoy attention and petting time, but I have been known to nip if you overstimulate me. I will let you know when I have had enough. I am okay with other cats and dogs, but I mostly keep to myself. I would be happier being the only pet in the home so I can have your attention all to myself. I am looking for a quiet home to call my own where I can relax and be content. Will you be that home?',
        shelter_id=10
    )

    db.session.add(animal60)
    db.session.commit()



def undo_animals():
    db.session.execute('TRUNCATE animals RESTART IDENTITY CASCADE;')
    db.session.commit()



#for dynamically pulling from api
# class BearerAuth(requests.auth.AuthBase):
#     def __init__(self, token):
#         self.token = token
#     def __call__(self, r):
#         r.headers["authorization"] = "Bearer " + self.token
#         return r

# def animals_id():
#     for i in range(20):
#         response = requests.get('https://api.petfinder.com/v2/animals?type=dog', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6IjhjMDM5NDY1NDNkOTQzYTBjZTRjZWFiY2NmZDEyMTY2YWMzMGI3ZWVlMzBjNDY5ZDYzYWEyNzI0YmQyNmMwM2M0MjViMjYzZjk1MTJiOTQ3IiwiaWF0IjoxNjIwMjI4MzAxLCJuYmYiOjE2MjAyMjgzMDEsImV4cCI6MTYyMDIzMTkwMSwic3ViIjoiIiwic2NvcGVzIjpbXX0.CXv3af2ekjKQ51STwPXjbJwS41hWA4jq97pLjmFDBFzWe_fBcw2FnuqlL37rLXeFo7W5PwiTEXBjaag2O9x8bVTjJ5JoFDiTjtuFpyrkXzV7be0BrNP4DxjtmBZWrEzlj3nz_wZueb7OuvCPtVK1IC-lNImi0lM68LmqtdA6_oQkgqGXZ8OvSW-lYUfbf6GkZou1BID-n_7XgSrJCgPLDyHfn4d3B2NBfhqkkFxTy9TZG2pPqZrzHUUvhXnQa6YSwkW34BA0kp7Fsg95CUlbbtLmen_68uATh6hR5co0lMpchOzJbf2ae_F_Hm0PeYtY4QQose3RESfQFXbQfcPsbg')).json()
#         print(response['animals'][i]['id'])

# print(animals_id())

# listIds = [

# ]


# def seed_products():
#     i = 1
#     while i < len(listIds) -1:
#         response = requests.get(f'https://api.petfinder.com/v2/animals/{listIds[i]}', auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJIYWdiU0ZpcWJ6S3lLeHh5dm1OVTlJV1RSVTZTZDBORFo4WmxRU0h1M2lFQlFRbm83WSIsImp0aSI6IjhjMDM5NDY1NDNkOTQzYTBjZTRjZWFiY2NmZDEyMTY2YWMzMGI3ZWVlMzBjNDY5ZDYzYWEyNzI0YmQyNmMwM2M0MjViMjYzZjk1MTJiOTQ3IiwiaWF0IjoxNjIwMjI4MzAxLCJuYmYiOjE2MjAyMjgzMDEsImV4cCI6MTYyMDIzMTkwMSwic3ViIjoiIiwic2NvcGVzIjpbXX0.CXv3af2ekjKQ51STwPXjbJwS41hWA4jq97pLjmFDBFzWe_fBcw2FnuqlL37rLXeFo7W5PwiTEXBjaag2O9x8bVTjJ5JoFDiTjtuFpyrkXzV7be0BrNP4DxjtmBZWrEzlj3nz_wZueb7OuvCPtVK1IC-lNImi0lM68LmqtdA6_oQkgqGXZ8OvSW-lYUfbf6GkZou1BID-n_7XgSrJCgPLDyHfn4d3B2NBfhqkkFxTy9TZG2pPqZrzHUUvhXnQa6YSwkW34BA0kp7Fsg95CUlbbtLmen_68uATh6hR5co0lMpchOzJbf2ae_F_Hm0PeYtY4QQose3RESfQFXbQfcPsbg')).json()
#         animal = response['animal']
#         for item in animal:
#             demo = Animal(
#                 name=item["name"],
#                 store_id=(i/20)+1,
#                 price=item["price"],
#                 quantity=item["quantity"],
#                 description=item["description"],
#             )
#             db.session.add(demo)
#         i += 1
#     db.session.commit()
