from flask import request, jsonify, abort
from app import db, auth
from app.models.message import Message
from app.models.user import User
from app.routes import main


@main.route('/test', methods=['GET'])
def test_route():
    return "Test route is working!"


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None


@main.route('/register', methods=['POST'])
def register_user():
    if not request.json or not 'username' in request.json or not 'password' in request.json or not 'email' in request.json:
        abort(400)
    
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if User.query.filter_by(username=username).first() is not None:
        abort(400, description="User already exists")

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'username': new_user.username, 'email': new_user.email}), 201


@main.route('/messages', methods=['GET'])
@auth.login_required
def get_messages():
    user = auth.current_user()
    messages = Message.query.filter_by(user_id=user.id).all()
    return jsonify([dict(message.to_dto()) for message in messages])

@main.route('/messages/<string:message_id>', methods=['GET'])
@auth.login_required
def get_message(message_id):
    user = auth.current_user()

    message = Message.query.filter_by(id=message_id, user_id=user.id).first()
    if not message:
        abort(404)
    message.increment_count()
    return jsonify(dict(message.to_dto()))

@main.route('/messages', methods=['POST'])
@auth.login_required
def create_message():
    if not request.json or 'content' not in request.json:
        abort(400)
    content = request.json['content']
    if len(content) > 255:
        abort(400, description="Message content exceeds 255 characters")


    user = auth.current_user()

    new_message = Message(content=content, user_id=user.id)
    db.session.add(new_message)
    db.session.commit()
    return jsonify(dict(new_message.to_dto())), 201

@main.route('/messages/<string:message_id>', methods=['PUT'])
@auth.login_required
def update_message(message_id):
    user = auth.current_user()

    message = Message.query.filter_by(id=message_id, user_id=user.id).first()

    if not message:
        abort(404)
    if not request.json or 'content' not in request.json:
        abort(400)
    content = request.json['content']
    if len(content) > 255:
        abort(400, description="Message content exceeds 255 characters")
    message.content = content
    db.session.commit()
    return jsonify(dict(message.to_dto()))

@main.route('/messages/<string:message_id>', methods=['DELETE'])
@auth.login_required
def delete_message(message_id):
    user = auth.current_user()

    message = Message.query.filter_by(id=message_id, user_id=user.id).first()
    if not message:
        abort(404)
    db.session.delete(message)
    db.session.commit()
    return jsonify({'result': 'success'})