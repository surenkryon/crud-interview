from datetime import datetime
from flask import jsonify, request
from sqlalchemy import asc, desc
from user import app
from user.db.model import User, db
from user.db.schema import UserSchema
from user.validation.register_validation import validate_request


# api for register a new user
@app.route("/api/v1/user/register", methods=['POST'])
def create_user():
    data = request.json

    # check the is fields are valid
    validation_result = validate_request(request.json)

    #  if no errors in fields it save the user
    if len(validation_result) == 0:
        user = User()

        user.first_name = data['first_name']

        user.last_name = data['last_name']

        user.mail_id = data['mail_id']

        user.age = data['age']

        user.created_date_time = datetime.now()

        db.session.add(user)

        db.session.commit()

        return jsonify({
            "message": "successfully_registered"
        }), 201

    else:
        return jsonify({
            "message": validation_result
        }), 400


# api for get users list
@app.route('/api/v1/user/list', methods=['GET'])
def get_all_users():
    # query all users in the db
    users = User.query.all()

    user_schema = UserSchema(many=True)

    # serialize the user object
    output = user_schema.dump(users)

    count = len(output)

    result = {'total Count': count, 'users': output}

    return jsonify(result), 200


# api for update user details
@app.route("/api/v1/user/update", methods=['PUT'])
def user_update():
    data = request.json
    id = data.get('id', None)
    # check mandatory field for update
    if id is None:
        return jsonify({
            "message": "id required for update"
        }), 400

    validation_result = validate_request(request.json)

    if len(validation_result) == 0:

        user = User.query.filter_by(id=data['id']).first()

        if user is None:
            return jsonify({
                "message": "user not found"
            }), 400

        else:
            user.first_name = data.get('first_name', user.first_name)

            user.mail_id = data.get('mail_id', user.mail_id)

            user.last_name = data.get('last_name', user.last_name)

            user.age = data.get('age', user.age)

            db.session.add(user)

            db.session.commit()
            return jsonify({
                "message": "user_updated sucessfully!..."
            }), 200
    else:
        return jsonify({
            "message": validation_result
        }), 200


# api for get user details
@app.route('/api/v1/user/detail', methods=['GET'])
def user_detail():
    # id field
    user_id = request.args.get('user_id')

    # check mandatory field for user details
    if user_id is None:
        return jsonify({
            "message": "user id is required for detail"
        }), 400

    # search user in table
    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return jsonify({
            "message": "user not found"
        }), 400

    else:
        issue_schema = UserSchema()

        output = issue_schema.dump(user)

        return jsonify(output), 200


# api for delete user
@app.route("/api/v1/user/delete", methods=['DELETE'])
def user_delete():
    user_id = request.args.get('user_id')

    if user_id is None:
        return jsonify({
            "message": "user id required for delete user"
        }), 400

    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return jsonify({
            "message": "user not found"
        }), 400
    else:
        db.session.delete(user)

        db.session.commit()

        return jsonify({
            "message": "user delete sucessfully!..."
        }), 200
