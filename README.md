![Banner](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/Capstone-Banner.png)

# Welcome to Adopt-a-Pet!
*[Adopt-a-Pet](https://adopt-a-pet-app.herokuapp.com)* is a clone of the popular PetFinder website which connects users to animals from animal shelters all over the United States.




**Technologies: React, Redux, Flask, Flask-SQLAlchemy, CSS3, JavaScript**

**API's: Google Map API, PetFinder API, Dog API, Cat API**



After a span of 2 weeks, the goal was to have 3 fully functional MVP's:

- Animal Page  - This page details everthing about a specific animal as well as the information on the animal's shelter. A form to inquire about the animal will appear if you are                  logged in.
- Basic Search - Allow the user to search by animal type or by breed.
- Shelter Page - This page details a specific shelter displaying all the animals located at that shelter.


In addition to those 3 MVP's I was able to implement these bonus features:

- Favorite Page - A logged in user is able to favorite any animal they choose. Those animals are then displayed on the user's favorite animals page.
- Shelter Map   - Was able to implement Google Map API for the exact location of the animal shelters.  Implemented an InfoWindow as well to allow the user to click on the map to                     take you to the shelter page.

For more details on the MVP's used, check out the MVP guide *[here](https://github.com/Natejo91/Adopt-a-Pet/wiki/MVP-Feature-List)*


## Home Page

When a user first comes to the website they will immediately see the home page.  This will have a list of animal tiles on it displaying the animals picture and their name and also has the website banner. You will see a navigation bar at the top with a home button, search bar, and login and signup buttons.

![HomePage](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/pet-homepage.PNG)


## Animal Page

After clicking on one of the animal tiles you will be brought to that animals page.  On the animal page you will see all the information about that animal, including the animals pictures, animal information, and breed information.  The shelter the animal is located at is also displayed here using Google Map API.  Towards the bottom of the page you will see the adoption form to inquire about the animal.  This form will only appear after you have logged in as a user.

![AnimalPage](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/animalpage1.PNG)
![AnimalPage2](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/animal-info.PNG)
![AnimalPage3](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/adoption%20form.PNG)


## Favorite Page
