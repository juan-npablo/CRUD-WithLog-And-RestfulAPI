import os
from bson import json_util, ObjectId
from bson.errors import InvalidId

from flask import Flask, jsonify, request, Response
from dotenv import load_dotenv
from flask_pymongo import PyMongo


load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo()
mongo.init_app(app)


@app.route('/books', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_keys = user_data.keys()
    if {'title', 'author', 'genre', 'amount', 'price', 'release_date', 'editorial'} == set(user_keys):
        new_user = mongo.db.books.insert_one({
            'title': user_data.get('title', None),
            'author': user_data.get('author', None),
            'genre': user_data.get('genre', None),
            'amount': user_data.get('amount', None),
            'price': user_data.get('price', None),
            'release_date': user_data.get('release_date', None),
            'editorial': user_data.get('editorial', None),
        })
        response = {'_id': str(new_user.inserted_id)}
        response.update(user_data)
        return jsonify(response)
    else:
        return jsonify({'message': 'Missing some fields in payload or payload is invalid'}), 400


@app.route('/books', methods=['GET'])
def get_all_users():
    users = mongo.db.books.find()
    return Response(json_util.dumps(users), mimetype='application/json')


@app.route('/books/<identifier>', methods=['GET'])
def get_user(identifier):
    try:
        user_id = ObjectId(identifier)
    except InvalidId:
        return jsonify({'message': 'User not found'}), 404

    user = mongo.db.books.find_one({'_id': user_id})
    if user:
        return Response(json_util.dumps(user), mimetype='application/json')
    else:
        return jsonify({'message': 'User not found'}), 404


@app.route('/books/<identifier>', methods=['PUT'])
def update_user(identifier):
    try:
        user_id = ObjectId(identifier)
    except InvalidId:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'message': 'Invalid payload: payload is empty'}), 400

    response = mongo.db.books.update_one({'_id': user_id}, {'$set': data})

    if response.matched_count == 0:
        return jsonify({'message': 'User not found'}), 404
    elif response.modified_count > 0:
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'Nothing to update'})


@app.route('/books/<identifier>', methods=['DELETE'])
def delete_user(identifier):
    try:
        user_id = ObjectId(identifier)
    except InvalidId:
        return jsonify({'message': 'User not found'}), 404

    response = mongo.db.books.delete_one({'_id': user_id})

    if response.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
