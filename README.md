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

When a user first comes to the website they will immediately see the home page.  This will have a list of animal tiles on it displaying the animals picture and their name and also has the website banner. You will see a navigation bar at the top with a home button, search bar, and login and signup buttons. If you are loggin in you will see the heart icons on the animal tiles and see your paw print on the nav bar to access your favorite animals page.

![HomePage](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/Pet-Homepage.PNG)


## Animal Page

After clicking on one of the animal tiles you will be brought to that animals page.  On the animal page you will see all the information about that animal, including the animals pictures, animal information, and breed information.  The shelter the animal is located at is also displayed here using Google Map API.  Towards the bottom of the page you will see the adoption form to inquire about the animal.  This form will only appear after you have logged in as a user.

![AnimalPage](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/animalpage1.PNG)
![AnimalPage2](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/animal-info.PNG)
![AnimalPage3](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/adoption%20form.PNG)


## Favorite Page

Once you are logged in you while see a heart icon appear on all animal tiles.  You are able to click these hearts to add animals to your favorites page. They will be saved to your user so whenever you log back in to the site, it will remember all of your favorited animals.

![FavoritePage](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/favorite-Page.PNG)


## Shelter Page

You can get to the shelter page from any animal page by clicking on the marker in the Google Map API.  One you are on the shelter page you will still see all of the shelter's information but you will no get a list of animals that are located at that shelter.

![ShelterPage](https://github.com/Natejo91/Adopt-a-Pet/blob/main/assets/shelter-page.PNG)
