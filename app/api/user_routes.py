from flask import Blueprint, jsonify
from flask_login import login_required, current_user, login_user
from app.models import User, Favorite_Animal
from app.forms import SignUpForm

user_routes = Blueprint('users', __name__)


# @user_routes.route('/')
# @login_required
# def users():
#     users = User.query.all()
#     return {"users": [user.to_dict() for user in users]}

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@user_routes.route('/<int:id>')
@login_required
def user():
    '''
    A logged in user can get their information
    '''
    userId = current_user.id
    user = User.query.get(userId)
    return user.to_dict()


@user_routes.route('/<int:id>', methods=['PATCH'])
@login_required
def update_user():
    '''
    Updates user information
    '''
    if current_user.id == 1:
        return

    if "image" not in request.files:
        return {"errors": "image required"}, 400

    image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)

    if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message
        return upload, 400

    url = upload["url"]

    userId = current_user.id
    form = SignupForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            first_name = form.data['first_name'],
            last_name = form.data['last_name'],
            zipcode = form.data['zipcode'],
            email = form.data['email'],
            password = form.data['password'],
            image_url = url
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@user_routes.route('<int:id>', methods=['DELETE'])
@login_required
def delete_user():
    '''
    Delete your user
    '''
    if current_user.id == 1:
        return {'message': 'Cannot delete demo user'}, 401

    userId = current_user.id
    user = User.query.get(userId)
    db.session.delete(user)
    db.session.commit()
    return {'message': 'Your account has been deleted!'}



@user_routes.route('<int:id>/favorites')
def get_Favorites(id):
    '''
    Return a users favorite pets
    '''
    favorites = Favorite_Animal.query.filter_by(user_=id).all()
    fav_list = [favorite.to_dict() for favorite in favorites]

    return jsonify(fav_list)


@user_routes.route('<int:id>/favorites', methods=['POST'])
def post_favorite_animal(id, fav_id):
    new_favorite_animal = Favorite_Animal(
        user_id = id,
        animal_id = fav_id
    )

    db.session.add(new_favorite_animal)
    db.session.commit()
    return jsonify(new_favorite_animal.to_dict())


@user_routes.route('<int:id>/favorites/<int:fav_id>', methods=['DELETE'])
def delete_favorite_animal(id, fav_id):
    favorite_animal = Favorite_Animal.query.filter_by(user_id=id, animal_id=fav_id).first()
    db.session.delete(favorite_animal)
    db.session.commit()
    return jsonify(favorite_animal.to_dict())
