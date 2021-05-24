from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user, login_user
from app.models import db, User, Favorite_Animal, Animal
from app.forms import UpdateForm
from app.awsupload import (
    upload_file_to_s3, allowed_file, get_unique_filename)

user_routes = Blueprint('users', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{error}")
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
    userId = current_user.id
    currentUser = User.query.get(userId)

    if "image" not in request.files:
       url = currentUser.image_url
    else:

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


    form = UpdateForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        newFirstname = request.form['first_name'];
        newLastname = request.form['last_name'];
        newZipcode = request.form['zipcode'];
        newPassword = request.form['password'];
        newImage = url



        if newFirstname:
            currentUser.first_name = newFirstname
        if newLastname:
            currentUser.last_name = newLastname
        if newZipcode:
            currentUser.zipcode = newZipcode
        if newPassword:
            currentUser.password = newPassword
        if newImage:
            currentUser.image_url = newImage

        db.session.commit()
        return currentUser.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}


@user_routes.route('', methods=['DELETE'])
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
