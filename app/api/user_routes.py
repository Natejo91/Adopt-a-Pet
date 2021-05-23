from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user, login_user
from app.models import db, User, Favorite_Animal, Animal
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


@user_routes.route('', methods=['PATCH'])
def update_user():
    '''
    Updates user information
    '''
    if current_user.id == 1:
        return

    userId = current_user.id

    newFirstname = request.form['first_name'];
    newLastname = request.form['last_name'];
    newZipcode = request.form['zipcode'];
    newEmail = request.form['email'];
    newPassword = request.form['password'];

    currentUser = User.query.get(userId)

    if newFirstname:
        currentUser.first_name = newFirstname
    if newLastname:
        currentUser.last_name = newLastname
    if newZipcode:
        currentUser.zipcode = newZipcode
    if newEmail:
        currentUser.email = newEmail
    if newPassword:
        currentUser.password = newPassword


    db.session.commit()
    return currentUser.to_dict()


@user_routes.route('/<int:id>', methods=['DELETE'])
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
