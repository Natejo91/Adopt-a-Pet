from app.models import db, Breed

breeds = [
  {
    "bred_for": "Small rodent hunting, lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "9 - 11.5",
      "metric": "23 - 29"
    },
    "id": 1,
    "image": {
      "height": 1199,
      "id": "BJa4kxc4X",
      "url": "https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg",
      "width": 1600
    },
    "life_span": "10 - 12 years",
    "name": "Affenpinscher",
    "origin": "Germany, France",
    "reference_image_id": "BJa4kxc4X",
    "temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
    "weight": {
      "imperial": "6 - 13",
      "metric": "3 - 6"
    }
  },
  {
    "bred_for": "Coursing and hunting",
    "breed_group": "Hound",
    "country_code": "AG",
    "height": {
      "imperial": "25 - 27",
      "metric": "64 - 69"
    },
    "id": 2,
    "image": {
      "height": 380,
      "id": "hMyT4CDXR",
      "url": "https://cdn2.thedogapi.com/images/hMyT4CDXR.jpg",
      "width": 606
    },
    "life_span": "10 - 13 years",
    "name": "Afghan Hound",
    "origin": "Afghanistan, Iran, Pakistan",
    "reference_image_id": "hMyT4CDXR",
    "temperament": "Aloof, Clownish, Dignified, Independent, Happy",
    "weight": {
      "imperial": "50 - 60",
      "metric": "23 - 27"
    }
  },
  {
    "bred_for": "A wild pack animal",
    "height": {
      "imperial": "30",
      "metric": "76"
    },
    "id": 3,
    "image": {
      "height": 335,
      "id": "rkiByec47",
      "url": "https://cdn2.thedogapi.com/images/rkiByec47.jpg",
      "width": 500
    },
    "life_span": "11 years",
    "name": "African Hunting Dog",
    "origin": "",
    "reference_image_id": "rkiByec47",
    "temperament": "Wild, Hardworking, Dutiful",
    "weight": {
      "imperial": "44 - 66",
      "metric": "20 - 30"
    }
  },
  {
    "bred_for": "Badger, otter hunting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "21 - 23",
      "metric": "53 - 58"
    },
    "id": 4,
    "image": {
      "height": 430,
      "id": "1-7cgoZSh",
      "url": "https://cdn2.thedogapi.com/images/1-7cgoZSh.jpg",
      "width": 645
    },
    "life_span": "10 - 13 years",
    "name": "Airedale Terrier",
    "origin": "United Kingdom, England",
    "reference_image_id": "1-7cgoZSh",
    "temperament": "Outgoing, Friendly, Alert, Confident, Intelligent, Courageous",
    "weight": {
      "imperial": "40 - 65",
      "metric": "18 - 29"
    }
  },
  {
    "bred_for": "Sheep guarding",
    "breed_group": "Working",
    "height": {
      "imperial": "28 - 34",
      "metric": "71 - 86"
    },
    "id": 5,
    "image": {
      "height": 471,
      "id": "26pHT3Qk7",
      "url": "https://cdn2.thedogapi.com/images/26pHT3Qk7.jpg",
      "width": 600
    },
    "life_span": "10 - 12 years",
    "name": "Akbash Dog",
    "origin": "",
    "reference_image_id": "26pHT3Qk7",
    "temperament": "Loyal, Independent, Intelligent, Brave",
    "weight": {
      "imperial": "90 - 120",
      "metric": "41 - 54"
    }
  },
  {
    "bred_for": "Hunting bears",
    "breed_group": "Working",
    "height": {
      "imperial": "24 - 28",
      "metric": "61 - 71"
    },
    "id": 6,
    "image": {
      "height": 853,
      "id": "BFRYBufpm",
      "url": "https://cdn2.thedogapi.com/images/BFRYBufpm.jpg",
      "width": 1280
    },
    "life_span": "10 - 14 years",
    "name": "Akita",
    "reference_image_id": "BFRYBufpm",
    "temperament": "Docile, Alert, Responsive, Dignified, Composed, Friendly, Receptive, Faithful, Courageous",
    "weight": {
      "imperial": "65 - 115",
      "metric": "29 - 52"
    }
  },
  {
    "bred_for": "Guarding",
    "breed_group": "Mixed",
    "description": "The Alapaha Blue Blood Bulldog is a well-developed, exaggerated bulldog with a broad head and natural drop ears. The prominent muzzle is covered by loose upper lips. The prominent eyes are set well apart. The Alapaha's coat is relatively short and fairly stiff. Preferred colors are blue merle, brown merle, or red merle all trimmed in white or chocolate and white. Also preferred are the glass eyes (blue) or marble eyes (brown and blue mixed in a single eye). The ears and tail are never trimmed or docked. The body is sturdy and very muscular. The well-muscled hips are narrower than the chest. The straight back is as long as the dog is high at the shoulders. The dewclaws are never removed and the feet are cat-like.",
    "height": {
      "imperial": "18 - 24",
      "metric": "46 - 61"
    },
    "history": "",
    "id": 7,
    "image": {
      "height": 2065,
      "id": "33mJ-V3RX",
      "url": "https://cdn2.thedogapi.com/images/33mJ-V3RX.jpg",
      "width": 1828
    },
    "life_span": "12 - 13 years",
    "name": "Alapaha Blue Blood Bulldog",
    "reference_image_id": "33mJ-V3RX",
    "temperament": "Loving, Protective, Trainable, Dutiful, Responsible",
    "weight": {
      "imperial": "55 - 90",
      "metric": "25 - 41"
    }
  },
  {
    "bred_for": "Sled pulling",
    "breed_group": "Mixed",
    "height": {
      "imperial": "23 - 26",
      "metric": "58 - 66"
    },
    "id": 8,
    "image": {
      "height": 500,
      "id": "-HgpNnGXl",
      "url": "https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg",
      "width": 500
    },
    "life_span": "10 - 13 years",
    "name": "Alaskan Husky",
    "reference_image_id": "-HgpNnGXl",
    "temperament": "Friendly, Energetic, Loyal, Gentle, Confident",
    "weight": {
      "imperial": "38 - 50",
      "metric": "17 - 23"
    }
  },
  {
    "bred_for": "Hauling heavy freight, Sled pulling",
    "breed_group": "Working",
    "height": {
      "imperial": "23 - 25",
      "metric": "58 - 64"
    },
    "id": 9,
    "image": {
      "height": 769,
      "id": "dW5UucTIW",
      "url": "https://cdn2.thedogapi.com/images/dW5UucTIW.jpg",
      "width": 1023
    },
    "life_span": "12 - 15 years",
    "name": "Alaskan Malamute",
    "reference_image_id": "dW5UucTIW",
    "temperament": "Friendly, Affectionate, Devoted, Loyal, Dignified, Playful",
    "weight": {
      "imperial": "65 - 100",
      "metric": "29 - 45"
    }
  },
  {
    "breed_group": "Working",
    "height": {
      "imperial": "22 - 27",
      "metric": "56 - 69"
    },
    "id": 10,
    "image": {
      "height": 1377,
      "id": "pk1AAdloG",
      "url": "https://cdn2.thedogapi.com/images/pk1AAdloG.jpg",
      "width": 1669
    },
    "life_span": "10 - 12 years",
    "name": "American Bulldog",
    "reference_image_id": "pk1AAdloG",
    "temperament": "Friendly, Assertive, Energetic, Loyal, Gentle, Confident, Dominant",
    "weight": {
      "imperial": "60 - 120",
      "metric": "27 - 54"
    }
  },
  {
    "bred_for": "Family companion dog",
    "breed_group": "",
    "country_code": "US",
    "height": {
      "imperial": "14 - 17",
      "metric": "36 - 43"
    },
    "id": 11,
    "image": {
      "height": 683,
      "id": "sqQJDtbpY",
      "url": "https://cdn2.thedogapi.com/images/sqQJDtbpY.jpg",
      "width": 1024
    },
    "life_span": "8 – 15 years",
    "name": "American Bully",
    "reference_image_id": "sqQJDtbpY",
    "temperament": "Strong Willed, Stubborn, Friendly, Clownish, Affectionate, Loyal, Obedient, Intelligent, Courageous",
    "weight": {
      "imperial": "30 - 150",
      "metric": "14 - 68"
    }
  },
  {
    "bred_for": "Circus performer",
    "breed_group": "Non-Sporting",
    "country_code": "US",
    "height": {
      "imperial": "15 - 19",
      "metric": "38 - 48"
    },
    "id": 12,
    "image": {
      "height": 802,
      "id": "Bymjyec4m",
      "url": "https://cdn2.thedogapi.com/images/Bymjyec4m.jpg",
      "width": 1000
    },
    "life_span": "12 - 15 years",
    "name": "American Eskimo Dog",
    "reference_image_id": "Bymjyec4m",
    "temperament": "Friendly, Alert, Reserved, Intelligent, Protective",
    "weight": {
      "imperial": "20 - 40",
      "metric": "9 - 18"
    }
  },
  {
    "bred_for": "Companionship",
    "country_code": "US",
    "height": {
      "imperial": "9 - 12",
      "metric": "23 - 30"
    },
    "id": 13,
    "image": {
      "height": 487,
      "id": "_gn8GLrE6",
      "url": "https://cdn2.thedogapi.com/images/_gn8GLrE6.jpg",
      "width": 730
    },
    "life_span": "13 – 15 years",
    "name": "American Eskimo Dog (Miniature)",
    "reference_image_id": "_gn8GLrE6",
    "temperament": "Friendly, Alert, Reserved, Intelligent, Protective",
    "weight": {
      "imperial": "7 - 10",
      "metric": "3 - 5"
    }
  },
  {
    "bred_for": "Fox hunting, scent hound",
    "breed_group": "Hound",
    "country_code": "US",
    "height": {
      "imperial": "21 - 28",
      "metric": "53 - 71"
    },
    "id": 14,
    "image": {
      "height": 2400,
      "id": "S14n1x9NQ",
      "url": "https://cdn2.thedogapi.com/images/S14n1x9NQ.jpg",
      "width": 3000
    },
    "life_span": "8 - 15 years",
    "name": "American Foxhound",
    "reference_image_id": "S14n1x9NQ",
    "temperament": "Kind, Sweet-Tempered, Loyal, Independent, Intelligent, Loving",
    "weight": {
      "imperial": "65 - 75",
      "metric": "29 - 34"
    }
  },
  {
    "bred_for": "Fighting",
    "breed_group": "Terrier",
    "country_code": "US",
    "height": {
      "imperial": "17 - 21",
      "metric": "43 - 53"
    },
    "id": 15,
    "image": {
      "height": 244,
      "id": "HkC31gcNm",
      "url": "https://cdn2.thedogapi.com/images/HkC31gcNm.png",
      "width": 300
    },
    "life_span": "10 - 15 years",
    "name": "American Pit Bull Terrier",
    "reference_image_id": "HkC31gcNm",
    "temperament": "Strong Willed, Stubborn, Friendly, Clownish, Affectionate, Loyal, Obedient, Intelligent, Courageous",
    "weight": {
      "imperial": "30 - 60",
      "metric": "14 - 27"
    }
  },
  {
    "bred_for": "",
    "breed_group": "Terrier",
    "country_code": "US",
    "height": {
      "imperial": "17 - 19",
      "metric": "43 - 48"
    },
    "id": 16,
    "image": {
      "height": 500,
      "id": "rJIakgc4m",
      "url": "https://cdn2.thedogapi.com/images/rJIakgc4m.jpg",
      "width": 357
    },
    "life_span": "12 - 15 years",
    "name": "American Staffordshire Terrier",
    "reference_image_id": "rJIakgc4m",
    "temperament": "Tenacious, Friendly, Devoted, Loyal, Attentive, Courageous",
    "weight": {
      "imperial": "50 - 60",
      "metric": "23 - 27"
    }
  },
  {
    "bred_for": "Bird flushing and retrieving",
    "breed_group": "Sporting",
    "country_code": "US",
    "height": {
      "imperial": "15 - 18",
      "metric": "38 - 46"
    },
    "id": 17,
    "image": {
      "height": 1264,
      "id": "SkmRJl9VQ",
      "url": "https://cdn2.thedogapi.com/images/SkmRJl9VQ.jpg",
      "width": 1600
    },
    "life_span": "10 - 12 years",
    "name": "American Water Spaniel",
    "reference_image_id": "SkmRJl9VQ",
    "temperament": "Friendly, Energetic, Obedient, Intelligent, Protective, Trainable",
    "weight": {
      "imperial": "25 - 45",
      "metric": "11 - 20"
    }
  },
  {
    "bred_for": "Livestock herding",
    "breed_group": "Working",
    "height": {
      "imperial": "27 - 29",
      "metric": "69 - 74"
    },
    "id": 18,
    "image": {
      "height": 1131,
      "id": "BJT0Jx5Nm",
      "url": "https://cdn2.thedogapi.com/images/BJT0Jx5Nm.jpg",
      "width": 1216
    },
    "life_span": "11 - 13 years",
    "name": "Anatolian Shepherd Dog",
    "reference_image_id": "BJT0Jx5Nm",
    "temperament": "Steady, Bold, Independent, Confident, Intelligent, Proud",
    "weight": {
      "imperial": "80 - 150",
      "metric": "36 - 68"
    }
  },
  {
    "bred_for": "Herding livestock, pulling carts, and guarding the farm",
    "height": {
      "imperial": "20 - 22",
      "metric": "51 - 56"
    },
    "id": 19,
    "image": {
      "height": 600,
      "id": "HkNkxlqEX",
      "url": "https://cdn2.thedogapi.com/images/HkNkxlqEX.jpg",
      "width": 400
    },
    "life_span": "12 – 14 years",
    "name": "Appenzeller Sennenhund",
    "reference_image_id": "HkNkxlqEX",
    "temperament": "Reliable, Fearless, Energetic, Lively, Self-assured",
    "weight": {
      "imperial": "48 - 55",
      "metric": "22 - 25"
    }
  },
  {
    "bred_for": "Cattle herding, herding trials",
    "breed_group": "Herding",
    "country_code": "AU",
    "height": {
      "imperial": "17 - 20",
      "metric": "43 - 51"
    },
    "id": 21,
    "image": {
      "height": 850,
      "id": "IBkYVm4v1",
      "url": "https://cdn2.thedogapi.com/images/IBkYVm4v1.jpg",
      "width": 736
    },
    "life_span": "12 - 14 years",
    "name": "Australian Cattle Dog",
    "reference_image_id": "IBkYVm4v1",
    "temperament": "Cautious, Energetic, Loyal, Obedient, Protective, Brave",
    "weight": {
      "imperial": "44 - 62",
      "metric": "20 - 28"
    }
  },
  {
    "bred_for": "Farm dog, Cattle herding",
    "breed_group": "Herding",
    "country_code": "AU",
    "height": {
      "imperial": "17 - 20",
      "metric": "43 - 51"
    },
    "id": 22,
    "image": {
      "height": 533,
      "id": "Hyq1ge9VQ",
      "url": "https://cdn2.thedogapi.com/images/Hyq1ge9VQ.jpg",
      "width": 800
    },
    "life_span": "10 - 13 years",
    "name": "Australian Kelpie",
    "reference_image_id": "Hyq1ge9VQ",
    "temperament": "Friendly, Energetic, Alert, Loyal, Intelligent, Eager",
    "weight": {
      "imperial": "31 - 46",
      "metric": "14 - 21"
    }
  },
  {
    "bred_for": "Sheep herding",
    "breed_group": "Herding",
    "country_code": "AU",
    "height": {
      "imperial": "18 - 23",
      "metric": "46 - 58"
    },
    "id": 23,
    "image": {
      "height": 733,
      "id": "B1-llgq4m",
      "url": "https://cdn2.thedogapi.com/images/B1-llgq4m.jpg",
      "width": 1200
    },
    "life_span": "12 - 16 years",
    "name": "Australian Shepherd",
    "reference_image_id": "B1-llgq4m",
    "temperament": "Good-natured, Affectionate, Intelligent, Active, Protective",
    "weight": {
      "imperial": "35 - 65",
      "metric": "16 - 29"
    }
  },
  {
    "bred_for": "Cattle herdering, hunting snakes and rodents",
    "breed_group": "Terrier",
    "country_code": "AU",
    "height": {
      "imperial": "10 - 11",
      "metric": "25 - 28"
    },
    "id": 24,
    "image": {
      "height": 720,
      "id": "r1Ylge5Vm",
      "url": "https://cdn2.thedogapi.com/images/r1Ylge5Vm.jpg",
      "width": 1081
    },
    "life_span": "15 years",
    "name": "Australian Terrier",
    "reference_image_id": "r1Ylge5Vm",
    "temperament": "Spirited, Alert, Loyal, Companionable, Even Tempered, Courageous",
    "weight": {
      "imperial": "14 - 16",
      "metric": "6 - 7"
    }
  },
  {
    "bred_for": "Livestock guardian, hunting",
    "breed_group": "Hound",
    "height": {
      "imperial": "23 - 29",
      "metric": "58 - 74"
    },
    "id": 25,
    "image": {
      "height": 768,
      "id": "SkvZgx94m",
      "url": "https://cdn2.thedogapi.com/images/SkvZgx94m.jpg",
      "width": 1024
    },
    "life_span": "10 - 13 years",
    "name": "Azawakh",
    "reference_image_id": "SkvZgx94m",
    "temperament": "Aloof, Affectionate, Attentive, Rugged, Fierce, Refined",
    "weight": {
      "imperial": "33 - 55",
      "metric": "15 - 25"
    }
  },
  {
    "bred_for": "Hunting water game",
    "height": {
      "imperial": "20 - 26",
      "metric": "51 - 66"
    },
    "id": 26,
    "image": {
      "height": 1280,
      "id": "HyWGexcVQ",
      "url": "https://cdn2.thedogapi.com/images/HyWGexcVQ.jpg",
      "width": 853
    },
    "life_span": "13 – 15 years",
    "name": "Barbet",
    "reference_image_id": "HyWGexcVQ",
    "temperament": "Obedient, Companionable, Intelligent, Joyful",
    "weight": {
      "imperial": "40 - 65",
      "metric": "18 - 29"
    }
  },
  {
    "bred_for": "Hunting",
    "breed_group": "Hound",
    "height": {
      "imperial": "16 - 17",
      "metric": "41 - 43"
    },
    "id": 28,
    "image": {
      "height": 493,
      "id": "H1dGlxqNQ",
      "url": "https://cdn2.thedogapi.com/images/H1dGlxqNQ.jpg",
      "width": 740
    },
    "life_span": "10 - 12 years",
    "name": "Basenji",
    "reference_image_id": "H1dGlxqNQ",
    "temperament": "Affectionate, Energetic, Alert, Curious, Playful, Intelligent",
    "weight": {
      "imperial": "22 - 24",
      "metric": "10 - 11"
    }
  },
  {
    "bred_for": "Hunting on foot.",
    "breed_group": "Hound",
    "height": {
      "imperial": "13 - 15",
      "metric": "33 - 38"
    },
    "id": 29,
    "image": {
      "height": 853,
      "id": "BkMQll94X",
      "url": "https://cdn2.thedogapi.com/images/BkMQll94X.jpg",
      "width": 1280
    },
    "life_span": "10 - 14 years",
    "name": "Basset Bleu de Gascogne",
    "reference_image_id": "BkMQll94X",
    "temperament": "Affectionate, Lively, Agile, Curious, Happy, Active",
    "weight": {
      "imperial": "35 - 40",
      "metric": "16 - 18"
    }
  },
  {
    "bred_for": "Hunting by scent",
    "breed_group": "Hound",
    "height": {
      "imperial": "14",
      "metric": "36"
    },
    "id": 30,
    "image": {
      "height": 640,
      "id": "Sy57xx9EX",
      "url": "https://cdn2.thedogapi.com/images/Sy57xx9EX.jpg",
      "width": 1024
    },
    "life_span": "12 - 15 years",
    "name": "Basset Hound",
    "reference_image_id": "Sy57xx9EX",
    "temperament": "Tenacious, Friendly, Affectionate, Devoted, Sweet-Tempered, Gentle",
    "weight": {
      "imperial": "50 - 65",
      "metric": "23 - 29"
    }
  },
  {
    "bred_for": "Rabbit, hare hunting",
    "breed_group": "Hound",
    "height": {
      "imperial": "13 - 15",
      "metric": "33 - 38"
    },
    "id": 31,
    "image": {
      "height": 667,
      "id": "Syd4xxqEm",
      "url": "https://cdn2.thedogapi.com/images/Syd4xxqEm.jpg",
      "width": 1000
    },
    "life_span": "13 - 16 years",
    "name": "Beagle",
    "reference_image_id": "Syd4xxqEm",
    "temperament": "Amiable, Even Tempered, Excitable, Determined, Gentle, Intelligent",
    "weight": {
      "imperial": "20 - 35",
      "metric": "9 - 16"
    }
  },
  {
    "bred_for": "Sheep herding",
    "breed_group": "Herding",
    "height": {
      "imperial": "20 - 22",
      "metric": "51 - 56"
    },
    "id": 32,
    "image": {
      "height": 733,
      "id": "A09F4c1qP",
      "url": "https://cdn2.thedogapi.com/images/A09F4c1qP.jpg",
      "width": 733
    },
    "life_span": "12 - 14 years",
    "name": "Bearded Collie",
    "reference_image_id": "A09F4c1qP",
    "temperament": "Self-confidence, Hardy, Lively, Alert, Intelligent, Active",
    "weight": {
      "imperial": "45 - 55",
      "metric": "20 - 25"
    }
  },
  {
    "bred_for": "Boar herding, hunting, guarding",
    "breed_group": "Herding",
    "height": {
      "imperial": "24 - 27.5",
      "metric": "61 - 70"
    },
    "id": 33,
    "image": {
      "height": 563,
      "id": "HJQ8ge5V7",
      "url": "https://cdn2.thedogapi.com/images/HJQ8ge5V7.jpg",
      "width": 720
    },
    "life_span": "10 - 12 years",
    "name": "Beauceron",
    "reference_image_id": "HJQ8ge5V7",
    "temperament": "Fearless, Friendly, Intelligent, Protective, Calm",
    "weight": {
      "imperial": "80 - 110",
      "metric": "36 - 50"
    }
  },
  {
    "bred_for": "Killing rat, badger, other vermin",
    "breed_group": "Terrier",
    "height": {
      "imperial": "15 - 16",
      "metric": "38 - 41"
    },
    "id": 34,
    "image": {
      "height": 531,
      "id": "ByK8gx947",
      "url": "https://cdn2.thedogapi.com/images/ByK8gx947.jpg",
      "width": 804
    },
    "life_span": "14 - 16 years",
    "name": "Bedlington Terrier",
    "reference_image_id": "ByK8gx947",
    "temperament": "Affectionate, Spirited, Intelligent, Good-tempered",
    "weight": {
      "imperial": "17 - 23",
      "metric": "8 - 10"
    }
  },
  {
    "bred_for": "Stock herding",
    "breed_group": "Herding",
    "height": {
      "imperial": "22 - 26",
      "metric": "56 - 66"
    },
    "id": 36,
    "image": {
      "height": 453,
      "id": "r1f_ll5VX",
      "url": "https://cdn2.thedogapi.com/images/r1f_ll5VX.jpg",
      "width": 604
    },
    "life_span": "12 - 14 years",
    "name": "Belgian Malinois",
    "reference_image_id": "r1f_ll5VX",
    "temperament": "Watchful, Alert, Stubborn, Friendly, Confident, Hard-working, Active, Protective",
    "weight": {
      "imperial": "40 - 80",
      "metric": "18 - 36"
    }
  },
  {
    "bred_for": "Guarding, Drafting, Police work.",
    "breed_group": "Herding",
    "height": {
      "imperial": "22 - 26",
      "metric": "56 - 66"
    },
    "id": 38,
    "image": {
      "height": 380,
      "id": "B1KdxlcNX",
      "url": "https://cdn2.thedogapi.com/images/B1KdxlcNX.jpg",
      "width": 645
    },
    "life_span": "10 - 12 years",
    "name": "Belgian Tervuren",
    "reference_image_id": "B1KdxlcNX",
    "temperament": "Energetic, Alert, Loyal, Intelligent, Attentive, Protective",
    "weight": {
      "imperial": "40 - 65",
      "metric": "18 - 29"
    }
  },
  {
    "bred_for": "Draft work",
    "breed_group": "Working",
    "height": {
      "imperial": "23 - 27.5",
      "metric": "58 - 70"
    },
    "id": 41,
    "image": {
      "height": 427,
      "id": "S1fFlx5Em",
      "url": "https://cdn2.thedogapi.com/images/S1fFlx5Em.jpg",
      "width": 640
    },
    "life_span": "7 - 10 years",
    "name": "Bernese Mountain Dog",
    "reference_image_id": "S1fFlx5Em",
    "temperament": "Affectionate, Loyal, Intelligent, Faithful",
    "weight": {
      "imperial": "65 - 120",
      "metric": "29 - 54"
    }
  },
  {
    "bred_for": "Companion",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "9.5 - 11.5",
      "metric": "24 - 29"
    },
    "id": 42,
    "image": {
      "height": 360,
      "id": "HkuYlxqEQ",
      "url": "https://cdn2.thedogapi.com/images/HkuYlxqEQ.jpg",
      "width": 480
    },
    "life_span": "15 years",
    "name": "Bichon Frise",
    "reference_image_id": "HkuYlxqEQ",
    "temperament": "Feisty, Affectionate, Cheerful, Playful, Gentle, Sensitive",
    "weight": {
      "imperial": "10 - 18",
      "metric": "5 - 8"
    }
  },
  {
    "bred_for": "Hunting raccoons, night hunting",
    "breed_group": "Hound",
    "height": {
      "imperial": "23 - 27",
      "metric": "58 - 69"
    },
    "id": 43,
    "image": {
      "height": 380,
      "id": "HJAFgxcNQ",
      "url": "https://cdn2.thedogapi.com/images/HJAFgxcNQ.jpg",
      "width": 556
    },
    "life_span": "10 - 12 years",
    "name": "Black and Tan Coonhound",
    "reference_image_id": "HJAFgxcNQ",
    "temperament": "Easygoing, Gentle, Adaptable, Trusting, Even Tempered, Lovable",
    "weight": {
      "imperial": "65 - 100",
      "metric": "29 - 45"
    }
  },
  {
    "bred_for": "Trailing",
    "breed_group": "Hound",
    "height": {
      "imperial": "23 - 27",
      "metric": "58 - 69"
    },
    "id": 45,
    "image": {
      "height": 600,
      "id": "Skdcgx9VX",
      "url": "https://cdn2.thedogapi.com/images/Skdcgx9VX.jpg",
      "width": 586
    },
    "life_span": "8 - 10 years",
    "name": "Bloodhound",
    "reference_image_id": "Skdcgx9VX",
    "temperament": "Stubborn, Affectionate, Gentle, Even Tempered",
    "weight": {
      "imperial": "80 - 110",
      "metric": "36 - 50"
    }
  },
  {
    "bred_for": "Hunting with a superior sense of smell.",
    "breed_group": "Hound",
    "height": {
      "imperial": "21 - 27",
      "metric": "53 - 69"
    },
    "id": 47,
    "image": {
      "height": 599,
      "id": "rJxieg9VQ",
      "url": "https://cdn2.thedogapi.com/images/rJxieg9VQ.jpg",
      "width": 731
    },
    "life_span": "12 - 14 years",
    "name": "Bluetick Coonhound",
    "reference_image_id": "rJxieg9VQ",
    "temperament": "Friendly, Intelligent, Active",
    "weight": {
      "imperial": "45 - 80",
      "metric": "20 - 36"
    }
  },
  {
    "bred_for": "Guarding the homestead, farm work.",
    "breed_group": "Working",
    "height": {
      "imperial": "22 - 27",
      "metric": "56 - 69"
    },
    "id": 48,
    "image": {
      "height": 669,
      "id": "HyOjge5Vm",
      "url": "https://cdn2.thedogapi.com/images/HyOjge5Vm.jpg",
      "width": 1200
    },
    "life_span": "10 - 12 years",
    "name": "Boerboel",
    "reference_image_id": "HyOjge5Vm",
    "temperament": "Obedient, Confident, Intelligent, Dominant, Territorial",
    "weight": {
      "imperial": "110 - 200",
      "metric": "50 - 91"
    }
  },
  {
    "bred_for": "Sheep herder",
    "breed_group": "Herding",
    "height": {
      "imperial": "18 - 22",
      "metric": "46 - 56"
    },
    "id": 50,
    "image": {
      "height": 1080,
      "id": "sGQvQUpsp",
      "url": "https://cdn2.thedogapi.com/images/sGQvQUpsp.jpg",
      "width": 1080
    },
    "life_span": "12 - 16 years",
    "name": "Border Collie",
    "reference_image_id": "sGQvQUpsp",
    "temperament": "Tenacious, Keen, Energetic, Responsive, Alert, Intelligent",
    "weight": {
      "imperial": "30 - 45",
      "metric": "14 - 20"
    }
  },
  {
    "bred_for": "Fox bolting, ratting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "11 - 16",
      "metric": "28 - 41"
    },
    "id": 51,
    "image": {
      "height": 450,
      "id": "HJOpge9Em",
      "url": "https://cdn2.thedogapi.com/images/HJOpge9Em.jpg",
      "width": 674
    },
    "life_span": "12 - 14 years",
    "name": "Border Terrier",
    "reference_image_id": "HJOpge9Em",
    "temperament": "Fearless, Affectionate, Alert, Obedient, Intelligent, Even Tempered",
    "weight": {
      "imperial": "11.5 - 15.5",
      "metric": "5 - 7"
    }
  },
  {
    "bred_for": "Ratting, Companionship",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "16 - 17",
      "metric": "41 - 43"
    },
    "id": 53,
    "image": {
      "height": 673,
      "id": "rkZRggqVX",
      "url": "https://cdn2.thedogapi.com/images/rkZRggqVX.jpg",
      "width": 1010
    },
    "life_span": "11 - 13 years",
    "name": "Boston Terrier",
    "reference_image_id": "rkZRggqVX",
    "temperament": "Friendly, Lively, Intelligent",
    "weight": {
      "imperial": "10 - 25",
      "metric": "5 - 11"
    }
  },
  {
    "bred_for": "Cattle herding",
    "breed_group": "Herding",
    "height": {
      "imperial": "23.5 - 27.5",
      "metric": "60 - 70"
    },
    "id": 54,
    "image": {
      "height": 454,
      "id": "Byd0xl5VX",
      "url": "https://cdn2.thedogapi.com/images/Byd0xl5VX.jpg",
      "width": 680
    },
    "life_span": "10 - 15 years",
    "name": "Bouvier des Flandres",
    "reference_image_id": "Byd0xl5VX",
    "temperament": "Protective, Loyal, Gentle, Intelligent, Familial, Rational",
    "weight": {
      "imperial": "70 - 110",
      "metric": "32 - 50"
    }
  },
  {
    "bred_for": "Bull-baiting, guardian",
    "breed_group": "Working",
    "height": {
      "imperial": "21.5 - 25",
      "metric": "55 - 64"
    },
    "id": 55,
    "image": {
      "height": 430,
      "id": "ry1kWe5VQ",
      "url": "https://cdn2.thedogapi.com/images/ry1kWe5VQ.jpg",
      "width": 645
    },
    "life_span": "8 - 10 years",
    "name": "Boxer",
    "reference_image_id": "ry1kWe5VQ",
    "temperament": "Devoted, Fearless, Friendly, Cheerful, Energetic, Loyal, Playful, Confident, Intelligent, Bright, Brave, Calm",
    "weight": {
      "imperial": "50 - 70",
      "metric": "23 - 32"
    }
  },
  {
    "bred_for": "Turkey retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "14 - 18",
      "metric": "36 - 46"
    },
    "id": 56,
    "image": {
      "height": 634,
      "id": "ryHJZlcNX",
      "url": "https://cdn2.thedogapi.com/images/ryHJZlcNX.jpg",
      "width": 577
    },
    "life_span": "10 - 14 years",
    "name": "Boykin Spaniel",
    "reference_image_id": "ryHJZlcNX",
    "temperament": "Friendly, Energetic, Companionable, Intelligent, Eager, Trainable",
    "weight": {
      "imperial": "25 - 40",
      "metric": "11 - 18"
    }
  },
  {
    "bred_for": "Versatile gun dog",
    "breed_group": "Sporting",
    "height": {
      "imperial": "21.5 - 26.5",
      "metric": "55 - 67"
    },
    "id": 57,
    "image": {
      "height": 505,
      "id": "S13yZg5VQ",
      "url": "https://cdn2.thedogapi.com/images/S13yZg5VQ.jpg",
      "width": 750
    },
    "life_span": "10 - 12 years",
    "name": "Bracco Italiano",
    "reference_image_id": "S13yZg5VQ",
    "temperament": "Stubborn, Affectionate, Loyal, Playful, Companionable, Trainable",
    "weight": {
      "imperial": "55 - 88",
      "metric": "25 - 40"
    }
  },
  {
    "bred_for": "Herding, guarding sheep",
    "breed_group": "Herding",
    "height": {
      "imperial": "22 - 27",
      "metric": "56 - 69"
    },
    "id": 58,
    "image": {
      "height": 576,
      "id": "rkVlblcEQ",
      "url": "https://cdn2.thedogapi.com/images/rkVlblcEQ.jpg",
      "width": 768
    },
    "life_span": "10 - 12 years",
    "name": "Briard",
    "reference_image_id": "rkVlblcEQ",
    "temperament": "Fearless, Loyal, Obedient, Intelligent, Faithful, Protective",
    "weight": {
      "imperial": "70 - 90",
      "metric": "32 - 41"
    }
  },
  {
    "bred_for": "Pointing, retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "17.5 - 20.5",
      "metric": "44 - 52"
    },
    "id": 59,
    "image": {
      "height": 600,
      "id": "HJWZZxc4X",
      "url": "https://cdn2.thedogapi.com/images/HJWZZxc4X.jpg",
      "width": 900
    },
    "life_span": "12 - 14 years",
    "name": "Brittany",
    "reference_image_id": "HJWZZxc4X",
    "temperament": "Agile, Adaptable, Quick, Intelligent, Attentive, Happy",
    "weight": {
      "imperial": "30 - 45",
      "metric": "14 - 20"
    }
  },
  {
    "bred_for": "Bull baiting, Fighting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "21 - 22",
      "metric": "53 - 56"
    },
    "id": 61,
    "image": {
      "height": 1080,
      "id": "VSraIEQGd",
      "url": "https://cdn2.thedogapi.com/images/VSraIEQGd.jpg",
      "width": 1080
    },
    "life_span": "10 - 12 years",
    "name": "Bull Terrier",
    "reference_image_id": "VSraIEQGd",
    "temperament": "Trainable, Protective, Sweet-Tempered, Keen, Active",
    "weight": {
      "imperial": "50 - 70",
      "metric": "23 - 32"
    }
  },
  {
    "bred_for": "An elegant man's fashion statement",
    "height": {
      "imperial": "10 - 14",
      "metric": "25 - 36"
    },
    "id": 62,
    "image": {
      "height": 450,
      "id": "BkKZWlcVX",
      "url": "https://cdn2.thedogapi.com/images/BkKZWlcVX.jpg",
      "width": 674
    },
    "life_span": "11 – 14 years",
    "name": "Bull Terrier (Miniature)",
    "reference_image_id": "BkKZWlcVX",
    "temperament": "Trainable, Protective, Sweet-Tempered, Keen, Active, Territorial",
    "weight": {
      "imperial": "25 - 33",
      "metric": "11 - 15"
    }
  },
  {
    "bred_for": "Estate guardian",
    "breed_group": "Working",
    "height": {
      "imperial": "24 - 27",
      "metric": "61 - 69"
    },
    "id": 64,
    "image": {
      "height": 638,
      "id": "r1ifZl5E7",
      "url": "https://cdn2.thedogapi.com/images/r1ifZl5E7.jpg",
      "width": 850
    },
    "life_span": "8 - 12 years",
    "name": "Bullmastiff",
    "reference_image_id": "r1ifZl5E7",
    "temperament": "Docile, Reliable, Devoted, Alert, Loyal, Reserved, Loving, Protective, Powerful, Calm, Courageous",
    "weight": {
      "imperial": "100 - 130",
      "metric": "45 - 59"
    }
  },
  {
    "bred_for": "Bolting of otter, foxes, other vermin",
    "breed_group": "Terrier",
    "height": {
      "imperial": "9 - 10",
      "metric": "23 - 25"
    },
    "id": 65,
    "image": {
      "height": 836,
      "id": "Sk7Qbg9E7",
      "url": "https://cdn2.thedogapi.com/images/Sk7Qbg9E7.jpg",
      "width": 1254
    },
    "life_span": "14 - 15 years",
    "name": "Cairn Terrier",
    "reference_image_id": "Sk7Qbg9E7",
    "temperament": "Hardy, Fearless, Assertive, Gay, Intelligent, Active",
    "weight": {
      "imperial": "13 - 14",
      "metric": "6 - 6"
    }
  },
  {
    "bred_for": "Companion, guard dog, and hunter",
    "breed_group": "Working",
    "height": {
      "imperial": "23.5 - 27.5",
      "metric": "60 - 70"
    },
    "id": 67,
    "image": {
      "height": 380,
      "id": "r15m-lc4m",
      "url": "https://cdn2.thedogapi.com/images/r15m-lc4m.jpg",
      "width": 645
    },
    "life_span": "10 - 11 years",
    "name": "Cane Corso",
    "reference_image_id": "r15m-lc4m",
    "temperament": "Trainable, Reserved, Stable, Quiet, Even Tempered, Calm",
    "weight": {
      "imperial": "88 - 120",
      "metric": "40 - 54"
    }
  },
  {
    "bred_for": "Cattle droving",
    "breed_group": "Herding",
    "height": {
      "imperial": "10.5 - 12.5",
      "metric": "27 - 32"
    },
    "id": 68,
    "image": {
      "height": 600,
      "id": "SyXN-e9NX",
      "url": "https://cdn2.thedogapi.com/images/SyXN-e9NX.jpg",
      "width": 800
    },
    "life_span": "12 - 14 years",
    "name": "Cardigan Welsh Corgi",
    "reference_image_id": "SyXN-e9NX",
    "temperament": "Affectionate, Devoted, Alert, Companionable, Intelligent, Active",
    "weight": {
      "imperial": "25 - 38",
      "metric": "11 - 17"
    }
  },
  {
    "bred_for": "Driving livestock",
    "breed_group": "Herding",
    "height": {
      "imperial": "20 - 26",
      "metric": "51 - 66"
    },
    "id": 69,
    "image": {
      "height": 650,
      "id": "BJcNbec4X",
      "url": "https://cdn2.thedogapi.com/images/BJcNbec4X.jpg",
      "width": 650
    },
    "life_span": "10 - 12 years",
    "name": "Catahoula Leopard Dog",
    "reference_image_id": "BJcNbec4X",
    "temperament": "Energetic, Inquisitive, Independent, Gentle, Intelligent, Loving",
    "weight": {
      "imperial": "50 - 95",
      "metric": "23 - 43"
    }
  },
  {
    "bred_for": "Guard dogs, defending sheep from predators, mainly wolves, jackals and bears",
    "breed_group": "Working",
    "height": {
      "imperial": "24 - 33.5",
      "metric": "61 - 85"
    },
    "id": 70,
    "image": {
      "height": 682,
      "id": "r1rrWe5Em",
      "url": "https://cdn2.thedogapi.com/images/r1rrWe5Em.jpg",
      "width": 1024
    },
    "life_span": "10 - 12 years",
    "name": "Caucasian Shepherd (Ovcharka)",
    "reference_image_id": "r1rrWe5Em",
    "temperament": "Alert, Quick, Dominant, Powerful, Calm, Strong",
    "weight": {
      "imperial": "80 - 100",
      "metric": "36 - 45"
    }
  },
  {
    "bred_for": "Flushing small birds, companion",
    "breed_group": "Toy",
    "height": {
      "imperial": "12 - 13",
      "metric": "30 - 33"
    },
    "id": 71,
    "image": {
      "height": 558,
      "id": "HJRBbe94Q",
      "url": "https://cdn2.thedogapi.com/images/HJRBbe94Q.jpg",
      "width": 961
    },
    "life_span": "10 - 14 years",
    "name": "Cavalier King Charles Spaniel",
    "reference_image_id": "HJRBbe94Q",
    "temperament": "Fearless, Affectionate, Sociable, Patient, Playful, Adaptable",
    "weight": {
      "imperial": "13 - 18",
      "metric": "6 - 8"
    }
  },
  {
    "bred_for": "Water Retriever",
    "breed_group": "Sporting",
    "height": {
      "imperial": "21 - 26",
      "metric": "53 - 66"
    },
    "id": 76,
    "image": {
      "height": 600,
      "id": "9BXwUeCc2",
      "url": "https://cdn2.thedogapi.com/images/9BXwUeCc2.jpg",
      "width": 600
    },
    "life_span": "10 - 13 years",
    "name": "Chesapeake Bay Retriever",
    "reference_image_id": "9BXwUeCc2",
    "temperament": "Affectionate, Intelligent, Quiet, Dominant, Happy, Protective",
    "weight": {
      "imperial": "55 - 80",
      "metric": "25 - 36"
    }
  },
  {
    "bred_for": "Ratting, lapdog, curio",
    "breed_group": "Toy",
    "height": {
      "imperial": "11 - 13",
      "metric": "28 - 33"
    },
    "id": 78,
    "image": {
      "height": 798,
      "id": "B1pDZx9Nm",
      "url": "https://cdn2.thedogapi.com/images/B1pDZx9Nm.jpg",
      "width": 1200
    },
    "life_span": "10 - 14 years",
    "name": "Chinese Crested",
    "reference_image_id": "B1pDZx9Nm",
    "temperament": "Affectionate, Sweet-Tempered, Lively, Alert, Playful, Happy",
    "weight": {
      "imperial": "10 - 13",
      "metric": "5 - 6"
    }
  },
  {
    "bred_for": "Fighting",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "18 - 20",
      "metric": "46 - 51"
    },
    "id": 79,
    "image": {
      "height": 761,
      "id": "B1ruWl94Q",
      "url": "https://cdn2.thedogapi.com/images/B1ruWl94Q.jpg",
      "width": 1049
    },
    "life_span": "10 years",
    "name": "Chinese Shar-Pei",
    "reference_image_id": "B1ruWl94Q",
    "temperament": "Suspicious, Affectionate, Devoted, Reserved, Independent, Loving",
    "weight": {
      "imperial": "45 - 60",
      "metric": "20 - 27"
    }
  },
  {
    "bred_for": "Sled pulling",
    "breed_group": "Working",
    "height": {
      "imperial": "22 - 26",
      "metric": "56 - 66"
    },
    "id": 80,
    "image": {
      "height": 478,
      "id": "Sypubg54Q",
      "url": "https://cdn2.thedogapi.com/images/Sypubg54Q.jpg",
      "width": 600
    },
    "life_span": "12 - 15 years",
    "name": "Chinook",
    "reference_image_id": "Sypubg54Q",
    "temperament": "Friendly, Alert, Dignified, Intelligent, Calm",
    "weight": {
      "imperial": "50 - 90",
      "metric": "23 - 41"
    }
  },
  {
    "bred_for": "Guardian, cart pulling, hunting",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "17 - 20",
      "metric": "43 - 51"
    },
    "id": 81,
    "image": {
      "height": 673,
      "id": "ry8KWgqEQ",
      "url": "https://cdn2.thedogapi.com/images/ry8KWgqEQ.jpg",
      "width": 1010
    },
    "life_span": "12 - 15 years",
    "name": "Chow Chow",
    "reference_image_id": "ry8KWgqEQ",
    "temperament": "Aloof, Loyal, Independent, Quiet",
    "weight": {
      "imperial": "40 - 70",
      "metric": "18 - 32"
    }
  },
  {
    "bred_for": "Bird flushing, retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "17 - 20",
      "metric": "43 - 51"
    },
    "id": 84,
    "image": {
      "height": 533,
      "id": "rkeqWgq4Q",
      "url": "https://cdn2.thedogapi.com/images/rkeqWgq4Q.jpg",
      "width": 762
    },
    "life_span": "10 - 12 years",
    "name": "Clumber Spaniel",
    "reference_image_id": "rkeqWgq4Q",
    "temperament": "Affectionate, Loyal, Dignified, Gentle, Calm, Great-hearted",
    "weight": {
      "imperial": "55 - 85",
      "metric": "25 - 39"
    }
  },
  {
    "bred_for": "Bird flushing, retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "14 - 15",
      "metric": "36 - 38"
    },
    "id": 86,
    "image": {
      "height": 1080,
      "id": "1lFmrzECl",
      "url": "https://cdn2.thedogapi.com/images/1lFmrzECl.jpg",
      "width": 1080
    },
    "life_span": "12 - 15 years",
    "name": "Cocker Spaniel",
    "reference_image_id": "1lFmrzECl",
    "temperament": "Trainable, Friendly, Affectionate, Playful, Quiet, Faithful",
    "weight": {
      "imperial": "20 - 30",
      "metric": "9 - 14"
    }
  },
  {
    "bred_for": "Hunting the American woodcock",
    "breed_group": "Sporting",
    "height": {
      "imperial": "14 - 15",
      "metric": "36 - 38"
    },
    "id": 87,
    "image": {
      "height": 640,
      "id": "HkRcZe547",
      "url": "https://cdn2.thedogapi.com/images/HkRcZe547.jpg",
      "width": 1024
    },
    "life_span": "12 - 15 years",
    "name": "Cocker Spaniel (American)",
    "reference_image_id": "HkRcZe547",
    "temperament": "Outgoing, Sociable, Trusting, Joyful, Even Tempered, Merry",
    "weight": {
      "imperial": "20 - 30",
      "metric": "9 - 14"
    }
  },
  {
    "bred_for": "Accompanying ladies on long sea voyages, ratters onboard ship.",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "9 - 11",
      "metric": "23 - 28"
    },
    "id": 89,
    "image": {
      "height": 1638,
      "id": "SyviZlqNm",
      "url": "https://cdn2.thedogapi.com/images/SyviZlqNm.jpg",
      "width": 2464
    },
    "life_span": "13 - 16 years",
    "name": "Coton de Tulear",
    "reference_image_id": "SyviZlqNm",
    "temperament": "Affectionate, Lively, Playful, Intelligent, Trainable, Vocal",
    "weight": {
      "imperial": "9 - 15",
      "metric": "4 - 7"
    }
  },
  {
    "bred_for": "Carriage dog - trot alongside carriages to protect the occupants from banditry or other interference",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "19 - 23",
      "metric": "48 - 58"
    },
    "id": 92,
    "image": {
      "height": 800,
      "id": "SkJ3blcN7",
      "url": "https://cdn2.thedogapi.com/images/SkJ3blcN7.jpg",
      "width": 1200
    },
    "life_span": "10 - 13 years",
    "name": "Dalmatian",
    "reference_image_id": "SkJ3blcN7",
    "temperament": "Outgoing, Friendly, Energetic, Playful, Sensitive, Intelligent, Active",
    "weight": {
      "imperial": "50 - 55",
      "metric": "23 - 25"
    }
  },
  {
    "bred_for": "Guardian",
    "breed_group": "Working",
    "height": {
      "imperial": "24 - 28",
      "metric": "61 - 71"
    },
    "id": 94,
    "image": {
      "height": 640,
      "id": "HyL3bl94Q",
      "url": "https://cdn2.thedogapi.com/images/HyL3bl94Q.jpg",
      "width": 1140
    },
    "life_span": "10 years",
    "name": "Doberman Pinscher",
    "reference_image_id": "HyL3bl94Q",
    "temperament": "Fearless, Energetic, Alert, Loyal, Obedient, Confident, Intelligent",
    "weight": {
      "imperial": "66 - 88",
      "metric": "30 - 40"
    }
  },
  {
    "bred_for": "Big-game hunting",
    "breed_group": "Working",
    "height": {
      "imperial": "23.5 - 27",
      "metric": "60 - 69"
    },
    "id": 95,
    "image": {
      "height": 467,
      "id": "S1nhWx94Q",
      "url": "https://cdn2.thedogapi.com/images/S1nhWx94Q.jpg",
      "width": 650
    },
    "life_span": "10 - 12 years",
    "name": "Dogo Argentino",
    "reference_image_id": "S1nhWx94Q",
    "temperament": "Friendly, Affectionate, Cheerful, Loyal, Tolerant, Protective",
    "weight": {
      "imperial": "80 - 100",
      "metric": "36 - 45"
    }
  },
  {
    "bred_for": "Farms, watchdog, guard duty",
    "height": {
      "imperial": "22 - 24.5",
      "metric": "56 - 62"
    },
    "id": 98,
    "image": {
      "height": 511,
      "id": "BkE6Wg5E7",
      "url": "https://cdn2.thedogapi.com/images/BkE6Wg5E7.jpg",
      "width": 856
    },
    "life_span": "15 years",
    "name": "Dutch Shepherd",
    "reference_image_id": "BkE6Wg5E7",
    "temperament": "Reliable, Affectionate, Alert, Loyal, Obedient, Trainable",
    "weight": {
      "imperial": "50 - 70",
      "metric": "23 - 32"
    }
  },
  {
    "bred_for": "Bird setting, retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "24 - 25",
      "metric": "61 - 64"
    },
    "id": 101,
    "image": {
      "height": 683,
      "id": "By4A-eqVX",
      "url": "https://cdn2.thedogapi.com/images/By4A-eqVX.jpg",
      "width": 1024
    },
    "life_span": "12 years",
    "name": "English Setter",
    "reference_image_id": "By4A-eqVX",
    "temperament": "Strong Willed, Mischievous, Affectionate, Energetic, Playful, Companionable, Gentle, Hard-working, Intelligent, Eager, People-Oriented",
    "weight": {
      "imperial": "45 - 80",
      "metric": "20 - 36"
    }
  },
  {
    "bred_for": "Herding & guarding livestock, farm watch dog",
    "breed_group": "Working",
    "height": {
      "imperial": "18 - 23",
      "metric": "46 - 58"
    },
    "id": 102,
    "image": {
      "height": 1280,
      "id": "H1QyMe5EQ",
      "url": "https://cdn2.thedogapi.com/images/H1QyMe5EQ.jpg",
      "width": 1920
    },
    "life_span": "10 - 13 years",
    "name": "English Shepherd",
    "reference_image_id": "H1QyMe5EQ",
    "temperament": "Kind, Energetic, Independent, Adaptable, Intelligent, Bossy",
    "weight": {
      "imperial": "44 - 66",
      "metric": "20 - 30"
    }
  },
  {
    "bred_for": "Bird flushing, retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "19 - 20",
      "metric": "48 - 51"
    },
    "id": 103,
    "image": {
      "height": 1080,
      "id": "Hk0Jfe5VQ",
      "url": "https://cdn2.thedogapi.com/images/Hk0Jfe5VQ.jpg",
      "width": 1440
    },
    "life_span": "12 - 14 years",
    "name": "English Springer Spaniel",
    "reference_image_id": "Hk0Jfe5VQ",
    "temperament": "Affectionate, Cheerful, Alert, Intelligent, Attentive, Active",
    "weight": {
      "imperial": "35 - 50",
      "metric": "16 - 23"
    }
  },
  {
    "bred_for": "Companion of kings",
    "breed_group": "Toy",
    "height": {
      "imperial": "10",
      "metric": "25"
    },
    "id": 104,
    "image": {
      "height": 696,
      "id": "SkIgzxqNQ",
      "url": "https://cdn2.thedogapi.com/images/SkIgzxqNQ.jpg",
      "width": 800
    },
    "life_span": "10 - 12 years",
    "name": "English Toy Spaniel",
    "reference_image_id": "SkIgzxqNQ",
    "temperament": "Affectionate, Reserved, Playful, Gentle, Happy, Loving",
    "weight": {
      "imperial": "8 - 14",
      "metric": "4 - 6"
    }
  },
  {
    "bred_for": "Rat-baiting",
    "height": {
      "imperial": "10 - 12",
      "metric": "25 - 30"
    },
    "id": 105,
    "image": {
      "height": 430,
      "id": "SJ6eMxqEQ",
      "url": "https://cdn2.thedogapi.com/images/SJ6eMxqEQ.jpg",
      "width": 645
    },
    "life_span": "12 - 13 years",
    "name": "English Toy Terrier",
    "reference_image_id": "SJ6eMxqEQ",
    "temperament": "Stubborn, Alert, Companionable, Intelligent, Cunning, Trainable",
    "weight": {
      "imperial": "6 - 8",
      "metric": "3 - 4"
    }
  },
  {
    "bred_for": "Companionship",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "20.5 - 23.5",
      "metric": "52 - 60"
    },
    "id": 107,
    "image": {
      "height": 532,
      "id": "S1VWGx9Nm",
      "url": "https://cdn2.thedogapi.com/images/S1VWGx9Nm.jpg",
      "width": 800
    },
    "life_span": "12 - 14 years",
    "name": "Eurasier",
    "reference_image_id": "S1VWGx9Nm",
    "temperament": "Alert, Reserved, Intelligent, Even Tempered, Watchful, Calm",
    "weight": {
      "imperial": "40 - 70",
      "metric": "18 - 32"
    }
  },
  {
    "bred_for": "Bird flushing, retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "17 - 18",
      "metric": "43 - 46"
    },
    "id": 108,
    "image": {
      "height": 906,
      "id": "SkJfGecE7",
      "url": "https://cdn2.thedogapi.com/images/SkJfGecE7.jpg",
      "width": 1280
    },
    "life_span": "11 - 15 years",
    "name": "Field Spaniel",
    "reference_image_id": "SkJfGecE7",
    "temperament": "Docile, Cautious, Sociable, Sensitive, Adaptable, Familial",
    "weight": {
      "imperial": "35 - 50",
      "metric": "16 - 23"
    }
  },
  {
    "bred_for": "Herding reindeer",
    "breed_group": "Herding",
    "height": {
      "imperial": "16 - 21",
      "metric": "41 - 53"
    },
    "id": 110,
    "image": {
      "height": 800,
      "id": "S1KMGg5Vm",
      "url": "https://cdn2.thedogapi.com/images/S1KMGg5Vm.jpg",
      "width": 1066
    },
    "life_span": "12 - 15 years",
    "name": "Finnish Lapphund",
    "reference_image_id": "S1KMGg5Vm",
    "temperament": "Friendly, Keen, Faithful, Calm, Courageous",
    "weight": {
      "imperial": "33 - 53",
      "metric": "15 - 24"
    }
  },
  {
    "bred_for": "Hunting birds, small mammals",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "15.5 - 20",
      "metric": "39 - 51"
    },
    "id": 111,
    "image": {
      "height": 417,
      "id": "3PjHlQbkV",
      "url": "https://cdn2.thedogapi.com/images/3PjHlQbkV.jpg",
      "width": 500
    },
    "life_span": "12 - 15 years",
    "name": "Finnish Spitz",
    "reference_image_id": "3PjHlQbkV",
    "temperament": "Playful, Loyal, Independent, Intelligent, Happy, Vocal",
    "weight": {
      "imperial": "23 - 28",
      "metric": "10 - 13"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "11 - 12",
      "metric": "28 - 30"
    },
    "id": 113,
    "image": {
      "height": 430,
      "id": "HyWNfxc47",
      "url": "https://cdn2.thedogapi.com/images/HyWNfxc47.jpg",
      "width": 740
    },
    "life_span": "9 - 11 years",
    "name": "French Bulldog",
    "reference_image_id": "HyWNfxc47",
    "temperament": "Playful, Affectionate, Keen, Sociable, Lively, Alert, Easygoing, Patient, Athletic, Bright",
    "weight": {
      "imperial": "28",
      "metric": "13"
    }
  },
  {
    "bred_for": "Watchdog, Hunting vermin on the farm.",
    "breed_group": "Working",
    "height": {
      "imperial": "17 - 20",
      "metric": "43 - 51"
    },
    "id": 114,
    "image": {
      "height": 480,
      "id": "B1u4zgqE7",
      "url": "https://cdn2.thedogapi.com/images/B1u4zgqE7.jpg",
      "width": 740
    },
    "life_span": "12 - 14 years",
    "name": "German Pinscher",
    "reference_image_id": "B1u4zgqE7",
    "temperament": "Spirited, Lively, Intelligent, Loving, Even Tempered, Familial",
    "weight": {
      "imperial": "25 - 45",
      "metric": "11 - 20"
    }
  },
  {
    "bred_for": "Herding, Guard dog",
    "breed_group": "Herding",
    "height": {
      "imperial": "22 - 26",
      "metric": "56 - 66"
    },
    "id": 115,
    "image": {
      "height": 425,
      "id": "SJyBfg5NX",
      "url": "https://cdn2.thedogapi.com/images/SJyBfg5NX.jpg",
      "width": 600
    },
    "life_span": "10 - 13 years",
    "name": "German Shepherd Dog",
    "reference_image_id": "SJyBfg5NX",
    "temperament": "Alert, Loyal, Obedient, Curious, Confident, Intelligent, Watchful, Courageous",
    "weight": {
      "imperial": "50 - 90",
      "metric": "23 - 41"
    }
  },
  {
    "bred_for": "General hunting",
    "breed_group": "Sporting",
    "height": {
      "imperial": "21 - 25",
      "metric": "53 - 64"
    },
    "id": 116,
    "image": {
      "height": 1230,
      "id": "SJqBMg5Nm",
      "url": "https://cdn2.thedogapi.com/images/SJqBMg5Nm.jpg",
      "width": 1395
    },
    "life_span": "12 - 14 years",
    "name": "German Shorthaired Pointer",
    "reference_image_id": "SJqBMg5Nm",
    "temperament": "Boisterous, Bold, Affectionate, Intelligent, Cooperative, Trainable",
    "weight": {
      "imperial": "45 - 70",
      "metric": "20 - 32"
    }
  },
  {
    "bred_for": "Herding, guarding",
    "breed_group": "Working",
    "height": {
      "imperial": "23.5 - 27.5",
      "metric": "60 - 70"
    },
    "id": 119,
    "image": {
      "height": 600,
      "id": "H1NIzlcV7",
      "url": "https://cdn2.thedogapi.com/images/H1NIzlcV7.jpg",
      "width": 900
    },
    "life_span": "10 - 12 years",
    "name": "Giant Schnauzer",
    "reference_image_id": "H1NIzlcV7",
    "temperament": "Strong Willed, Kind, Loyal, Intelligent, Dominant, Powerful",
    "weight": {
      "imperial": "65 - 90",
      "metric": "29 - 41"
    }
  },
  {
    "bred_for": "Rid the home and farm of vermin, and hunt badger and fox",
    "breed_group": "Terrier",
    "height": {
      "imperial": "12.5 - 14",
      "metric": "32 - 36"
    },
    "id": 120,
    "image": {
      "height": 380,
      "id": "H1oLMe94m",
      "url": "https://cdn2.thedogapi.com/images/H1oLMe94m.jpg",
      "width": 645
    },
    "life_span": "12 - 15 years",
    "name": "Glen of Imaal Terrier",
    "reference_image_id": "H1oLMe94m",
    "temperament": "Spirited, Agile, Loyal, Gentle, Active, Courageous",
    "weight": {
      "imperial": "32 - 40",
      "metric": "15 - 18"
    }
  },
  {
    "bred_for": "Retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "21.5 - 24",
      "metric": "55 - 61"
    },
    "id": 121,
    "image": {
      "height": 652,
      "id": "HJ7Pzg5EQ",
      "url": "https://cdn2.thedogapi.com/images/HJ7Pzg5EQ.jpg",
      "width": 900
    },
    "life_span": "10 - 12 years",
    "name": "Golden Retriever",
    "reference_image_id": "HJ7Pzg5EQ",
    "temperament": "Intelligent, Kind, Reliable, Friendly, Trustworthy, Confident",
    "weight": {
      "imperial": "55 - 75",
      "metric": "25 - 34"
    }
  },
  {
    "bred_for": "Find and point gamebirds",
    "breed_group": "Sporting",
    "height": {
      "imperial": "23 - 27",
      "metric": "58 - 69"
    },
    "id": 123,
    "image": {
      "height": 467,
      "id": "SJ5vzx5NX",
      "url": "https://cdn2.thedogapi.com/images/SJ5vzx5NX.jpg",
      "width": 622
    },
    "life_span": "10 - 12 years",
    "name": "Gordon Setter",
    "reference_image_id": "SJ5vzx5NX",
    "temperament": "Fearless, Alert, Loyal, Confident, Gay, Eager",
    "weight": {
      "imperial": "45 - 80",
      "metric": "20 - 36"
    }
  },
  {
    "bred_for": "Hunting & holding boars, Guardian",
    "breed_group": "Working",
    "height": {
      "imperial": "28 - 32",
      "metric": "71 - 81"
    },
    "id": 124,
    "image": {
      "height": 732,
      "id": "B1Edfl9NX",
      "url": "https://cdn2.thedogapi.com/images/B1Edfl9NX.jpg",
      "width": 800
    },
    "life_span": "7 - 10 years",
    "name": "Great Dane",
    "reference_image_id": "B1Edfl9NX",
    "temperament": "Friendly, Devoted, Reserved, Gentle, Confident, Loving",
    "weight": {
      "imperial": "110 - 190",
      "metric": "50 - 86"
    }
  },
  {
    "bred_for": "Sheep guardian",
    "breed_group": "Working",
    "height": {
      "imperial": "25 - 32",
      "metric": "64 - 81"
    },
    "id": 125,
    "image": {
      "height": 550,
      "id": "B12uzg9V7",
      "url": "https://cdn2.thedogapi.com/images/B12uzg9V7.png",
      "width": 800
    },
    "life_span": "10 - 12 years",
    "name": "Great Pyrenees",
    "reference_image_id": "B12uzg9V7",
    "temperament": "Strong Willed, Fearless, Affectionate, Patient, Gentle, Confident",
    "weight": {
      "imperial": "85 - 115",
      "metric": "39 - 52"
    }
  },
  {
    "bred_for": "Coursing hares",
    "breed_group": "Hound",
    "height": {
      "imperial": "27 - 30",
      "metric": "69 - 76"
    },
    "id": 127,
    "image": {
      "height": 681,
      "id": "ryNYMx94X",
      "url": "https://cdn2.thedogapi.com/images/ryNYMx94X.jpg",
      "width": 1024
    },
    "life_span": "10 - 13 years",
    "name": "Greyhound",
    "reference_image_id": "ryNYMx94X",
    "temperament": "Affectionate, Athletic, Gentle, Intelligent, Quiet, Even Tempered",
    "weight": {
      "imperial": "50 - 70",
      "metric": "23 - 32"
    }
  },
  {
    "bred_for": "Hunt and kill vermin in stables",
    "height": {
      "imperial": "9 - 11",
      "metric": "23 - 28"
    },
    "id": 128,
    "image": {
      "height": 380,
      "id": "ryoYGec4Q",
      "url": "https://cdn2.thedogapi.com/images/ryoYGec4Q.jpg",
      "width": 645
    },
    "life_span": "10 – 15 years",
    "name": "Griffon Bruxellois",
    "reference_image_id": "ryoYGec4Q",
    "temperament": "Self-important, Inquisitive, Alert, Companionable, Sensitive, Watchful",
    "weight": {
      "imperial": "12",
      "metric": "5"
    }
  },
  {
    "bred_for": "Hunting hares by trailing them",
    "breed_group": "Hound",
    "height": {
      "imperial": "18 - 22",
      "metric": "46 - 56"
    },
    "id": 129,
    "image": {
      "height": 1080,
      "id": "B1IcfgqE7",
      "url": "https://cdn2.thedogapi.com/images/B1IcfgqE7.jpg",
      "width": 1920
    },
    "life_span": "12 - 15 years",
    "name": "Harrier",
    "reference_image_id": "B1IcfgqE7",
    "temperament": "Outgoing, Friendly, Cheerful, Sweet-Tempered, Tolerant, Active",
    "weight": {
      "imperial": "40 - 60",
      "metric": "18 - 27"
    }
  },
  {
    "bred_for": "Companionship",
    "breed_group": "Toy",
    "height": {
      "imperial": "8.5 - 11.5",
      "metric": "22 - 29"
    },
    "id": 130,
    "image": {
      "height": 507,
      "id": "rkXiGl9V7",
      "url": "https://cdn2.thedogapi.com/images/rkXiGl9V7.jpg",
      "width": 800
    },
    "life_span": "14 - 15 years",
    "name": "Havanese",
    "reference_image_id": "rkXiGl9V7",
    "temperament": "Affectionate, Responsive, Playful, Companionable, Gentle, Intelligent",
    "weight": {
      "imperial": "7 - 13",
      "metric": "3 - 6"
    }
  },
  {
    "bred_for": "Bird setting, retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "24 - 27",
      "metric": "61 - 69"
    },
    "id": 134,
    "image": {
      "height": 522,
      "id": "S1osGeqVm",
      "url": "https://cdn2.thedogapi.com/images/S1osGeqVm.jpg",
      "width": 818
    },
    "life_span": "10 - 11 years",
    "name": "Irish Setter",
    "reference_image_id": "S1osGeqVm",
    "temperament": "Affectionate, Energetic, Lively, Independent, Playful, Companionable",
    "weight": {
      "imperial": "35 - 70",
      "metric": "16 - 32"
    }
  },
  {
    "breed_group": "Terrier",
    "height": {
      "imperial": "18",
      "metric": "46"
    },
    "id": 135,
    "image": {
      "height": 626,
      "id": "By-hGecVX",
      "url": "https://cdn2.thedogapi.com/images/By-hGecVX.jpg",
      "width": 800
    },
    "life_span": "12 - 16 years",
    "name": "Irish Terrier",
    "reference_image_id": "By-hGecVX",
    "temperament": "Respectful, Lively, Intelligent, Dominant, Protective, Trainable",
    "weight": {
      "imperial": "25 - 27",
      "metric": "11 - 12"
    }
  },
  {
    "bred_for": "Coursing wolves, elk",
    "breed_group": "Hound",
    "height": {
      "imperial": "30 - 35",
      "metric": "76 - 89"
    },
    "id": 137,
    "image": {
      "height": 630,
      "id": "Hyd2zgcEX",
      "url": "https://cdn2.thedogapi.com/images/Hyd2zgcEX.jpg",
      "width": 1000
    },
    "life_span": "6 - 8 years",
    "name": "Irish Wolfhound",
    "reference_image_id": "Hyd2zgcEX",
    "temperament": "Sweet-Tempered, Loyal, Dignified, Patient, Thoughtful, Generous",
    "weight": {
      "imperial": "105 - 180",
      "metric": "48 - 82"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "13 - 15",
      "metric": "33 - 38"
    },
    "id": 138,
    "image": {
      "height": 377,
      "id": "SJAnzg9NX",
      "url": "https://cdn2.thedogapi.com/images/SJAnzg9NX.jpg",
      "width": 640
    },
    "life_span": "12 - 15 years",
    "name": "Italian Greyhound",
    "reference_image_id": "SJAnzg9NX",
    "temperament": "Mischievous, Affectionate, Agile, Athletic, Companionable, Intelligent",
    "weight": {
      "imperial": "7 - 15",
      "metric": "3 - 7"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "8 - 11",
      "metric": "20 - 28"
    },
    "id": 140,
    "image": {
      "height": 581,
      "id": "r1H6feqEm",
      "url": "https://cdn2.thedogapi.com/images/r1H6feqEm.jpg",
      "width": 900
    },
    "life_span": "12 - 14 years",
    "name": "Japanese Chin",
    "reference_image_id": "r1H6feqEm",
    "temperament": "Alert, Loyal, Independent, Intelligent, Loving, Cat-like",
    "weight": {
      "imperial": "4 - 9",
      "metric": "2 - 4"
    }
  },
  {
    "bred_for": "Companion",
    "height": {
      "imperial": "12 - 15",
      "metric": "30 - 38"
    },
    "id": 141,
    "image": {
      "height": 351,
      "id": "HksaMxqNX",
      "url": "https://cdn2.thedogapi.com/images/HksaMxqNX.jpg",
      "width": 600
    },
    "life_span": "10 – 16 years",
    "name": "Japanese Spitz",
    "reference_image_id": "HksaMxqNX",
    "temperament": "Affectionate, Obedient, Playful, Companionable, Intelligent, Proud",
    "weight": {
      "imperial": "15 - 19",
      "metric": "7 - 9"
    }
  },
  {
    "bred_for": "Barge watchdog",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "17 - 18",
      "metric": "43 - 46"
    },
    "id": 142,
    "image": {
      "height": 683,
      "id": "S1GAGg9Vm",
      "url": "https://cdn2.thedogapi.com/images/S1GAGg9Vm.jpg",
      "width": 1024
    },
    "life_span": "12 - 15 years",
    "name": "Keeshond",
    "reference_image_id": "S1GAGg9Vm",
    "temperament": "Agile, Obedient, Playful, Quick, Sturdy, Bright",
    "weight": {
      "imperial": "35 - 45",
      "metric": "16 - 20"
    }
  },
  {
    "bred_for": "Sheep guardian",
    "breed_group": "Working",
    "height": {
      "imperial": "25.5 - 27.5",
      "metric": "65 - 70"
    },
    "id": 144,
    "image": {
      "height": 772,
      "id": "Bko0fl547",
      "url": "https://cdn2.thedogapi.com/images/Bko0fl547.jpg",
      "width": 1030
    },
    "life_span": "10 - 12 years",
    "name": "Komondor",
    "reference_image_id": "Bko0fl547",
    "temperament": "Steady, Fearless, Affectionate, Independent, Gentle, Calm",
    "weight": {
      "imperial": "80 - 100",
      "metric": "36 - 45"
    }
  },
  {
    "bred_for": "Luring ducks into traps - \"tolling\"",
    "breed_group": "Sporting",
    "height": {
      "imperial": "14 - 16",
      "metric": "36 - 41"
    },
    "id": 145,
    "image": {
      "height": 1080,
      "id": "kOMy84GQE",
      "url": "https://cdn2.thedogapi.com/images/kOMy84GQE.jpg",
      "width": 1080
    },
    "life_span": "12 - 15 years",
    "name": "Kooikerhondje",
    "reference_image_id": "kOMy84GQE",
    "temperament": "Benevolent, Agile, Alert, Intelligent, Active, Territorial",
    "weight": {
      "imperial": "20 - 30",
      "metric": "9 - 14"
    }
  },
  {
    "bred_for": "Guardian, hunting large game",
    "breed_group": "Working",
    "height": {
      "imperial": "26 - 30",
      "metric": "66 - 76"
    },
    "id": 147,
    "image": {
      "height": 768,
      "id": "BykZ7ecVX",
      "url": "https://cdn2.thedogapi.com/images/BykZ7ecVX.jpg",
      "width": 960
    },
    "life_span": "8 - 10 years",
    "name": "Kuvasz",
    "reference_image_id": "BykZ7ecVX",
    "temperament": "Clownish, Loyal, Patient, Independent, Intelligent, Protective",
    "weight": {
      "imperial": "70 - 115",
      "metric": "32 - 52"
    }
  },
  {
    "bred_for": "Water retrieving",
    "breed_group": "Sporting",
    "height": {
      "imperial": "21.5 - 24.5",
      "metric": "55 - 62"
    },
    "id": 149,
    "image": {
      "height": 667,
      "id": "B1uW7l5VX",
      "url": "https://cdn2.thedogapi.com/images/B1uW7l5VX.jpg",
      "width": 992
    },
    "life_span": "10 - 13 years",
    "name": "Labrador Retriever",
    "reference_image_id": "B1uW7l5VX",
    "temperament": "Kind, Outgoing, Agile, Gentle, Intelligent, Trusting, Even Tempered",
    "weight": {
      "imperial": "55 - 80",
      "metric": "25 - 36"
    }
  },
  {
    "bred_for": "Water retrieval dog in the marshes of Romagna",
    "breed_group": "Sporting",
    "height": {
      "imperial": "16 - 19",
      "metric": "41 - 48"
    },
    "id": 151,
    "image": {
      "height": 1200,
      "id": "ryzzmgqE7",
      "url": "https://cdn2.thedogapi.com/images/ryzzmgqE7.jpg",
      "width": 1600
    },
    "life_span": "14 - 16 years",
    "name": "Lagotto Romagnolo",
    "reference_image_id": "ryzzmgqE7",
    "temperament": "Keen, Loyal, Companionable, Loving, Active, Trainable",
    "weight": {
      "imperial": "24 - 35",
      "metric": "11 - 16"
    }
  },
  {
    "bred_for": "Cattle herding, Ratting, Driving cattle to market.",
    "height": {
      "imperial": "10 - 12",
      "metric": "25 - 30"
    },
    "id": 153,
    "image": {
      "height": 453,
      "id": "S1RGml5Em",
      "url": "https://cdn2.thedogapi.com/images/S1RGml5Em.jpg",
      "width": 680
    },
    "life_span": "12 – 15 years",
    "name": "Lancashire Heeler",
    "reference_image_id": "S1RGml5Em",
    "temperament": "Clever, Friendly, Alert, Intelligent",
    "weight": {
      "imperial": "6 - 13",
      "metric": "3 - 6"
    }
  },
  {
    "bred_for": "Guardian, appearance.",
    "breed_group": "Working",
    "height": {
      "imperial": "25.5 - 31.5",
      "metric": "65 - 80"
    },
    "id": 155,
    "image": {
      "height": 694,
      "id": "ByrmQlqVm",
      "url": "https://cdn2.thedogapi.com/images/ByrmQlqVm.jpg",
      "width": 1024
    },
    "life_span": "6 - 8 years",
    "name": "Leonberger",
    "reference_image_id": "ByrmQlqVm",
    "temperament": "Obedient, Fearless, Loyal, Companionable, Adaptable, Loving",
    "weight": {
      "imperial": "120 - 170",
      "metric": "54 - 77"
    }
  },
  {
    "bred_for": "Guarding inside the home, companion",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "10 - 11",
      "metric": "25 - 28"
    },
    "id": 156,
    "image": {
      "height": 444,
      "id": "SJp7Qe5EX",
      "url": "https://cdn2.thedogapi.com/images/SJp7Qe5EX.jpg",
      "width": 680
    },
    "life_span": "12 - 15 years",
    "name": "Lhasa Apso",
    "reference_image_id": "SJp7Qe5EX",
    "temperament": "Steady, Fearless, Friendly, Devoted, Assertive, Spirited, Energetic, Lively, Alert, Obedient, Playful, Intelligent",
    "weight": {
      "imperial": "12 - 18",
      "metric": "5 - 8"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "8 - 10",
      "metric": "20 - 25"
    },
    "id": 161,
    "image": {
      "height": 453,
      "id": "B1SV7gqN7",
      "url": "https://cdn2.thedogapi.com/images/B1SV7gqN7.jpg",
      "width": 680
    },
    "life_span": "15 - 18 years",
    "name": "Maltese",
    "reference_image_id": "B1SV7gqN7",
    "temperament": "Playful, Docile, Fearless, Affectionate, Sweet-Tempered, Lively, Responsive, Easygoing, Gentle, Intelligent, Active",
    "weight": {
      "imperial": "4 - 7",
      "metric": "2 - 3"
    }
  },
  {
    "breed_group": "Herding",
    "height": {
      "imperial": "13 - 18",
      "metric": "33 - 46"
    },
    "id": 165,
    "image": {
      "height": 640,
      "id": "BkHHQgcN7",
      "url": "https://cdn2.thedogapi.com/images/BkHHQgcN7.jpg",
      "width": 920
    },
    "life_span": "12 - 15 years",
    "name": "Miniature American Shepherd",
    "reference_image_id": "BkHHQgcN7",
    "temperament": "Energetic, Loyal, Intelligent, Trainable",
    "weight": {
      "imperial": "20 - 40",
      "metric": "9 - 18"
    }
  },
  {
    "bred_for": "Small vermin hunting",
    "breed_group": "Toy",
    "height": {
      "imperial": "10 - 12.5",
      "metric": "25 - 32"
    },
    "id": 167,
    "image": {
      "height": 1125,
      "id": "Hy3H7g94X",
      "url": "https://cdn2.thedogapi.com/images/Hy3H7g94X.jpg",
      "width": 1500
    },
    "life_span": "15 years",
    "name": "Miniature Pinscher",
    "reference_image_id": "Hy3H7g94X",
    "temperament": "Clever, Outgoing, Friendly, Energetic, Responsive, Playful",
    "weight": {
      "imperial": "8 - 11",
      "metric": "4 - 5"
    }
  },
  {
    "bred_for": "Ratting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "12 - 14",
      "metric": "30 - 36"
    },
    "id": 168,
    "image": {
      "height": 533,
      "id": "SJIUQl9NX",
      "url": "https://cdn2.thedogapi.com/images/SJIUQl9NX.jpg",
      "width": 800
    },
    "life_span": "12 - 14 years",
    "name": "Miniature Schnauzer",
    "reference_image_id": "SJIUQl9NX",
    "temperament": "Fearless, Friendly, Spirited, Alert, Obedient, Intelligent",
    "weight": {
      "imperial": "11 - 20",
      "metric": "5 - 9"
    }
  },
  {
    "bred_for": "All purpose water dog, fishing aid",
    "breed_group": "Working",
    "height": {
      "imperial": "26 - 28",
      "metric": "66 - 71"
    },
    "id": 171,
    "image": {
      "height": 986,
      "id": "Sk4DXl54m",
      "url": "https://cdn2.thedogapi.com/images/Sk4DXl54m.jpg",
      "width": 1174
    },
    "life_span": "8 - 10 years",
    "name": "Newfoundland",
    "reference_image_id": "Sk4DXl54m",
    "temperament": "Sweet-Tempered, Gentle, Trainable",
    "weight": {
      "imperial": "100 - 150",
      "metric": "45 - 68"
    }
  },
  {
    "bred_for": "Ratting, fox bolting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "9 - 10",
      "metric": "23 - 25"
    },
    "id": 172,
    "image": {
      "height": 1092,
      "id": "B1ADQg94X",
      "url": "https://cdn2.thedogapi.com/images/B1ADQg94X.jpg",
      "width": 1468
    },
    "life_span": "12 - 15 years",
    "name": "Norfolk Terrier",
    "reference_image_id": "B1ADQg94X",
    "temperament": "Self-confidence, Fearless, Spirited, Companionable, Happy, Lovable",
    "weight": {
      "imperial": "11 - 12",
      "metric": "5 - 5"
    }
  },
  {
    "bred_for": "Ratting, fox bolting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "10",
      "metric": "25"
    },
    "id": 176,
    "image": {
      "height": 640,
      "id": "BkgKXlqE7",
      "url": "https://cdn2.thedogapi.com/images/BkgKXlqE7.jpg",
      "width": 1140
    },
    "life_span": "12 - 15 years",
    "name": "Norwich Terrier",
    "reference_image_id": "BkgKXlqE7",
    "temperament": "Hardy, Affectionate, Energetic, Sensitive, Intelligent",
    "weight": {
      "imperial": "11 - 12",
      "metric": "5 - 5"
    }
  },
  {
    "breed_group": "Sporting",
    "height": {
      "imperial": "17 - 21",
      "metric": "43 - 53"
    },
    "id": 177,
    "image": {
      "height": 420,
      "id": "SyYtQe5V7",
      "url": "https://cdn2.thedogapi.com/images/SyYtQe5V7.jpg",
      "width": 630
    },
    "life_span": "12 - 14 years",
    "name": "Nova Scotia Duck Tolling Retriever",
    "reference_image_id": "SyYtQe5V7",
    "temperament": "Outgoing, Alert, Patient, Intelligent, Loving",
    "weight": {
      "imperial": "35 - 50",
      "metric": "16 - 23"
    }
  },
  {
    "bred_for": "Driving sheep, cattle",
    "breed_group": "Herding",
    "height": {
      "imperial": "21",
      "metric": "53"
    },
    "id": 178,
    "image": {
      "height": 889,
      "id": "HkZ57lq4m",
      "url": "https://cdn2.thedogapi.com/images/HkZ57lq4m.jpg",
      "width": 1334
    },
    "life_span": "10 - 12 years",
    "name": "Old English Sheepdog",
    "reference_image_id": "HkZ57lq4m",
    "temperament": "Sociable, Bubbly, Playful, Adaptable, Intelligent, Loving",
    "weight": {
      "imperial": "60 - 100",
      "metric": "27 - 45"
    }
  },
  {
    "height": {
      "imperial": "15 - 19",
      "metric": "38 - 48"
    },
    "id": 179,
    "image": {
      "height": 546,
      "id": "B1d5me547",
      "url": "https://cdn2.thedogapi.com/images/B1d5me547.jpg",
      "width": 554
    },
    "life_span": "9 – 14 years",
    "name": "Olde English Bulldogge",
    "reference_image_id": "B1d5me547",
    "temperament": "Friendly, Alert, Confident, Loving, Courageous, Strong",
    "weight": {
      "imperial": "65 – 85",
      "metric": "NaN"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "8 - 11",
      "metric": "20 - 28"
    },
    "id": 181,
    "image": {
      "height": 765,
      "id": "SkJj7e547",
      "url": "https://cdn2.thedogapi.com/images/SkJj7e547.jpg",
      "width": 960
    },
    "life_span": "13 - 17 years",
    "name": "Papillon",
    "reference_image_id": "SkJj7e547",
    "temperament": "Hardy, Friendly, Energetic, Alert, Intelligent, Happy",
    "weight": {
      "imperial": "3 - 12",
      "metric": "1 - 5"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "6 - 9",
      "metric": "15 - 23"
    },
    "id": 183,
    "image": {
      "height": 640,
      "id": "ByIiml9Nm",
      "url": "https://cdn2.thedogapi.com/images/ByIiml9Nm.jpg",
      "width": 960
    },
    "life_span": "14 - 18 years",
    "name": "Pekingese",
    "reference_image_id": "ByIiml9Nm",
    "temperament": "Opinionated, Good-natured, Stubborn, Affectionate, Aggressive, Intelligent",
    "weight": {
      "imperial": "14",
      "metric": "6"
    }
  },
  {
    "bred_for": "Driving stock to market in northern Wales",
    "breed_group": "Herding",
    "height": {
      "imperial": "10 - 12",
      "metric": "25 - 30"
    },
    "id": 184,
    "image": {
      "height": 720,
      "id": "rJ6iQeqEm",
      "url": "https://cdn2.thedogapi.com/images/rJ6iQeqEm.jpg",
      "width": 1280
    },
    "life_span": "12 - 14 years",
    "name": "Pembroke Welsh Corgi",
    "reference_image_id": "rJ6iQeqEm",
    "temperament": "Tenacious, Outgoing, Friendly, Bold, Playful, Protective",
    "weight": {
      "imperial": "25 - 30",
      "metric": "11 - 14"
    }
  },
  {
    "breed_group": "Working",
    "height": {
      "imperial": "22 - 25.5",
      "metric": "56 - 65"
    },
    "id": 185,
    "image": {
      "height": 483,
      "id": "S1V3Qeq4X",
      "url": "https://cdn2.thedogapi.com/images/S1V3Qeq4X.jpg",
      "width": 600
    },
    "life_span": "10 - 12 years",
    "name": "Perro de Presa Canario",
    "reference_image_id": "S1V3Qeq4X",
    "temperament": "Strong Willed, Suspicious, Gentle, Dominant, Calm",
    "weight": {
      "imperial": "88 - 110",
      "metric": "40 - 50"
    }
  },
  {
    "bred_for": "Hunting rabbits",
    "breed_group": "Hound",
    "height": {
      "imperial": "21 - 25",
      "metric": "53 - 64"
    },
    "id": 188,
    "image": {
      "height": 2938,
      "id": "Byz6mgqEQ",
      "url": "https://cdn2.thedogapi.com/images/Byz6mgqEQ.jpg",
      "width": 3918
    },
    "life_span": "12 - 14 years",
    "name": "Pharaoh Hound",
    "reference_image_id": "Byz6mgqEQ",
    "temperament": "Affectionate, Sociable, Playful, Intelligent, Active, Trainable",
    "weight": {
      "imperial": "40 - 60",
      "metric": "18 - 27"
    }
  },
  {
    "bred_for": "Hunting big-game like Boar.",
    "breed_group": "Hound",
    "height": {
      "imperial": "20 - 25",
      "metric": "51 - 64"
    },
    "id": 189,
    "image": {
      "height": 480,
      "id": "B1i67l5VQ",
      "url": "https://cdn2.thedogapi.com/images/B1i67l5VQ.jpg",
      "width": 640
    },
    "life_span": "12 - 14 years",
    "name": "Plott",
    "reference_image_id": "B1i67l5VQ",
    "temperament": "Bold, Alert, Loyal, Intelligent",
    "weight": {
      "imperial": "40 - 60",
      "metric": "18 - 27"
    }
  },
  {
    "bred_for": "Companion",
    "breed_group": "Toy",
    "height": {
      "imperial": "8 - 12",
      "metric": "20 - 30"
    },
    "id": 193,
    "image": {
      "height": 532,
      "id": "HJd0XecNX",
      "url": "https://cdn2.thedogapi.com/images/HJd0XecNX.jpg",
      "width": 800
    },
    "life_span": "15 years",
    "name": "Pomeranian",
    "reference_image_id": "HJd0XecNX",
    "temperament": "Extroverted, Friendly, Sociable, Playful, Intelligent, Active",
    "weight": {
      "imperial": "3 - 7",
      "metric": "1 - 3"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "10 - 12",
      "metric": "25 - 30"
    },
    "id": 201,
    "image": {
      "height": 600,
      "id": "HyJvcl9N7",
      "url": "https://cdn2.thedogapi.com/images/HyJvcl9N7.jpg",
      "width": 800
    },
    "life_span": "12 - 14 years",
    "name": "Pug",
    "reference_image_id": "HyJvcl9N7",
    "temperament": "Docile, Clever, Charming, Stubborn, Sociable, Playful, Quiet, Attentive",
    "weight": {
      "imperial": "14 - 18",
      "metric": "6 - 8"
    }
  },
  {
    "bred_for": "Herding",
    "breed_group": "Herding",
    "height": {
      "imperial": "16 - 17",
      "metric": "41 - 43"
    },
    "id": 204,
    "image": {
      "height": 829,
      "id": "ryPgVl5N7",
      "url": "https://cdn2.thedogapi.com/images/ryPgVl5N7.jpg",
      "width": 1199
    },
    "life_span": "12 - 16 Years years",
    "name": "Puli",
    "reference_image_id": "ryPgVl5N7",
    "temperament": "Energetic, Agile, Loyal, Obedient, Intelligent, Faithful",
    "weight": {
      "imperial": "25 - 35",
      "metric": "11 - 16"
    }
  },
  {
    "breed_group": "Herding",
    "height": {
      "imperial": "15 - 18.5",
      "metric": "38 - 47"
    },
    "id": 205,
    "image": {
      "height": 391,
      "id": "SyRe4xcN7",
      "url": "https://cdn2.thedogapi.com/images/SyRe4xcN7.jpg",
      "width": 695
    },
    "life_span": "13 - 15 years",
    "name": "Pumi",
    "reference_image_id": "SyRe4xcN7",
    "temperament": "Lively, Reserved, Intelligent, Active, Protective, Vocal",
    "weight": {
      "imperial": "18 - 33",
      "metric": "8 - 15"
    }
  },
  {
    "breed_group": "Terrier",
    "height": {
      "imperial": "10 - 13",
      "metric": "25 - 33"
    },
    "id": 207,
    "image": {
      "height": 689,
      "id": "HkXWNl9E7",
      "url": "https://cdn2.thedogapi.com/images/HkXWNl9E7.jpg",
      "width": 825
    },
    "life_span": "12 - 18 years",
    "name": "Rat Terrier",
    "reference_image_id": "HkXWNl9E7",
    "temperament": "Affectionate, Lively, Inquisitive, Alert, Intelligent, Loving",
    "weight": {
      "imperial": "8 - 25",
      "metric": "4 - 11"
    }
  },
  {
    "bred_for": "Hunting raccoon, deer, bear, and cougar.",
    "breed_group": "Hound",
    "height": {
      "imperial": "21 - 27",
      "metric": "53 - 69"
    },
    "id": 208,
    "image": {
      "height": 1323,
      "id": "HJMzEl5N7",
      "url": "https://cdn2.thedogapi.com/images/HJMzEl5N7.jpg",
      "width": 1537
    },
    "life_span": "10 - 12 years",
    "name": "Redbone Coonhound",
    "reference_image_id": "HJMzEl5N7",
    "temperament": "Affectionate, Energetic, Independent, Companionable, Familial, Unflappable",
    "weight": {
      "imperial": "45 - 80",
      "metric": "20 - 36"
    }
  },
  {
    "bred_for": "Big game hunting, guarding",
    "breed_group": "Hound",
    "height": {
      "imperial": "24 - 27",
      "metric": "61 - 69"
    },
    "id": 209,
    "image": {
      "height": 667,
      "id": "By9zNgqE7",
      "url": "https://cdn2.thedogapi.com/images/By9zNgqE7.jpg",
      "width": 1000
    },
    "life_span": "10 - 12 years",
    "name": "Rhodesian Ridgeback",
    "reference_image_id": "By9zNgqE7",
    "temperament": "Strong Willed, Mischievous, Loyal, Dignified, Sensitive, Intelligent",
    "weight": {
      "imperial": "75 - 80",
      "metric": "34 - 36"
    }
  },
  {
    "bred_for": "Cattle drover, guardian, draft",
    "breed_group": "Working",
    "height": {
      "imperial": "22 - 27",
      "metric": "56 - 69"
    },
    "id": 210,
    "image": {
      "height": 595,
      "id": "r1xXEgcNX",
      "url": "https://cdn2.thedogapi.com/images/r1xXEgcNX.jpg",
      "width": 736
    },
    "life_span": "8 - 10 years",
    "name": "Rottweiler",
    "reference_image_id": "r1xXEgcNX",
    "temperament": "Steady, Good-natured, Fearless, Devoted, Alert, Obedient, Confident, Self-assured, Calm, Courageous",
    "weight": {
      "imperial": "75 - 110",
      "metric": "34 - 50"
    }
  },
  {
    "bred_for": "Draft, search, rescue",
    "breed_group": "Working",
    "height": {
      "imperial": "25.5 - 27.5",
      "metric": "65 - 70"
    },
    "id": 212,
    "image": {
      "height": 1084,
      "id": "_Qf9nfRzL",
      "url": "https://cdn2.thedogapi.com/images/_Qf9nfRzL.png",
      "width": 1080
    },
    "life_span": "7 - 10 years",
    "name": "Saint Bernard",
    "reference_image_id": "_Qf9nfRzL",
    "temperament": "Friendly, Lively, Gentle, Watchful, Calm",
    "weight": {
      "imperial": "130 - 180",
      "metric": "59 - 82"
    }
  },
  {
    "bred_for": "Coursing gazelle and hare",
    "breed_group": "Hound",
    "height": {
      "imperial": "23 - 28",
      "metric": "58 - 71"
    },
    "id": 213,
    "image": {
      "height": 450,
      "id": "fjFIuehNo",
      "url": "https://cdn2.thedogapi.com/images/fjFIuehNo.jpg",
      "width": 750
    },
    "life_span": "12 - 14 years",
    "name": "Saluki",
    "reference_image_id": "fjFIuehNo",
    "temperament": "Aloof, Reserved, Intelligent, Quiet",
    "weight": {
      "imperial": "35 - 65",
      "metric": "16 - 29"
    }
  },
  {
    "bred_for": "Herding reindeer, guardian, draft",
    "breed_group": "Working",
    "height": {
      "imperial": "19 - 23.5",
      "metric": "48 - 60"
    },
    "id": 214,
    "image": {
      "height": 797,
      "id": "S1T8Ee9Nm",
      "url": "https://cdn2.thedogapi.com/images/S1T8Ee9Nm.jpg",
      "width": 1200
    },
    "life_span": "12 - 14 years",
    "name": "Samoyed",
    "reference_image_id": "S1T8Ee9Nm",
    "temperament": "Stubborn, Friendly, Sociable, Lively, Alert, Playful",
    "weight": {
      "imperial": "50 - 60",
      "metric": "23 - 27"
    }
  },
  {
    "bred_for": "Barge watchdog",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "10 - 13",
      "metric": "25 - 33"
    },
    "id": 216,
    "image": {
      "height": 681,
      "id": "SyBvVgc47",
      "url": "https://cdn2.thedogapi.com/images/SyBvVgc47.jpg",
      "width": 1024
    },
    "life_span": "13 - 15 years",
    "name": "Schipperke",
    "reference_image_id": "SyBvVgc47",
    "temperament": "Fearless, Agile, Curious, Independent, Confident, Faithful",
    "weight": {
      "imperial": "10 - 16",
      "metric": "5 - 7"
    }
  },
  {
    "bred_for": "Coursing deer",
    "breed_group": "Hound",
    "height": {
      "imperial": "28 - 32",
      "metric": "71 - 81"
    },
    "id": 218,
    "image": {
      "height": 480,
      "id": "SkNjqx9NQ",
      "url": "https://cdn2.thedogapi.com/images/SkNjqx9NQ.jpg",
      "width": 700
    },
    "life_span": "8 - 10 years",
    "name": "Scottish Deerhound",
    "reference_image_id": "SkNjqx9NQ",
    "temperament": "Docile, Friendly, Dignified, Gentle",
    "weight": {
      "imperial": "70 - 130",
      "metric": "32 - 59"
    }
  },
  {
    "bred_for": "Vermin hunting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "10",
      "metric": "25"
    },
    "id": 219,
    "image": {
      "height": 976,
      "id": "Bklnce5NX",
      "url": "https://cdn2.thedogapi.com/images/Bklnce5NX.jpg",
      "width": 1280
    },
    "life_span": "11 - 13 years",
    "name": "Scottish Terrier",
    "reference_image_id": "Bklnce5NX",
    "temperament": "Feisty, Alert, Independent, Playful, Quick, Self-assured",
    "weight": {
      "imperial": "18 - 22",
      "metric": "8 - 10"
    }
  },
  {
    "bred_for": "Sheep herding",
    "breed_group": "Herding",
    "height": {
      "imperial": "13 - 16",
      "metric": "33 - 41"
    },
    "id": 221,
    "image": {
      "height": 640,
      "id": "rJa29l9E7",
      "url": "https://cdn2.thedogapi.com/images/rJa29l9E7.jpg",
      "width": 824
    },
    "life_span": "12 - 14 years",
    "name": "Shetland Sheepdog",
    "reference_image_id": "rJa29l9E7",
    "temperament": "Affectionate, Lively, Responsive, Alert, Loyal, Reserved, Playful, Gentle, Intelligent, Active, Trainable, Strong",
    "weight": {
      "imperial": "30",
      "metric": "14"
    }
  },
  {
    "bred_for": "Hunting in the mountains of Japan, Alert Watchdog",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "13.5 - 16.5",
      "metric": "34 - 42"
    },
    "id": 222,
    "image": {
      "height": 1080,
      "id": "Zn3IjPX3f",
      "url": "https://cdn2.thedogapi.com/images/Zn3IjPX3f.jpg",
      "width": 1080
    },
    "life_span": "12 - 16 years",
    "name": "Shiba Inu",
    "reference_image_id": "Zn3IjPX3f",
    "temperament": "Charming, Fearless, Keen, Alert, Confident, Faithful",
    "weight": {
      "imperial": "17 - 23",
      "metric": "8 - 10"
    }
  },
  {
    "bred_for": "Lapdog",
    "breed_group": "Toy",
    "height": {
      "imperial": "8 - 11",
      "metric": "20 - 28"
    },
    "id": 223,
    "image": {
      "height": 600,
      "id": "BkrJjgcV7",
      "url": "https://cdn2.thedogapi.com/images/BkrJjgcV7.jpg",
      "width": 800
    },
    "life_span": "10 - 18 years",
    "name": "Shih Tzu",
    "reference_image_id": "BkrJjgcV7",
    "temperament": "Clever, Spunky, Outgoing, Friendly, Affectionate, Lively, Alert, Loyal, Independent, Playful, Gentle, Intelligent, Happy, Active, Courageous",
    "weight": {
      "imperial": "9 - 16",
      "metric": "4 - 7"
    }
  },
  {
    "bred_for": "Swimming, Carrying backpacks, Pulling carts or sleds",
    "height": {
      "imperial": "26 - 30",
      "metric": "66 - 76"
    },
    "id": 225,
    "image": {
      "height": 803,
      "id": "SJJxjecEX",
      "url": "https://cdn2.thedogapi.com/images/SJJxjecEX.jpg",
      "width": 1005
    },
    "life_span": "9 – 14 years",
    "name": "Shiloh Shepherd",
    "reference_image_id": "SJJxjecEX",
    "temperament": "Outgoing, Loyal, Companionable, Gentle, Loving, Trainable",
    "weight": {
      "imperial": "120 - 140",
      "metric": "54 - 64"
    }
  },
  {
    "bred_for": "Sled pulling",
    "breed_group": "Working",
    "height": {
      "imperial": "20 - 23.5",
      "metric": "51 - 60"
    },
    "id": 226,
    "image": {
      "height": 1280,
      "id": "S17ZilqNm",
      "url": "https://cdn2.thedogapi.com/images/S17ZilqNm.jpg",
      "width": 1920
    },
    "life_span": "12 years",
    "name": "Siberian Husky",
    "reference_image_id": "S17ZilqNm",
    "temperament": "Outgoing, Friendly, Alert, Gentle, Intelligent",
    "weight": {
      "imperial": "35 - 60",
      "metric": "16 - 27"
    }
  },
  {
    "bred_for": "Small vermin hunting, companionship",
    "breed_group": "Toy",
    "height": {
      "imperial": "9 - 10",
      "metric": "23 - 25"
    },
    "id": 228,
    "image": {
      "height": 1142,
      "id": "ByzGsl5Nm",
      "url": "https://cdn2.thedogapi.com/images/ByzGsl5Nm.jpg",
      "width": 1599
    },
    "life_span": "12 - 15 years",
    "name": "Silky Terrier",
    "reference_image_id": "ByzGsl5Nm",
    "temperament": "Friendly, Responsive, Inquisitive, Alert, Quick, Joyful",
    "weight": {
      "imperial": "8 - 10",
      "metric": "4 - 5"
    }
  },
  {
    "bred_for": "Fox bolting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "15.5",
      "metric": "39"
    },
    "id": 232,
    "image": {
      "height": 1031,
      "id": "Syszjx9Em",
      "url": "https://cdn2.thedogapi.com/images/Syszjx9Em.jpg",
      "width": 1600
    },
    "life_span": "12 - 14 years",
    "name": "Smooth Fox Terrier",
    "reference_image_id": "Syszjx9Em",
    "temperament": "Fearless, Affectionate, Alert, Playful, Intelligent, Active",
    "weight": {
      "imperial": "up - 18",
      "metric": "NaN - 8"
    }
  },
  {
    "bred_for": "Vermin hunting, guarding, all-around farm helper",
    "breed_group": "Terrier",
    "height": {
      "imperial": "16 - 18",
      "metric": "41 - 46"
    },
    "id": 233,
    "image": {
      "height": 800,
      "id": "HJHmix5NQ",
      "url": "https://cdn2.thedogapi.com/images/HJHmix5NQ.jpg",
      "width": 1200
    },
    "life_span": "12 - 15 years",
    "name": "Soft Coated Wheaten Terrier",
    "reference_image_id": "HJHmix5NQ",
    "temperament": "Affectionate, Spirited, Energetic, Playful, Intelligent, Faithful",
    "weight": {
      "imperial": "30 - 40",
      "metric": "14 - 18"
    }
  },
  {
    "bred_for": "Herding flocks of sheep and goats from one pasture to another",
    "breed_group": "Sporting",
    "height": {
      "imperial": "16 - 20",
      "metric": "41 - 51"
    },
    "id": 235,
    "image": {
      "height": 922,
      "id": "HJf4jl9VX",
      "url": "https://cdn2.thedogapi.com/images/HJf4jl9VX.jpg",
      "width": 1200
    },
    "life_span": "12 - 15 years",
    "name": "Spanish Water Dog",
    "reference_image_id": "HJf4jl9VX",
    "temperament": "Trainable, Diligent, Affectionate, Loyal, Athletic, Intelligent",
    "weight": {
      "imperial": "30 - 50",
      "metric": "14 - 23"
    }
  },
  {
    "breed_group": "Sporting",
    "height": {
      "imperial": "22.5 - 27.5",
      "metric": "57 - 70"
    },
    "id": 236,
    "image": {
      "height": 772,
      "id": "rk5Eoe5Nm",
      "url": "https://cdn2.thedogapi.com/images/rk5Eoe5Nm.jpg",
      "width": 1030
    },
    "life_span": "10 - 12 years",
    "name": "Spinone Italiano",
    "reference_image_id": "rk5Eoe5Nm",
    "temperament": "Docile, Friendly, Affectionate, Loyal, Patient, Gentle",
    "weight": {
      "imperial": "61 - 85",
      "metric": "28 - 39"
    }
  },
  {
    "bred_for": "",
    "breed_group": "Terrier",
    "height": {
      "imperial": "14 - 16",
      "metric": "36 - 41"
    },
    "id": 238,
    "image": {
      "height": 852,
      "id": "H1zSie9V7",
      "url": "https://cdn2.thedogapi.com/images/H1zSie9V7.jpg",
      "width": 1280
    },
    "life_span": "12 - 14 years",
    "name": "Staffordshire Bull Terrier",
    "reference_image_id": "H1zSie9V7",
    "temperament": "Reliable, Fearless, Bold, Affectionate, Loyal, Intelligent, Courageous",
    "weight": {
      "imperial": "24 - 38",
      "metric": "11 - 17"
    }
  },
  {
    "bred_for": "Ratting, guarding",
    "breed_group": "Working",
    "height": {
      "imperial": "17.5 - 19.5",
      "metric": "44 - 50"
    },
    "id": 239,
    "image": {
      "height": 585,
      "id": "tmzeu6ID_",
      "url": "https://cdn2.thedogapi.com/images/tmzeu6ID_.jpg",
      "width": 650
    },
    "life_span": "13 - 15 years",
    "name": "Standard Schnauzer",
    "reference_image_id": "tmzeu6ID_",
    "temperament": "Trainable, Good-natured, Devoted, Lively, Playful, Intelligent",
    "weight": {
      "imperial": "30 - 50",
      "metric": "14 - 23"
    }
  },
  {
    "breed_group": "Herding",
    "height": {
      "imperial": "11.5 - 13.5",
      "metric": "29 - 34"
    },
    "id": 242,
    "image": {
      "height": 851,
      "id": "HJ-Dix94Q",
      "url": "https://cdn2.thedogapi.com/images/HJ-Dix94Q.jpg",
      "width": 1280
    },
    "life_span": "12 - 14 years",
    "name": "Swedish Vallhund",
    "reference_image_id": "HJ-Dix94Q",
    "temperament": "Fearless, Friendly, Energetic, Alert, Intelligent, Watchful",
    "weight": {
      "imperial": "20 - 30",
      "metric": "9 - 14"
    }
  },
  {
    "breed_group": "Hound",
    "height": {
      "imperial": "20 - 24",
      "metric": "51 - 61"
    },
    "id": 243,
    "image": {
      "height": 720,
      "id": "zv89hR-O8",
      "url": "https://cdn2.thedogapi.com/images/zv89hR-O8.jpg",
      "width": 1080
    },
    "life_span": "10 - 12 years",
    "name": "Thai Ridgeback",
    "reference_image_id": "zv89hR-O8",
    "temperament": "Protective, Loyal, Independent, Intelligent, Loving, Familial",
    "weight": {
      "imperial": "35 - 55",
      "metric": "16 - 25"
    }
  },
  {
    "breed_group": "Working",
    "height": {
      "imperial": "24 - 26",
      "metric": "61 - 66"
    },
    "id": 244,
    "image": {
      "height": 1375,
      "id": "SkM9sec47",
      "url": "https://cdn2.thedogapi.com/images/SkM9sec47.jpg",
      "width": 1600
    },
    "life_span": "10 - 14 years",
    "name": "Tibetan Mastiff",
    "reference_image_id": "SkM9sec47",
    "temperament": "Strong Willed, Tenacious, Aloof, Stubborn, Intelligent, Protective",
    "weight": {
      "imperial": "85 - 140",
      "metric": "39 - 64"
    }
  },
  {
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "10",
      "metric": "25"
    },
    "id": 245,
    "image": {
      "height": 825,
      "id": "Hyjcol947",
      "url": "https://cdn2.thedogapi.com/images/Hyjcol947.jpg",
      "width": 1023
    },
    "life_span": "12 - 15 years",
    "name": "Tibetan Spaniel",
    "reference_image_id": "Hyjcol947",
    "temperament": "Willful, Aloof, Assertive, Independent, Playful, Intelligent, Happy",
    "weight": {
      "imperial": "9 - 15",
      "metric": "4 - 7"
    }
  },
  {
    "bred_for": "Good luck charms, mascots, watchdogs, herding dogs, and companions",
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "14 - 17",
      "metric": "36 - 43"
    },
    "id": 246,
    "image": {
      "height": 1226,
      "id": "6f5n_42mB",
      "url": "https://cdn2.thedogapi.com/images/6f5n_42mB.jpg",
      "width": 981
    },
    "life_span": "12 - 15 years",
    "name": "Tibetan Terrier",
    "reference_image_id": "6f5n_42mB",
    "temperament": "Affectionate, Energetic, Amiable, Reserved, Gentle, Sensitive",
    "weight": {
      "imperial": "20 - 24",
      "metric": "9 - 11"
    }
  },
  {
    "breed_group": "Toy",
    "height": {
      "imperial": "8 - 11",
      "metric": "20 - 28"
    },
    "id": 248,
    "image": {
      "height": 1024,
      "id": "B17ase9V7",
      "url": "https://cdn2.thedogapi.com/images/B17ase9V7.jpg",
      "width": 1200
    },
    "life_span": "12 - 15 years",
    "name": "Toy Fox Terrier",
    "reference_image_id": "B17ase9V7",
    "temperament": "Friendly, Spirited, Alert, Loyal, Playful, Intelligent",
    "weight": {
      "imperial": "4 - 9",
      "metric": "2 - 4"
    }
  },
  {
    "breed_group": "Hound",
    "height": {
      "imperial": "20 - 27",
      "metric": "51 - 69"
    },
    "id": 250,
    "image": {
      "height": 1080,
      "id": "SkRpsgc47",
      "url": "https://cdn2.thedogapi.com/images/SkRpsgc47.jpg",
      "width": 1920
    },
    "life_span": "10 - 13 years",
    "name": "Treeing Walker Coonhound",
    "reference_image_id": "SkRpsgc47",
    "temperament": "Clever, Affectionate, Confident, Intelligent, Loving, Trainable",
    "weight": {
      "imperial": "45 - 80",
      "metric": "20 - 36"
    }
  },
  {
    "bred_for": "Pointing and trailing",
    "breed_group": "Sporting",
    "height": {
      "imperial": "21 - 24",
      "metric": "53 - 61"
    },
    "id": 251,
    "image": {
      "height": 1276,
      "id": "r1o0jx9Em",
      "url": "https://cdn2.thedogapi.com/images/r1o0jx9Em.jpg",
      "width": 2269
    },
    "life_span": "10 - 14 years",
    "name": "Vizsla",
    "reference_image_id": "r1o0jx9Em",
    "temperament": "Affectionate, Energetic, Loyal, Gentle, Quiet",
    "weight": {
      "imperial": "50 - 65",
      "metric": "23 - 29"
    }
  },
  {
    "bred_for": "Large game trailing and versatile gundog",
    "breed_group": "Sporting",
    "height": {
      "imperial": "23 - 27",
      "metric": "58 - 69"
    },
    "id": 253,
    "image": {
      "height": 954,
      "id": "SyU12l9V7",
      "url": "https://cdn2.thedogapi.com/images/SyU12l9V7.jpg",
      "width": 901
    },
    "life_span": "12 - 15 years",
    "name": "Weimaraner",
    "reference_image_id": "SyU12l9V7",
    "temperament": "Steady, Aloof, Stubborn, Energetic, Alert, Intelligent, Powerful, Fast",
    "weight": {
      "imperial": "55 - 90",
      "metric": "25 - 41"
    }
  },
  {
    "bred_for": "Flushing and retrieving birds",
    "breed_group": "Sporting",
    "height": {
      "imperial": "17 - 19",
      "metric": "43 - 48"
    },
    "id": 254,
    "image": {
      "height": 944,
      "id": "BJ1gnx5Vm",
      "url": "https://cdn2.thedogapi.com/images/BJ1gnx5Vm.jpg",
      "width": 1331
    },
    "life_span": "12 - 15 years",
    "name": "Welsh Springer Spaniel",
    "reference_image_id": "BJ1gnx5Vm",
    "temperament": "Stubborn, Friendly, Affectionate, Loyal, Playful, Active",
    "weight": {
      "imperial": "35 - 55",
      "metric": "16 - 25"
    }
  },
  {
    "bred_for": "Fox, badger, vermin hunting",
    "breed_group": "Terrier",
    "height": {
      "imperial": "10 - 11",
      "metric": "25 - 28"
    },
    "id": 256,
    "image": {
      "height": 1032,
      "id": "Bkdx2g5Em",
      "url": "https://cdn2.thedogapi.com/images/Bkdx2g5Em.jpg",
      "width": 1065
    },
    "life_span": "15 - 20 years",
    "name": "West Highland White Terrier",
    "reference_image_id": "Bkdx2g5Em",
    "temperament": "Hardy, Friendly, Alert, Independent, Gay, Active, Courageous",
    "weight": {
      "imperial": "15 - 22",
      "metric": "7 - 10"
    }
  },
  {
    "bred_for": "Coursing, racing",
    "breed_group": "Hound",
    "height": {
      "imperial": "18 - 22",
      "metric": "46 - 56"
    },
    "id": 257,
    "image": {
      "height": 1071,
      "id": "Hyv-ne94m",
      "url": "https://cdn2.thedogapi.com/images/Hyv-ne94m.jpg",
      "width": 1600
    },
    "life_span": "12 - 15 years",
    "name": "Whippet",
    "reference_image_id": "Hyv-ne94m",
    "temperament": "Friendly, Affectionate, Lively, Gentle, Intelligent, Quiet",
    "weight": {
      "imperial": "25 - 35",
      "metric": "11 - 16"
    }
  },
  {
    "height": {
      "imperial": "22 - 25",
      "metric": "56 - 64"
    },
    "id": 258,
    "image": {
      "height": 800,
      "id": "r14M3e9E7",
      "url": "https://cdn2.thedogapi.com/images/r14M3e9E7.jpg",
      "width": 1200
    },
    "life_span": "12 – 14 years",
    "name": "White Shepherd",
    "reference_image_id": "r14M3e9E7",
    "temperament": "Self-confidence, Aloof, Fearless, Alert, Companionable, Eager",
    "weight": {
      "imperial": "60 - 85",
      "metric": "27 - 39"
    }
  },
  {
    "bred_for": "Vermin hunting, fox bolting",
    "height": {
      "imperial": "13 - 16",
      "metric": "33 - 41"
    },
    "history": " England",
    "id": 259,
    "image": {
      "height": 795,
      "id": "SJ6f2g9EQ",
      "url": "https://cdn2.thedogapi.com/images/SJ6f2g9EQ.jpg",
      "width": 1000
    },
    "life_span": "13 – 14 years",
    "name": "Wire Fox Terrier",
    "reference_image_id": "SJ6f2g9EQ",
    "temperament": "Fearless, Friendly, Bold, Keen, Alert, Quick",
    "weight": {
      "imperial": "15 - 19",
      "metric": "7 - 9"
    }
  },
  {
    "bred_for": "Gundog, \"swamp-tromping\", Flushing, pointing, and retrieving water fowl & game birds",
    "breed_group": "Sporting",
    "height": {
      "imperial": "20 - 24",
      "metric": "51 - 61"
    },
    "id": 260,
    "image": {
      "height": 1604,
      "id": "Bkam2l9Vm",
      "url": "https://cdn2.thedogapi.com/images/Bkam2l9Vm.jpg",
      "width": 2328
    },
    "life_span": "12 - 14 years",
    "name": "Wirehaired Pointing Griffon",
    "reference_image_id": "Bkam2l9Vm",
    "temperament": "Loyal, Gentle, Vigilant, Trainable, Proud",
    "weight": {
      "imperial": "45 - 70",
      "metric": "20 - 32"
    }
  },
  {
    "breed_group": "Non-Sporting",
    "height": {
      "imperial": "10 - 23",
      "metric": "25 - 58"
    },
    "id": 262,
    "image": {
      "height": 1350,
      "id": "HkNS3gqEm",
      "url": "https://cdn2.thedogapi.com/images/HkNS3gqEm.jpg",
      "width": 1500
    },
    "life_span": "12 - 14 years",
    "name": "Xoloitzcuintli",
    "reference_image_id": "HkNS3gqEm",
    "temperament": "Cheerful, Alert, Companionable, Intelligent, Protective, Calm",
    "weight": {
      "imperial": "9 - 31",
      "metric": "4 - 14"
    }
  },
  {
    "bred_for": "Small vermin hunting",
    "breed_group": "Toy",
    "height": {
      "imperial": "8 - 9",
      "metric": "20 - 23"
    },
    "id": 264,
    "image": {
      "height": 683,
      "id": "B12BnxcVQ",
      "url": "https://cdn2.thedogapi.com/images/B12BnxcVQ.jpg",
      "width": 1024
    },
    "life_span": "12 - 16 years",
    "name": "Yorkshire Terrier",
    "reference_image_id": "B12BnxcVQ",
    "temperament": "Bold, Independent, Confident, Intelligent, Courageous",
    "weight": {
      "imperial": "4 - 7",
      "metric": "2 - 3"
    }
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/Abyssinian.aspx",
    "child_friendly": 3,
    "country_code": "EG",
    "country_codes": "EG",
    "description": "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.",
    "dog_friendly": 4,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "abys",
    "image": {
      "height": 1445,
      "id": "0XYvRd7oD",
      "url": "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg",
      "width": 1204
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "14 - 15",
    "name": "Abyssinian",
    "natural": 1,
    "origin": "Egypt",
    "rare": 0,
    "reference_image_id": "0XYvRd7oD",
    "rex": 0,
    "shedding_level": 2,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Active, Energetic, Independent, Intelligent, Gentle",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/abyssinian",
    "vetstreet_url": "http://www.vetstreet.com/cats/abyssinian",
    "vocalisation": 1,
    "weight": {
      "imperial": "7  -  10",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Abyssinian_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 4,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "GR",
    "country_codes": "GR",
    "description": "Native to the Greek islands known as the Cyclades in the Aegean Sea, these are natural cats, meaning they developed without humans getting involved in their breeding. As a breed, Aegean Cats are rare, although they are numerous on their home islands. They are generally friendly toward people and can be excellent cats for families with children.",
    "dog_friendly": 4,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "aege",
    "image": {
      "height": 800,
      "id": "ozEvzdVM-",
      "url": "https://cdn2.thecatapi.com/images/ozEvzdVM-.jpg",
      "width": 1200
    },
    "indoor": 0,
    "intelligence": 3,
    "life_span": "9 - 12",
    "name": "Aegean",
    "natural": 0,
    "origin": "Greece",
    "rare": 0,
    "reference_image_id": "ozEvzdVM-",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Social, Intelligent, Playful, Active",
    "vetstreet_url": "http://www.vetstreet.com/cats/aegean-cat",
    "vocalisation": 3,
    "weight": {
      "imperial": "7 - 10",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Aegean_cat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/AmericanBobtail.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "American Bobtails are loving and incredibly intelligent cats possessing a distinctive wild appearance. They are extremely interactive cats that bond with their human family with great devotion.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "abob",
    "image": {
      "height": 951,
      "id": "hBXicehMA",
      "url": "https://cdn2.thecatapi.com/images/hBXicehMA.jpg",
      "width": 1600
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "11 - 15",
    "name": "American Bobtail",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "hBXicehMA",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 1,
    "temperament": "Intelligent, Interactive, Lively, Playful, Sensitive",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/american-bobtail",
    "vetstreet_url": "http://www.vetstreet.com/cats/american-bobtail",
    "vocalisation": 3,
    "weight": {
      "imperial": "7 - 16",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/American_Bobtail"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/AmericanCurl.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Distinguished by truly unique ears that curl back in a graceful arc, offering an alert, perky, happily surprised expression, they cause people to break out into a big smile when viewing their first Curl. Curls are very people-oriented, faithful, affectionate soulmates, adjusting remarkably fast to other pets, children, and new situations.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "acur",
    "image": {
      "height": 964,
      "id": "xnsqonbjW",
      "url": "https://cdn2.thecatapi.com/images/xnsqonbjW.jpg",
      "width": 1000
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "12 - 16",
    "name": "American Curl",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "xnsqonbjW",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Curious, Intelligent, Interactive, Lively, Playful, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/american-curl",
    "vetstreet_url": "http://www.vetstreet.com/cats/american-curl",
    "vocalisation": 3,
    "weight": {
      "imperial": "5 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/American_Curl"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Domestic Shorthair",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/AmericanShorthair.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The American Shorthair is known for its longevity, robust health, good looks, sweet personality, and amiability with children, dogs, and other pets.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "asho",
    "image": {
      "height": 1200,
      "id": "JFPROfGtQ",
      "url": "https://cdn2.thecatapi.com/images/JFPROfGtQ.jpg",
      "width": 1600
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "15 - 17",
    "name": "American Shorthair",
    "natural": 1,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "JFPROfGtQ",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Active, Curious, Easy Going, Playful, Calm",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/american-shorthair",
    "vetstreet_url": "http://www.vetstreet.com/cats/american-shorthair",
    "vocalisation": 3,
    "weight": {
      "imperial": "8 - 15",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/American_Shorthair"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/AmericanWirehair.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The American Wirehair tends to be a calm and tolerant cat who takes life as it comes. His favorite hobby is bird-watching from a sunny windowsill, and his hunting ability will stand you in good stead if insects enter the house.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "awir",
    "image": {
      "height": 936,
      "id": "8D--jCd21",
      "url": "https://cdn2.thecatapi.com/images/8D--jCd21.jpg",
      "width": 1280
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "14 - 18",
    "name": "American Wirehair",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "8D--jCd21",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Curious, Gentle, Intelligent, Interactive, Lively, Loyal, Playful, Sensible, Social",
    "vetstreet_url": "http://www.vetstreet.com/cats/american-wirehair",
    "vocalisation": 3,
    "weight": {
      "imperial": "8 - 15",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/American_Wirehair"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Alley cat",
    "child_friendly": 4,
    "country_code": "AE",
    "country_codes": "AE",
    "description": "Arabian Mau cats are social and energetic. Due to their energy levels, these cats do best in homes where their owners will be able to provide them with plenty of playtime, attention and interaction from their owners. These kitties are friendly, intelligent, and adaptable, and will even get along well with other pets and children.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "amau",
    "image": {
      "height": 1554,
      "id": "k71ULYfRr",
      "url": "https://cdn2.thecatapi.com/images/k71ULYfRr.jpg",
      "width": 2048
    },
    "indoor": 0,
    "intelligence": 3,
    "life_span": "12 - 14",
    "name": "Arabian Mau",
    "natural": 1,
    "origin": "United Arab Emirates",
    "rare": 0,
    "reference_image_id": "k71ULYfRr",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Agile, Curious, Independent, Playful, Loyal",
    "vcahospitals_url": "",
    "vocalisation": 1,
    "weight": {
      "imperial": "8 - 16",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_Mau"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Spotted Mist",
    "child_friendly": 4,
    "country_code": "AU",
    "country_codes": "AU",
    "description": "The Australian Mist thrives on human companionship. Tolerant of even the youngest of children, these friendly felines enjoy playing games and being part of the hustle and bustle of a busy household. They make entertaining companions for people of all ages, and are happy to remain indoors between dusk and dawn or to be wholly indoor pets.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "amis",
    "image": {
      "height": 1165,
      "id": "_6x-3TiCA",
      "url": "https://cdn2.thecatapi.com/images/_6x-3TiCA.jpg",
      "width": 1231
    },
    "indoor": 0,
    "intelligence": 4,
    "lap": 1,
    "life_span": "12 - 16",
    "name": "Australian Mist",
    "natural": 0,
    "origin": "Australia",
    "rare": 0,
    "reference_image_id": "_6x-3TiCA",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Lively, Social, Fun-loving, Relaxed, Affectionate",
    "vocalisation": 3,
    "weight": {
      "imperial": "7 - 15",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Australian_Mist"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Long-haired Siamese",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/Balinese.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Balinese are curious, outgoing, intelligent cats with excellent communication skills. They are known for their chatty personalities and are always eager to tell you their views on life, love, and what you’ve served them for dinner. ",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 1,
    "id": "bali",
    "image": {
      "height": 1000,
      "id": "13MkvUreZ",
      "url": "https://cdn2.thecatapi.com/images/13MkvUreZ.jpg",
      "width": 1600
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "10 - 15",
    "name": "Balinese",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "13MkvUreZ",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Intelligent, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/balinese",
    "vetstreet_url": "http://www.vetstreet.com/cats/balinese",
    "vocalisation": 5,
    "weight": {
      "imperial": "4 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Balinese_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Bambino is a breed of cat that was created as a cross between the Sphynx and the Munchkin breeds. The Bambino cat has short legs, large upright ears, and is usually hairless. They love to be handled and cuddled up on the laps of their family members.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 1,
    "grooming": 1,
    "hairless": 1,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "bamb",
    "image": {
      "height": 1030,
      "id": "5AdhMjeEu",
      "url": "https://cdn2.thecatapi.com/images/5AdhMjeEu.jpg",
      "width": 1296
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 14",
    "name": "Bambino",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "5AdhMjeEu",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 1,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Lively, Friendly, Intelligent",
    "vocalisation": 3,
    "weight": {
      "imperial": "4 - 9",
      "metric": "2 - 4"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Bambino_cat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "bidability": 3,
    "cat_friendly": 4,
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/Bengal.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Bengals are a lot of fun to live with, but they're definitely not the cat for everyone, or for first-time cat owners. Extremely intelligent, curious and active, they demand a lot of interaction and woe betide the owner who doesn't provide it.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 1,
    "id": "beng",
    "image": {
      "height": 739,
      "id": "O3btzLlsO",
      "url": "https://cdn2.thecatapi.com/images/O3btzLlsO.png",
      "width": 1100
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 0,
    "life_span": "12 - 15",
    "name": "Bengal",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "O3btzLlsO",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Alert, Agile, Energetic, Demanding, Intelligent",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/bengal",
    "vetstreet_url": "http://www.vetstreet.com/cats/bengal",
    "vocalisation": 5,
    "weight": {
      "imperial": "6 - 12",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Bengal_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Sacred Birman, Sacred Cat Of Burma",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/Birman.aspx",
    "child_friendly": 4,
    "country_code": "FR",
    "country_codes": "FR",
    "description": "The Birman is a docile, quiet cat who loves people and will follow them from room to room. Expect the Birman to want to be involved in what you’re doing. He communicates in a soft voice, mainly to remind you that perhaps it’s time for dinner or maybe for a nice cuddle on the sofa. He enjoys being held and will relax in your arms like a furry baby.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "birm",
    "image": {
      "height": 814,
      "id": "HOrX5gwLS",
      "url": "https://cdn2.thecatapi.com/images/HOrX5gwLS.jpg",
      "width": 1376
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "14 - 15",
    "name": "Birman",
    "natural": 0,
    "origin": "France",
    "rare": 0,
    "reference_image_id": "HOrX5gwLS",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Active, Gentle, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/birman",
    "vetstreet_url": "http://www.vetstreet.com/cats/birman",
    "vocalisation": 1,
    "weight": {
      "imperial": "6 - 15",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Birman"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Small black Panther",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/Bombay.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The the golden eyes and the shiny black coa of the Bopmbay is absolutely striking. Likely to bond most with one family member, the Bombay will follow you from room to room and will almost always have something to say about what you are doing, loving attention and to be carried around, often on his caregiver's shoulder.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "bomb",
    "image": {
      "height": 650,
      "id": "5iYq9NmT1",
      "url": "https://cdn2.thecatapi.com/images/5iYq9NmT1.jpg",
      "width": 1250
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 16",
    "name": "Bombay",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "5iYq9NmT1",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Dependent, Gentle, Intelligent, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/bombay",
    "vetstreet_url": "http://www.vetstreet.com/cats/bombay",
    "vocalisation": 5,
    "weight": {
      "imperial": "6 - 11",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Bombay_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "GB",
    "country_codes": "GB",
    "description": "The British Longhair is a very laid-back relaxed cat, often perceived to be very independent although they will enjoy the company of an equally relaxed and likeminded cat. They are an affectionate breed, but very much on their own terms and tend to prefer to choose to come and sit with their owners rather than being picked up.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 5,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "bslo",
    "image": {
      "height": 960,
      "id": "7isAO4Cav",
      "url": "https://cdn2.thecatapi.com/images/7isAO4Cav.jpg",
      "width": 960
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "12 - 14",
    "name": "British Longhair",
    "natural": 0,
    "origin": "United Kingdom",
    "rare": 0,
    "reference_image_id": "7isAO4Cav",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Easy Going, Independent, Intelligent, Loyal, Social",
    "vocalisation": 1,
    "weight": {
      "imperial": "8 - 18",
      "metric": "4 - 8"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/British_Longhair"
  },
  {
    "adaptability": 5,
    "affection_level": 4,
    "alt_names": "Highlander, Highland Straight, Britannica",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/BritishShorthair.aspx",
    "child_friendly": 4,
    "country_code": "GB",
    "country_codes": "GB",
    "description": "The British Shorthair is a very pleasant cat to have as a companion, ans is easy going and placid. The British is a fiercely loyal, loving cat and will attach herself to every one of her family members. While loving to play, she doesn't need hourly attention. If she is in the mood to play, she will find someone and bring a toy to that person. The British also plays well by herself, and thus is a good companion for single people.",
    "dog_friendly": 5,
    "energy_level": 2,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "bsho",
    "image": {
      "height": 1457,
      "id": "s4wQfYoEk",
      "url": "https://cdn2.thecatapi.com/images/s4wQfYoEk.jpg",
      "width": 1600
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "12 - 17",
    "name": "British Shorthair",
    "natural": 1,
    "origin": "United Kingdom",
    "rare": 0,
    "reference_image_id": "s4wQfYoEk",
    "rex": 0,
    "shedding_level": 4,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 2,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Easy Going, Gentle, Loyal, Patient, calm",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/british-shorthair",
    "vetstreet_url": "http://www.vetstreet.com/cats/british-shorthair",
    "vocalisation": 1,
    "weight": {
      "imperial": "12 - 20",
      "metric": "5 - 9"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/British_Shorthair"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/Burmese.aspx",
    "child_friendly": 4,
    "country_code": "MM",
    "country_codes": "MM",
    "description": "Burmese love being with people, playing with them, and keeping them entertained. They crave close physical contact and abhor an empty lap. They will follow their humans from room to room, and sleep in bed with them, preferably under the covers, cuddled as close as possible. At play, they will turn around to see if their human is watching and being entertained by their crazy antics.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 1,
    "id": "bure",
    "image": {
      "height": 650,
      "id": "4lXnnfxac",
      "url": "https://cdn2.thecatapi.com/images/4lXnnfxac.jpg",
      "width": 1250
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "15 - 16",
    "name": "Burmese",
    "natural": 0,
    "origin": "Burma",
    "rare": 0,
    "reference_image_id": "4lXnnfxac",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Curious, Intelligent, Gentle, Social, Interactive, Playful, Lively",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/burmese",
    "vetstreet_url": "http://www.vetstreet.com/cats/burmese",
    "vocalisation": 5,
    "weight": {
      "imperial": "6 - 12",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Burmese_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsAB/Burmilla.aspx",
    "child_friendly": 4,
    "country_code": "GB",
    "country_codes": "GB",
    "description": "The Burmilla is a fairly placid cat. She tends to be an easy cat to get along with, requiring minimal care. The Burmilla is affectionate and sweet and makes a good companion, the Burmilla is an ideal companion to while away a lonely evening. Loyal, devoted, and affectionate, this cat will stay by its owner, always keeping them company.",
    "dog_friendly": 4,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "buri",
    "image": {
      "height": 960,
      "id": "jvg3XfEdC",
      "url": "https://cdn2.thecatapi.com/images/jvg3XfEdC.jpg",
      "width": 960
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "10 - 15",
    "name": "Burmilla",
    "natural": 0,
    "origin": "United Kingdom",
    "rare": 0,
    "reference_image_id": "jvg3XfEdC",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Easy Going, Friendly, Intelligent, Lively, Playful, Social",
    "vetstreet_url": "http://www.vetstreet.com/cats/burmilla",
    "vocalisation": 5,
    "weight": {
      "imperial": "6 - 13",
      "metric": "3 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Burmilla"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Spangle",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Perhaps the only thing about the California spangled cat that isn’t wild-like is its personality. Known to be affectionate, gentle and sociable, this breed enjoys spending a great deal of time with its owners. They are very playful, often choosing to perch in high locations and show off their acrobatic skills.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "cspa",
    "image": {
      "height": 688,
      "id": "B1ERTmgph",
      "url": "https://cdn2.thecatapi.com/images/B1ERTmgph.jpg",
      "width": 1200
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "10 - 14",
    "name": "California Spangled",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "B1ERTmgph",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Curious, Intelligent, Loyal, Social",
    "vocalisation": 1,
    "weight": {
      "imperial": "10 - 15",
      "metric": "5 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/California_Spangled"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Chantilly, Foreign Longhair",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Chantilly is a devoted companion and prefers company to being left alone. While the Chantilly is not demanding, she will \"chirp\" and \"talk\" as if having a conversation. This breed is affectionate, with a sweet temperament. It can stay still for extended periods, happily lounging in the lap of its loved one. This quality makes the Tiffany an ideal traveling companion, and an ideal house companion for senior citizens and the physically handicapped.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 5,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "ctif",
    "image": {
      "height": 2938,
      "id": "TR-5nAd_S",
      "url": "https://cdn2.thecatapi.com/images/TR-5nAd_S.jpg",
      "width": 2901
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "14 - 16",
    "name": "Chantilly-Tiffany",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "TR-5nAd_S",
    "rex": 0,
    "shedding_level": 5,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Demanding, Interactive, Loyal",
    "vocalisation": 5,
    "weight": {
      "imperial": "7 - 12",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Chantilly-Tiffany"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/Chartreux.aspx",
    "child_friendly": 4,
    "country_code": "FR",
    "country_codes": "FR",
    "description": "The Chartreux is generally silent but communicative. Short play sessions, mixed with naps and meals are their perfect day. Whilst appreciating any attention you give them, they are not demanding, content instead to follow you around devotedly, sleep on your bed and snuggle with you if you’re not feeling well.",
    "dog_friendly": 5,
    "energy_level": 2,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 1,
    "id": "char",
    "image": {
      "height": 1024,
      "id": "j6oFGLpRG",
      "url": "https://cdn2.thecatapi.com/images/j6oFGLpRG.jpg",
      "width": 768
    },
    "indoor": 0,
    "intelligence": 4,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Chartreux",
    "natural": 0,
    "origin": "France",
    "rare": 0,
    "reference_image_id": "j6oFGLpRG",
    "rex": 1,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Loyal, Intelligent, Social, Lively, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/chartreux",
    "vetstreet_url": "http://www.vetstreet.com/cats/chartreux",
    "vocalisation": 1,
    "weight": {
      "imperial": "6 - 15",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Chartreux"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Nile Cat",
    "child_friendly": 4,
    "country_code": "EG",
    "country_codes": "EG",
    "description": "For those owners who desire a feline capable of evoking the great outdoors, the strikingly beautiful Chausie retains a bit of the wild in its appearance but has the house manners of our friendly, familiar moggies. Very playful, this cat needs a large amount of space to be able to fully embrace its hunting instincts.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 1,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "chau",
    "image": {
      "height": 786,
      "id": "vJ3lEYgXr",
      "url": "https://cdn2.thecatapi.com/images/vJ3lEYgXr.jpg",
      "width": 1100
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "12 - 14",
    "name": "Chausie",
    "natural": 0,
    "origin": "Egypt",
    "rare": 0,
    "reference_image_id": "vJ3lEYgXr",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Intelligent, Playful, Social",
    "vocalisation": 1,
    "weight": {
      "imperial": "7 - 15",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Chausie"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": " ",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Cheetoh has a super affectionate nature and real love for their human companions; they are intelligent with the ability to learn quickly. You can expect that a Cheetoh will be a fun-loving kitty who enjoys playing, running, and jumping through every room in your house.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "chee",
    "image": {
      "height": 973,
      "id": "IFXsxmXLm",
      "url": "https://cdn2.thecatapi.com/images/IFXsxmXLm.jpg",
      "width": 973
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "12 - 14",
    "name": "Cheetoh",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "IFXsxmXLm",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Gentle, Intelligent, Social",
    "vocalisation": 5,
    "weight": {
      "imperial": "8 - 15",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Bengal_cat#Cheetoh"
  },
  {
    "adaptability": 3,
    "affection_level": 4,
    "alt_names": "",
    "bidability": 4,
    "cat_friendly": 3,
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/ColorpointShorthair.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Colorpoint Shorthairs are an affectionate breed, devoted and loyal to their people. Sensitive to their owner’s moods, Colorpoints are more than happy to sit at your side or on your lap and purr words of encouragement on a bad day. They will constantly seek out your lap whenever it is open and in the moments when your lap is preoccupied they will stretch out in sunny spots on the ground.",
    "dog_friendly": 4,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "csho",
    "image": {
      "height": 1600,
      "id": "oSpqGyUDS",
      "url": "https://cdn2.thecatapi.com/images/oSpqGyUDS.jpg",
      "width": 1363
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 16",
    "name": "Colorpoint Shorthair",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "oSpqGyUDS",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 2,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Intelligent, Playful, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/colorpoint-shorthair",
    "vocalisation": 5,
    "weight": {
      "imperial": "4 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Colorpoint_Shorthair"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cat_friendly": 2,
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/CornishRex.aspx",
    "child_friendly": 4,
    "country_code": "GB",
    "country_codes": "GB",
    "description": "This is a confident cat who loves people and will follow them around, waiting for any opportunity to sit in a lap or give a kiss. He enjoys being handled, making it easy to take him to the veterinarian or train him for therapy work. The Cornish Rex stay in kitten mode most of their lives and well into their senior years. ",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 1,
    "id": "crex",
    "image": {
      "height": 1784,
      "id": "unX21IBVB",
      "url": "https://cdn2.thecatapi.com/images/unX21IBVB.jpg",
      "width": 2976
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "11 - 14",
    "name": "Cornish Rex",
    "natural": 0,
    "origin": "United Kingdom",
    "rare": 0,
    "reference_image_id": "unX21IBVB",
    "rex": 1,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Intelligent, Active, Curious, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/cornish-rex",
    "vetstreet_url": "http://www.vetstreet.com/cats/cornish-rex",
    "vocalisation": 1,
    "weight": {
      "imperial": "5 - 9",
      "metric": "2 - 4"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Cornish_Rex"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Spangle",
    "child_friendly": 4,
    "country_code": "CA",
    "country_codes": "CA",
    "description": "The Cymric is a placid, sweet cat. They do not get too upset about anything that happens in their world. They are loving companions and adore people. They are smart and dexterous, capable of using his paws to get into cabinets or to open doors.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "cymr",
    "image": {
      "height": 900,
      "id": "3dbtapCWM",
      "url": "https://cdn2.thecatapi.com/images/3dbtapCWM.jpg",
      "width": 1440
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "8 - 14",
    "name": "Cymric",
    "natural": 0,
    "origin": "Canada",
    "rare": 0,
    "reference_image_id": "3dbtapCWM",
    "rex": 0,
    "shedding_level": 5,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 1,
    "temperament": "Gentle, Loyal, Intelligent, Playful",
    "vetstreet_url": "http://www.vetstreet.com/cats/cymric",
    "vocalisation": 3,
    "weight": {
      "imperial": "8 - 13",
      "metric": "4 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Cymric_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Cypriot cat",
    "child_friendly": 4,
    "country_code": "CY",
    "country_codes": "CY",
    "description": "Loving, loyal, social and inquisitive, the Cyprus cat forms strong ties with their families and love nothing more than to be involved in everything that goes on in their surroundings. They are not overly active by nature which makes them the perfect companion for people who would like to share their homes with a laid-back relaxed feline companion. ",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "cypr",
    "image": {
      "height": 768,
      "id": "tJbzb7FKo",
      "url": "https://cdn2.thecatapi.com/images/tJbzb7FKo.jpg",
      "width": 1024
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Cyprus",
    "natural": 1,
    "origin": "Cyprus",
    "rare": 0,
    "reference_image_id": "tJbzb7FKo",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Social",
    "vocalisation": 3,
    "weight": {
      "imperial": "8 - 16",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Cyprus_cat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Pixie cat, Alien cat, Poodle cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/DevonRex.aspx",
    "child_friendly": 4,
    "country_code": "GB",
    "country_codes": "GB",
    "description": "The favourite perch of the Devon Rex is right at head level, on the shoulder of her favorite person. She takes a lively interest in everything that is going on and refuses to be left out of any activity. Count on her to stay as close to you as possible, occasionally communicating his opinions in a quiet voice. She loves people and welcomes the attentions of friends and family alike.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 1,
    "id": "drex",
    "image": {
      "height": 1160,
      "id": "4RzEwvyzz",
      "url": "https://cdn2.thecatapi.com/images/4RzEwvyzz.png",
      "width": 1729
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "10 - 15",
    "name": "Devon Rex",
    "natural": 0,
    "origin": "United Kingdom",
    "rare": 0,
    "reference_image_id": "4RzEwvyzz",
    "rex": 1,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Highly interactive, Mischievous, Loyal, Social, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/devon-rex",
    "vetstreet_url": "http://www.vetstreet.com/cats/devon-rex",
    "vocalisation": 1,
    "weight": {
      "imperial": "5 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Devon_Rex"
  },
  {
    "adaptability": 4,
    "affection_level": 4,
    "cat_friendly": 3,
    "child_friendly": 3,
    "country_code": "RU",
    "country_codes": "RU",
    "description": "Donskoy are affectionate, intelligent, and easy-going. They demand lots of attention and interaction. The Donskoy also gets along well with other pets. It is now thought the same gene that causes degrees of hairlessness in the Donskoy also causes alterations in cat personality, making them calmer the less hair they have.",
    "dog_friendly": 3,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 2,
    "hairless": 1,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "dons",
    "image": {
      "height": 750,
      "id": "3KG57GfMW",
      "url": "https://cdn2.thecatapi.com/images/3KG57GfMW.jpg",
      "width": 750
    },
    "indoor": 0,
    "intelligence": 3,
    "life_span": "12 - 15",
    "name": "Donskoy",
    "natural": 0,
    "origin": "Russia",
    "rare": 1,
    "reference_image_id": "3KG57GfMW",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Playful, affectionate, loyal, social",
    "vocalisation": 2,
    "weight": {
      "imperial": "10 - 12",
      "metric": "5 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Donskoy_(cat)"
  },
  {
    "adaptability": 3,
    "affection_level": 3,
    "alt_names": "Chinese Lia Hua, Lí hua māo (貍花貓), Li Hua",
    "cat_friendly": 3,
    "child_friendly": 3,
    "country_code": "CN",
    "country_codes": "CN",
    "description": "The Dragon Li is loyal, but not particularly affectionate. They are known to be very intelligent, and their natural breed status means that they're very active. She is is gentle with people, and has a reputation as a talented hunter of rats and other vermin.",
    "dog_friendly": 3,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "lihu",
    "image": {
      "height": 1080,
      "id": "BQMSld0A0",
      "url": "https://cdn2.thecatapi.com/images/BQMSld0A0.jpg",
      "width": 1080
    },
    "indoor": 1,
    "intelligence": 3,
    "life_span": "12 - 15",
    "name": "Dragon Li",
    "natural": 1,
    "origin": "China",
    "rare": 0,
    "reference_image_id": "BQMSld0A0",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Intelligent, Friendly, Gentle, Loving, Loyal",
    "vetstreet_url": "http://www.vetstreet.com/cats/li-hua",
    "vocalisation": 3,
    "weight": {
      "imperial": "9 - 12",
      "metric": "4 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Dragon_Li"
  },
  {
    "adaptability": 2,
    "affection_level": 5,
    "alt_names": "Pharaoh Cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/EgyptianMau.aspx",
    "child_friendly": 3,
    "country_code": "EG",
    "country_codes": "EG",
    "description": "The Egyptian Mau is gentle and reserved. She loves her people and desires attention and affection from them but is wary of others. Early, continuing socialization is essential with this sensitive and sometimes shy cat, especially if you plan to show or travel with her. Otherwise, she can be easily startled by unexpected noises or events.",
    "dog_friendly": 3,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "emau",
    "image": {
      "height": 2147,
      "id": "TuSyTkt2n",
      "url": "https://cdn2.thecatapi.com/images/TuSyTkt2n.jpg",
      "width": 2475
    },
    "indoor": 0,
    "intelligence": 4,
    "lap": 1,
    "life_span": "18 - 20",
    "name": "Egyptian Mau",
    "natural": 1,
    "origin": "Egypt",
    "rare": 0,
    "reference_image_id": "TuSyTkt2n",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 2,
    "suppressed_tail": 0,
    "temperament": "Agile, Dependent, Gentle, Intelligent, Lively, Loyal, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/egyptian-mau",
    "vetstreet_url": "http://www.vetstreet.com/cats/egyptian-mau",
    "vocalisation": 3,
    "weight": {
      "imperial": "6 - 14",
      "metric": "3 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Egyptian_Mau"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Exotic",
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/Exotic.aspx",
    "child_friendly": 3,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Exotic Shorthair is a gentle friendly cat that has the same personality as the Persian. They love having fun, don’t mind the company of other cats and dogs, also love to curl up for a sleep in a safe place. Exotics love their own people, but around strangers they are cautious at first. Given time, they usually warm up to visitors.",
    "dog_friendly": 3,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "esho",
    "image": {
      "height": 768,
      "id": "YnPrYEmfe",
      "url": "https://cdn2.thecatapi.com/images/YnPrYEmfe.jpg",
      "width": 1024
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Exotic Shorthair",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "YnPrYEmfe",
    "rex": 0,
    "shedding_level": 2,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 2,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Sweet, Loyal, Quiet, Peaceful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/exotic-shorthair",
    "vetstreet_url": "http://www.vetstreet.com/cats/exotic-shorthair",
    "vocalisation": 1,
    "weight": {
      "imperial": "7 - 14",
      "metric": "3 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Exotic_Shorthair"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Havana, HB",
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/HavanaBrown.aspx",
    "child_friendly": 4,
    "country_code": "GB",
    "country_codes": "GB",
    "description": "The Havana Brown is human oriented, playful, and curious. She has a strong desire to spend time with her people and involve herself in everything they do. Being naturally inquisitive, the Havana Brown reaches out with a paw to touch and feel when investigating curiosities in its environment. They are truly sensitive by nature and frequently gently touch their human companions as if they are extending a paw of friendship.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "hbro",
    "image": {
      "height": 823,
      "id": "njK25knLH",
      "url": "https://cdn2.thecatapi.com/images/njK25knLH.jpg",
      "width": 1024
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "10 - 15",
    "name": "Havana Brown",
    "natural": 0,
    "origin": "United Kingdom",
    "rare": 0,
    "reference_image_id": "njK25knLH",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Curious, Demanding, Friendly, Intelligent, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/havana-brown",
    "vetstreet_url": "http://www.vetstreet.com/cats/havana-brown",
    "vocalisation": 1,
    "weight": {
      "imperial": "6 - 10",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Havana_Brown"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Himalayan Persian, Colourpoint Persian, Longhaired Colourpoint, Himmy",
    "child_friendly": 2,
    "country_code": "US",
    "country_codes": "US",
    "description": "Calm and devoted, Himalayans make excellent companions, though they prefer a quieter home. They are playful in a sedate kind of way and enjoy having an assortment of toys. The Himalayan will stretch out next to you, sleep in your bed and even sit on your lap when she is in the mood.",
    "dog_friendly": 2,
    "energy_level": 1,
    "experimental": 0,
    "grooming": 5,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "hima",
    "image": {
      "height": 961,
      "id": "CDhOtM-Ig",
      "url": "https://cdn2.thecatapi.com/images/CDhOtM-Ig.jpg",
      "width": 1200
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "9 - 15",
    "name": "Himalayan",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "CDhOtM-Ig",
    "rex": 0,
    "shedding_level": 4,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 2,
    "suppressed_tail": 0,
    "temperament": "Dependent, Gentle, Intelligent, Quiet, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/himalayan",
    "vetstreet_url": "http://www.vetstreet.com/cats/himalayan",
    "vocalisation": 1,
    "weight": {
      "imperial": "7 - 14",
      "metric": "3 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Himalayan_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Japanese Truncated Cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsCJ/JapaneseBobtail.aspx",
    "child_friendly": 4,
    "country_code": "JP",
    "country_codes": "JP",
    "description": "The Japanese Bobtail is an active, sweet, loving and highly intelligent breed. They love to be with people and play seemingly endlessly. They learn their name and respond to it. They bring toys to people and play fetch with a favorite toy for hours. Bobtails are social and are at their best when in the company of people. They take over the house and are not intimidated. If a dog is in the house, Bobtails assume Bobtails are in charge.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "jbob",
    "image": {
      "height": 750,
      "id": "-tm9-znzl",
      "url": "https://cdn2.thecatapi.com/images/-tm9-znzl.jpg",
      "width": 1125
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "14 - 16",
    "name": "Japanese Bobtail",
    "natural": 1,
    "origin": "Japan",
    "rare": 0,
    "reference_image_id": "-tm9-znzl",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 1,
    "temperament": "Active, Agile, Clever, Easy Going, Intelligent, Lively, Loyal, Playful, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/japanese-bobtail",
    "vetstreet_url": "http://www.vetstreet.com/cats/japanese-bobtail",
    "vocalisation": 5,
    "weight": {
      "imperial": "5 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Japanese_Bobtail"
  },
  {
    "adaptability": 4,
    "affection_level": 5,
    "alt_names": " ",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Javanese are endlessly interested, intelligent and active. They tend to enjoy jumping to great heights, playing with fishing pole-type or other interactive toys and just generally investigating their surroundings. He will attempt to copy things you do, such as opening doors or drawers.",
    "dog_friendly": 4,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 1,
    "id": "java",
    "image": {
      "height": 1287,
      "id": "xoI_EpOKe",
      "url": "https://cdn2.thecatapi.com/images/xoI_EpOKe.jpg",
      "width": 1232
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "10 - 12",
    "name": "Javanese",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "xoI_EpOKe",
    "rex": 0,
    "shedding_level": 2,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Active, Devoted, Intelligent, Playful",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/javanese",
    "vetstreet_url": "http://www.vetstreet.com/cats/javanese",
    "vocalisation": 5,
    "weight": {
      "imperial": "5 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Javanese_cat"
  },
  {
    "adaptability": 4,
    "affection_level": 4,
    "alt_names": "Diamond Eye cat",
    "cat_friendly": 3,
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/KhaoManee.aspx",
    "child_friendly": 3,
    "country_code": "TH",
    "country_codes": "TH",
    "description": "The Khao Manee is highly intelligent, with an extrovert and inquisitive nature, however they are also very calm and relaxed, making them an idea lap cat.",
    "dog_friendly": 3,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "khao",
    "image": {
      "height": 1037,
      "id": "165ok6ESN",
      "url": "https://cdn2.thecatapi.com/images/165ok6ESN.jpg",
      "width": 1555
    },
    "indoor": 0,
    "intelligence": 4,
    "lap": 1,
    "life_span": "10 - 12",
    "name": "Khao Manee",
    "natural": 0,
    "origin": "Thailand",
    "rare": 0,
    "reference_image_id": "165ok6ESN",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Calm, Relaxed, Talkative, Playful, Warm",
    "vocalisation": 5,
    "weight": {
      "imperial": "8 - 12",
      "metric": "4 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Khao_Manee"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/Korat.aspx",
    "child_friendly": 4,
    "country_code": "TH",
    "country_codes": "TH",
    "description": "The Korat is a natural breed, and one of the oldest stable cat breeds. They are highly intelligent and confident cats that can be fearless, although they are startled by loud sounds and sudden movements. Korats form strong bonds with their people and like to cuddle and stay nearby.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "kora",
    "image": {
      "height": 627,
      "id": "DbwiefiaY",
      "url": "https://cdn2.thecatapi.com/images/DbwiefiaY.png",
      "width": 1200
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "10 - 15",
    "name": "Korat",
    "natural": 0,
    "origin": "Thailand",
    "rare": 1,
    "reference_image_id": "DbwiefiaY",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 2,
    "suppressed_tail": 0,
    "temperament": "Active, Loyal, highly intelligent, Expressive, Trainable",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/korat",
    "vetstreet_url": "http://www.vetstreet.com/cats/korat",
    "vocalisation": 3,
    "weight": {
      "imperial": "7 - 11",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Korat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "child_friendly": 5,
    "country_code": "RU",
    "country_codes": "RU",
    "description": "The character of the Kurilian Bobtail is independent, highly intelligent, clever, inquisitive, sociable, playful, trainable, absent of aggression and very gentle. They are devoted to their humans and when allowed are either on the lap of or sleeping in bed with their owners.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "kuri",
    "image": {
      "height": 750,
      "id": "NZpO4pU56M",
      "url": "https://cdn2.thecatapi.com/images/NZpO4pU56M.jpg",
      "width": 750
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "15 - 20",
    "name": "Kurilian",
    "natural": 1,
    "origin": "Russia",
    "rare": 0,
    "reference_image_id": "NZpO4pU56M",
    "rex": 0,
    "shedding_level": 2,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 1,
    "temperament": "Independent, highly intelligent, clever, inquisitive, sociable, playful, trainable",
    "vetstreet_url": "http://www.vetstreet.com/cats/kurilian-bobtail",
    "vocalisation": 3,
    "weight": {
      "imperial": "8 - 15",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Kurilian_Bobtail"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Si-Sawat",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/LaPerm.aspx",
    "child_friendly": 4,
    "country_code": "TH",
    "country_codes": "TH",
    "description": "LaPerms are gentle and affectionate but also very active. Unlike many active breeds, the LaPerm is also quite content to be a lap cat. The LaPerm will often follow your lead; that is, if they are busy playing and you decide to sit and relax, simply pick up your LaPerm and sit down with it, and it will stay in your lap, devouring the attention you give it.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 1,
    "id": "lape",
    "image": {
      "height": 890,
      "id": "aKbsEYjSl",
      "url": "https://cdn2.thecatapi.com/images/aKbsEYjSl.jpg",
      "width": 1074
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "10 - 15",
    "name": "LaPerm",
    "natural": 0,
    "origin": "Thailand",
    "rare": 0,
    "reference_image_id": "aKbsEYjSl",
    "rex": 1,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Friendly, Gentle, Intelligent, Playful, Quiet",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/laperm",
    "vetstreet_url": "http://www.vetstreet.com/cats/laperm",
    "vocalisation": 3,
    "weight": {
      "imperial": "6 - 10",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/LaPerm"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Coon Cat, Maine Cat, Maine Shag, Snowshoe Cat, American Longhair, The Gentle Giants",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/MaineCoon.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "They are known for their size and luxurious long coat Maine Coons are considered a gentle giant. The good-natured and affable Maine Coon adapts well to many lifestyles and personalities. She likes being with people and has the habit of following them around, but isn’t needy. Most Maine Coons love water and they can be quite good swimmers.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "mcoo",
    "image": {
      "height": 1080,
      "id": "OOD3VXAQn",
      "url": "https://cdn2.thecatapi.com/images/OOD3VXAQn.jpg",
      "width": 1080
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Maine Coon",
    "natural": 1,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "OOD3VXAQn",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Adaptable, Intelligent, Loving, Gentle, Independent",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/maine-coon",
    "vetstreet_url": "http://www.vetstreet.com/cats/maine-coon",
    "vocalisation": 1,
    "weight": {
      "imperial": "12 - 18",
      "metric": "5 - 8"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Maine_Coon"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Manks, Stubbin, Rumpy",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/Manx.aspx",
    "child_friendly": 4,
    "country_code": "IM",
    "country_codes": "IM",
    "description": "The Manx is a placid, sweet cat that is gentle and playful. She never seems to get too upset about anything. She is a loving companion and adores being with people.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "manx",
    "image": {
      "height": 466,
      "id": "fhYh2PDcC",
      "url": "https://cdn2.thecatapi.com/images/fhYh2PDcC.jpg",
      "width": 700
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 14",
    "name": "Manx",
    "natural": 1,
    "origin": "Isle of Man",
    "rare": 0,
    "reference_image_id": "fhYh2PDcC",
    "rex": 0,
    "shedding_level": 5,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 1,
    "temperament": "Easy Going, Intelligent, Loyal, Playful, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/manx",
    "vetstreet_url": "http://www.vetstreet.com/cats/manx",
    "vocalisation": 3,
    "weight": {
      "imperial": "7 - 13",
      "metric": "3 - 6"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Manx_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Munchkin is an outgoing cat who enjoys being handled. She has lots of energy and is faster and more agile than she looks. The shortness of their legs does not seem to interfere with their running and leaping abilities.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "munc",
    "image": {
      "height": 1200,
      "id": "j5cVSqLer",
      "url": "https://cdn2.thecatapi.com/images/j5cVSqLer.jpg",
      "width": 1600
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "10 - 15",
    "name": "Munchkin",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "j5cVSqLer",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 1,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Agile, Easy Going, Intelligent, Playful",
    "vetstreet_url": "http://www.vetstreet.com/cats/munchkin",
    "vocalisation": 3,
    "weight": {
      "imperial": "5 - 9",
      "metric": "2 - 4"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Munchkin_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Longhaired Russian Blue",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Nebelung may have a reserved nature, but she loves to play (being especially fond of retrieving) and enjoys jumping or climbing to high places where she can study people and situations at her leisure before making up her mind about whether she wants to get involved.",
    "dog_friendly": 4,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "nebe",
    "image": {
      "height": 862,
      "id": "OGTWqNNOt",
      "url": "https://cdn2.thecatapi.com/images/OGTWqNNOt.jpg",
      "width": 1150
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "11 - 16",
    "name": "Nebelung",
    "natural": 0,
    "origin": "United States",
    "rare": 1,
    "reference_image_id": "OGTWqNNOt",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Gentle, Quiet, Shy, Playful",
    "vocalisation": 1,
    "weight": {
      "imperial": "7 - 11",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Nebelung"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Skogkatt / Skaukatt, Norsk Skogkatt / Norsk Skaukatt, Weegie",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/NorwegianForestCat.aspx",
    "child_friendly": 4,
    "country_code": "NO",
    "country_codes": "NO",
    "description": "The Norwegian Forest Cat is a sweet, loving cat. She appreciates praise and loves to interact with her parent. She makes a loving companion and bonds with her parents once she accepts them for her own. She is still a hunter at heart. She loves to chase toys as if they are real. She is territorial and patrols several times each day to make certain that all is fine.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "norw",
    "image": {
      "height": 1021,
      "id": "06dgGmEOV",
      "url": "https://cdn2.thecatapi.com/images/06dgGmEOV.jpg",
      "width": 1200
    },
    "indoor": 0,
    "intelligence": 4,
    "life_span": "12 - 16",
    "name": "Norwegian Forest Cat",
    "natural": 1,
    "origin": "Norway",
    "rare": 0,
    "reference_image_id": "06dgGmEOV",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Sweet, Active, Intelligent, Social, Playful, Lively, Curious",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/norwegian-forest-cat",
    "vetstreet_url": "http://www.vetstreet.com/cats/norwegian-forest-cat",
    "vocalisation": 1,
    "weight": {
      "imperial": "8 - 16",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Norwegian_Forest_Cat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/Ocicat.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Loyal and devoted to their owners, the Ocicat is intelligent, confident, outgoing, and seems to have many dog traits. They can be trained to fetch toys, walk on a lead, taught to 'speak', come when called, and follow other commands. ",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 1,
    "id": "ocic",
    "image": {
      "height": 853,
      "id": "JAx-08Y0n",
      "url": "https://cdn2.thecatapi.com/images/JAx-08Y0n.jpg",
      "width": 1280
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "12 - 14",
    "name": "Ocicat",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "JAx-08Y0n",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Active, Agile, Curious, Demanding, Friendly, Gentle, Lively, Playful, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/ocicat",
    "vetstreet_url": "http://www.vetstreet.com/cats/ocicat",
    "vocalisation": 3,
    "weight": {
      "imperial": "7 - 15",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Ocicat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Foreign Type",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/Oriental.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Orientals are passionate about the people in their lives. They become extremely attached to their humans, so be prepared for a lifetime commitment. When you are not available to entertain her, an Oriental will divert herself by jumping on top of the refrigerator, opening drawers, seeking out new hideaways.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 1,
    "id": "orie",
    "image": {
      "height": 1200,
      "id": "LutjkZJpH",
      "url": "https://cdn2.thecatapi.com/images/LutjkZJpH.jpg",
      "width": 800
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 14",
    "name": "Oriental",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "LutjkZJpH",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Energetic, Affectionate, Intelligent, Social, Playful, Curious",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/oriental",
    "vetstreet_url": "http://www.vetstreet.com/cats/oriental",
    "vocalisation": 5,
    "weight": {
      "imperial": "5 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Oriental_Shorthair"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Companionable and affectionate, the Pixie-bob wants to be an integral part of the family. The Pixie-Bob’s ability to bond with their humans along with their patient personas make them excellent companions for children.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "pixi",
    "image": {
      "height": 683,
      "id": "z7fJRNeN6",
      "url": "https://cdn2.thecatapi.com/images/z7fJRNeN6.jpg",
      "width": 1024
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "13 - 16",
    "name": "Pixie-bob",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "z7fJRNeN6",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 1,
    "temperament": "Affectionate, Social, Intelligent, Loyal",
    "vetstreet_url": "http://www.vetstreet.com/cats/pixiebob",
    "vocalisation": 1,
    "weight": {
      "imperial": "8 - 17",
      "metric": "4 - 8"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Pixiebob"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/Ragamuffin.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Ragamuffin is calm, even tempered and gets along well with all family members. Changes in routine generally do not upset her. She is an ideal companion for those in apartments, and with children due to her patient nature.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "raga",
    "image": {
      "height": 2000,
      "id": "SMuZx-bFM",
      "url": "https://cdn2.thecatapi.com/images/SMuZx-bFM.jpg",
      "width": 3000
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 16",
    "name": "Ragamuffin",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "SMuZx-bFM",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Friendly, Gentle, Calm",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/ragamuffin",
    "vetstreet_url": "http://www.vetstreet.com/cats/ragamuffin",
    "vocalisation": 1,
    "weight": {
      "imperial": "8 - 20",
      "metric": "4 - 9"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Ragamuffin_cat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Rag doll",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/Ragdoll.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Ragdolls love their people, greeting them at the door, following them around the house, and leaping into a lap or snuggling in bed whenever given the chance. They are the epitome of a lap cat, enjoy being carried and collapsing into the arms of anyone who holds them.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 3,
    "hypoallergenic": 0,
    "id": "ragd",
    "image": {
      "height": 1024,
      "id": "oGefY4YoG",
      "url": "https://cdn2.thecatapi.com/images/oGefY4YoG.jpg",
      "width": 768
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "12 - 17",
    "name": "Ragdoll",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "oGefY4YoG",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Friendly, Gentle, Quiet, Easygoing",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/ragdoll",
    "vetstreet_url": "http://www.vetstreet.com/cats/ragdoll",
    "vocalisation": 1,
    "weight": {
      "imperial": "12 - 20",
      "metric": "5 - 9"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Ragdoll"
  },
  {
    "adaptability": 3,
    "affection_level": 3,
    "alt_names": "Archangel Blue, Archangel Cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsKthruR/RussianBlue.aspx",
    "child_friendly": 3,
    "country_code": "RU",
    "country_codes": "RU",
    "description": "Russian Blues are very loving and reserved. They do not like noisy households but they do like to play and can be quite active when outdoors. They bond very closely with their owner and are known to be compatible with other pets.",
    "dog_friendly": 3,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 1,
    "id": "rblu",
    "image": {
      "height": 853,
      "id": "Rhj-JsTLP",
      "url": "https://cdn2.thecatapi.com/images/Rhj-JsTLP.jpg",
      "width": 1280
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "10 - 16",
    "name": "Russian Blue",
    "natural": 1,
    "origin": "Russia",
    "rare": 0,
    "reference_image_id": "Rhj-JsTLP",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 1,
    "suppressed_tail": 0,
    "temperament": "Active, Dependent, Easy Going, Gentle, Intelligent, Loyal, Playful, Quiet",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/russian-blue",
    "vetstreet_url": "http://www.vetstreet.com/cats/russian-blue-nebelung",
    "vocalisation": 1,
    "weight": {
      "imperial": "5 - 11",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Russian_Blue"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "Savannah is the feline version of a dog. Actively seeking social interaction, they are given to pouting if left out. Remaining kitten-like through life. Profoundly loyal to immediate family members whilst questioning the presence of strangers. Making excellent companions that are loyal, intelligent and eager to be involved.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 1,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "sava",
    "image": {
      "height": 1100,
      "id": "a8nIYvs6S",
      "url": "https://cdn2.thecatapi.com/images/a8nIYvs6S.jpg",
      "width": 850
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "17 - 20",
    "name": "Savannah",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "a8nIYvs6S",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Curious, Social, Intelligent, Loyal, Outgoing, Adventurous, Affectionate",
    "vetstreet_url": "http://www.vetstreet.com/cats/savannah",
    "vocalisation": 1,
    "weight": {
      "imperial": "8 - 25",
      "metric": "4 - 11"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Savannah_cat"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Scot Fold",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/ScottishFold.aspx",
    "child_friendly": 4,
    "country_code": "GB",
    "country_codes": "GB",
    "description": "The Scottish Fold is a sweet, charming breed. She is an easy cat to live with and to care for. She is affectionate and is comfortable with all members of her family. Her tail should be handled gently. Folds are known for sleeping on their backs, and for sitting with their legs stretched out and their paws on their belly. This is called the \"Buddha Position\".",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 4,
    "hypoallergenic": 0,
    "id": "sfol",
    "image": {
      "height": 1440,
      "id": "o9t0LDcsa",
      "url": "https://cdn2.thecatapi.com/images/o9t0LDcsa.jpg",
      "width": 1920
    },
    "indoor": 0,
    "intelligence": 3,
    "life_span": "11 - 14",
    "name": "Scottish Fold",
    "natural": 0,
    "origin": "United Kingdom",
    "rare": 0,
    "reference_image_id": "o9t0LDcsa",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Intelligent, Loyal, Playful, Social, Sweet, Loving",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/scottish-fold",
    "vetstreet_url": "http://www.vetstreet.com/cats/scottish-fold-highland-fold",
    "vocalisation": 1,
    "weight": {
      "imperial": "5 - 11",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Scottish_Fold"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Shepherd Cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/SelkirkRex.aspx",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Selkirk Rex is an incredibly patient, loving, and tolerant breed. The Selkirk also has a silly side and is sometimes described as clownish. She loves being a lap cat and will be happy to chat with you in a quiet voice if you talk to her. ",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 4,
    "hypoallergenic": 1,
    "id": "srex",
    "image": {
      "height": 902,
      "id": "II9dOZmrw",
      "url": "https://cdn2.thecatapi.com/images/II9dOZmrw.jpg",
      "width": 1920
    },
    "indoor": 0,
    "intelligence": 3,
    "lap": 1,
    "life_span": "14 - 15",
    "name": "Selkirk Rex",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "II9dOZmrw",
    "rex": 1,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Active, Affectionate, Dependent, Gentle, Patient, Playful, Quiet, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/selkirk-rex",
    "vetstreet_url": "http://www.vetstreet.com/cats/selkirk-rex",
    "vocalisation": 3,
    "weight": {
      "imperial": "6 - 16",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Selkirk_Rex"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Siam, Thai Cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/Siamese.aspx",
    "child_friendly": 4,
    "country_code": "TH",
    "country_codes": "TH",
    "description": "While Siamese cats are extremely fond of their people, they will follow you around and supervise your every move, being talkative and opinionated. They are a demanding and social cat, that do not like being left alone for long periods.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 1,
    "id": "siam",
    "image": {
      "height": 811,
      "id": "ai6Jps4sx",
      "url": "https://cdn2.thecatapi.com/images/ai6Jps4sx.jpg",
      "width": 1110
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Siamese",
    "natural": 0,
    "origin": "Thailand",
    "rare": 0,
    "reference_image_id": "ai6Jps4sx",
    "rex": 0,
    "shedding_level": 2,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Active, Agile, Clever, Sociable, Loving, Energetic",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/siamese",
    "vetstreet_url": "http://www.vetstreet.com/cats/siamese",
    "vocalisation": 5,
    "weight": {
      "imperial": "8 - 15",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Siamese_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Moscow Semi-longhair, HairSiberian Forest Cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/Siberian.aspx",
    "child_friendly": 4,
    "country_code": "RU",
    "country_codes": "RU",
    "description": "The Siberians dog like temperament and affection makes the ideal lap cat and will live quite happily indoors. Very agile and powerful, the Siberian cat can easily leap and reach high places, including the tops of refrigerators and even doors. ",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 1,
    "id": "sibe",
    "image": {
      "height": 2560,
      "id": "3bkZAjRh1",
      "url": "https://cdn2.thecatapi.com/images/3bkZAjRh1.jpg",
      "width": 4232
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Siberian",
    "natural": 1,
    "origin": "Russia",
    "rare": 0,
    "reference_image_id": "3bkZAjRh1",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 3,
    "suppressed_tail": 0,
    "temperament": "Curious, Intelligent, Loyal, Sweet, Agile, Playful, Affectionate",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/siberian",
    "vetstreet_url": "http://www.vetstreet.com/cats/siberian",
    "vocalisation": 1,
    "weight": {
      "imperial": "8 - 16",
      "metric": "4 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Siberian_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Drain Cat, Kucinta, Pura",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/Singapura.aspx",
    "child_friendly": 4,
    "country_code": "SP",
    "country_codes": "SP",
    "description": "The Singapura is usually cautious when it comes to meeting new people, but loves attention from his family so much that she sometimes has the reputation of being a pest. This is a highly active, curious and affectionate cat. She may be small, but she knows she’s in charge",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "sing",
    "image": {
      "height": 1350,
      "id": "Qtncp2nRe",
      "url": "https://cdn2.thecatapi.com/images/Qtncp2nRe.jpg",
      "width": 1080
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Singapura",
    "natural": 0,
    "origin": "Singapore",
    "rare": 0,
    "reference_image_id": "Qtncp2nRe",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Curious, Easy Going, Intelligent, Interactive, Lively, Loyal",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/singapura",
    "vetstreet_url": "http://www.vetstreet.com/cats/singapura",
    "vocalisation": 1,
    "weight": {
      "imperial": "5 - 8",
      "metric": "2 - 4"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Singapura_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Snowshoe is a vibrant, energetic, affectionate and intelligent cat. They love being around people which makes them ideal for families, and becomes unhappy when left alone for long periods of time. Usually attaching themselves to one person, they do whatever they can to get your attention.",
    "dog_friendly": 5,
    "energy_level": 4,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "snow",
    "image": {
      "height": 750,
      "id": "MK-sYESvO",
      "url": "https://cdn2.thecatapi.com/images/MK-sYESvO.jpg",
      "width": 1170
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "14 - 19",
    "name": "Snowshoe",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "MK-sYESvO",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Social, Intelligent, Sweet-tempered",
    "vocalisation": 5,
    "weight": {
      "imperial": "7 - 12",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Snowshoe_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Fox Cat, Long-Haired Abyssinian",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/Somali.aspx",
    "child_friendly": 3,
    "country_code": "SO",
    "country_codes": "SO",
    "description": "The Somali lives life to the fullest. He climbs higher, jumps farther, plays harder. Nothing escapes the notice of this highly intelligent and inquisitive cat. Somalis love the company of humans and other animals.",
    "dog_friendly": 4,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "soma",
    "image": {
      "height": 1008,
      "id": "EPF2ejNS0",
      "url": "https://cdn2.thecatapi.com/images/EPF2ejNS0.jpg",
      "width": 850
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "12 - 16",
    "name": "Somali",
    "natural": 0,
    "origin": "Somalia",
    "rare": 0,
    "reference_image_id": "EPF2ejNS0",
    "rex": 0,
    "shedding_level": 4,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Mischievous, Tenacious, Intelligent, Affectionate, Gentle, Interactive, Loyal",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/somali",
    "vetstreet_url": "http://www.vetstreet.com/cats/somali",
    "vocalisation": 1,
    "weight": {
      "imperial": "6 - 12",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Somali_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Canadian Hairless, Canadian Sphynx",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/Sphynx.aspx",
    "child_friendly": 4,
    "country_code": "CA",
    "country_codes": "CA",
    "description": "The Sphynx is an intelligent, inquisitive, extremely friendly people-oriented breed. Sphynx commonly greet their owners  at the front door, with obvious excitement and happiness. She has an unexpected sense of humor that is often at odds with her dour expression.",
    "dog_friendly": 5,
    "energy_level": 3,
    "experimental": 0,
    "grooming": 2,
    "hairless": 1,
    "health_issues": 4,
    "hypoallergenic": 1,
    "id": "sphy",
    "image": {
      "height": 1067,
      "id": "BDb8ZXb1v",
      "url": "https://cdn2.thecatapi.com/images/BDb8ZXb1v.jpg",
      "width": 1600
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 14",
    "name": "Sphynx",
    "natural": 0,
    "origin": "Canada",
    "rare": 1,
    "reference_image_id": "BDb8ZXb1v",
    "rex": 0,
    "shedding_level": 1,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Loyal, Inquisitive, Friendly, Quiet, Gentle",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/sphynx",
    "vetstreet_url": "http://www.vetstreet.com/cats/sphynx",
    "vocalisation": 5,
    "weight": {
      "imperial": "6 - 12",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Sphynx_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Tonk",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/Tonkinese.aspx",
    "child_friendly": 4,
    "country_code": "CA",
    "country_codes": "CA",
    "description": "Intelligent and generous with their affection, a Tonkinese will supervise all activities with curiosity. Loving, social, active, playful, yet content to be a lap cat",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "tonk",
    "image": {
      "height": 1080,
      "id": "KBroiVNCM",
      "url": "https://cdn2.thecatapi.com/images/KBroiVNCM.jpg",
      "width": 1080
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "14 - 16",
    "name": "Tonkinese",
    "natural": 0,
    "origin": "Canada",
    "rare": 0,
    "reference_image_id": "KBroiVNCM",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Curious, Intelligent, Social, Lively, Outgoing, Playful, Affectionate",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/tonkinese",
    "vetstreet_url": "http://www.vetstreet.com/cats/tonkinese",
    "vocalisation": 5,
    "weight": {
      "imperial": "6 - 12",
      "metric": "3 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Tonkinese_(cat)"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "The Toyger has a sweet, calm personality and is generally friendly. He's outgoing enough to walk on a leash, energetic enough to play fetch and other interactive games, and confident enough to get along with other cats and friendly dogs.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 1,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "toyg",
    "image": {
      "height": 1080,
      "id": "O3F3_S1XN",
      "url": "https://cdn2.thecatapi.com/images/O3F3_S1XN.jpg",
      "width": 1080
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "12 - 15",
    "name": "Toyger",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "O3F3_S1XN",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 3,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Playful, Social, Intelligent",
    "vetstreet_url": "http://www.vetstreet.com/cats/toyger",
    "vocalisation": 5,
    "weight": {
      "imperial": "7 - 15",
      "metric": "3 - 7"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Toyger"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Ankara",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/TurkishAngora.aspx",
    "child_friendly": 4,
    "country_code": "TR",
    "country_codes": "TR",
    "description": "This is a smart and intelligent cat which bonds well with humans. With its affectionate and playful personality the Angora is a top choice for families. The Angora gets along great with other pets in the home, but it will make clear who is in charge, and who the house belongs to",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 2,
    "hypoallergenic": 0,
    "id": "tang",
    "image": {
      "height": 1104,
      "id": "7CGV6WVXq",
      "url": "https://cdn2.thecatapi.com/images/7CGV6WVXq.jpg",
      "width": 736
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "15 - 18",
    "name": "Turkish Angora",
    "natural": 1,
    "origin": "Turkey",
    "rare": 0,
    "reference_image_id": "7CGV6WVXq",
    "rex": 0,
    "shedding_level": 2,
    "short_legs": 0,
    "social_needs": 5,
    "stranger_friendly": 5,
    "suppressed_tail": 0,
    "temperament": "Affectionate, Agile, Clever, Gentle, Intelligent, Playful, Social",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/turkish-angora",
    "vetstreet_url": "http://www.vetstreet.com/cats/turkish-angora",
    "vocalisation": 3,
    "weight": {
      "imperial": "5 - 10",
      "metric": "2 - 5"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Turkish_Angora"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "Turkish Cat, Swimming cat",
    "cfa_url": "http://cfa.org/Breeds/BreedsSthruT/TurkishVan.aspx",
    "child_friendly": 4,
    "country_code": "TR",
    "country_codes": "TR",
    "description": "While the Turkish Van loves to jump and climb, play with toys, retrieve and play chase, she is is big and ungainly; this is one cat who doesn’t always land on his feet. While not much of a lap cat, the Van will be happy to cuddle next to you and sleep in your bed. ",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 2,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "tvan",
    "image": {
      "height": 1280,
      "id": "sxIXJax6h",
      "url": "https://cdn2.thecatapi.com/images/sxIXJax6h.jpg",
      "width": 960
    },
    "indoor": 0,
    "intelligence": 5,
    "life_span": "12 - 17",
    "name": "Turkish Van",
    "natural": 1,
    "origin": "Turkey",
    "rare": 0,
    "reference_image_id": "sxIXJax6h",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Agile, Intelligent, Loyal, Playful, Energetic",
    "vcahospitals_url": "https://vcahospitals.com/know-your-pet/cat-breeds/turkish-van",
    "vetstreet_url": "http://www.vetstreet.com/cats/turkish-van",
    "vocalisation": 5,
    "weight": {
      "imperial": "7 - 20",
      "metric": "3 - 9"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/Turkish_Van"
  },
  {
    "adaptability": 5,
    "affection_level": 5,
    "alt_names": "York",
    "child_friendly": 4,
    "country_code": "US",
    "country_codes": "US",
    "description": "York Chocolate cats are known to be true lap cats with a sweet temperament. They love to be cuddled and petted. Their curious nature makes them follow you all the time and participate in almost everything you do, even if it's related to water: unlike many other cats, York Chocolates love it.",
    "dog_friendly": 5,
    "energy_level": 5,
    "experimental": 0,
    "grooming": 3,
    "hairless": 0,
    "health_issues": 1,
    "hypoallergenic": 0,
    "id": "ycho",
    "image": {
      "height": 1203,
      "id": "0SxW2SQ_S",
      "url": "https://cdn2.thecatapi.com/images/0SxW2SQ_S.jpg",
      "width": 800
    },
    "indoor": 0,
    "intelligence": 5,
    "lap": 1,
    "life_span": "13 - 15",
    "name": "York Chocolate",
    "natural": 0,
    "origin": "United States",
    "rare": 0,
    "reference_image_id": "0SxW2SQ_S",
    "rex": 0,
    "shedding_level": 3,
    "short_legs": 0,
    "social_needs": 4,
    "stranger_friendly": 4,
    "suppressed_tail": 0,
    "temperament": "Playful, Social, Intelligent, Curious, Friendly",
    "vocalisation": 5,
    "weight": {
      "imperial": "12 - 18",
      "metric": "5 - 8"
    },
    "wikipedia_url": "https://en.wikipedia.org/wiki/York_Chocolate"
  }
]

# breed1 = breeds[0]

# print(breed1['temperament'])

# for item in breeds:
#     try:
#         print(item['temperament'])
#     except:
#         print('item has no temperament')

def seed_breeds():
    for item in breeds:
        breed = Breed(
            name=item['name'],
            description=item['temperament'],
            image_url=item['image']['url']
        )
        db.session.add(breed)
    db.session.commit()

def undo_breeds():
    db.session.execute('TRUNCATE breeds RESTART IDENTITY CASCADE;')
    db.session.commit()
