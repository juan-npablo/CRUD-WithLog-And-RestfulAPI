from flask import Flask, jsonify, request

app = Flask(__name__)

records = []
user_id = 0


@app.route('/CRUD/users', methods=['POST'])
def create_user():
    global user_id
    new_user = {
        'id': user_id,
        'full_name': request.json['full_name'],
        'age': request.json['age'],
        'email': request.json['email']
    }
    records.append(new_user)
    user_id += 1
    return jsonify(new_user), 201


@app.route('/CRUD/users', methods=['GET'])
def get_users():
    return jsonify(records)


@app.route('/CRUD/users/<int:user_id>', methods=['GET'])
def get_user(identifier):
    try:
        user_found = next(filter(lambda user: user['id'] == identifier, records))
        return jsonify(user_found)
    except StopIteration:
        return jsonify({'message': 'User not found'}), 404


@app.route('/CRUD/users/<int:user_id>', methods=['PUT'])
def update_user(identifier):
    try:
        user_found = next(filter(lambda user: user['id'] == identifier, records))
        user_found['full_name'] = request.json['full_name']
        user_found['age'] = request.json['age']
        user_found['email'] = request.json['email']
        return jsonify(user_found)
    except StopIteration:
        return jsonify({'message': 'User not found'}), 404


@app.route('/CRUD/users/<int:user_id>', methods=['DELETE'])
def delete_user(identifier):
    try:
        user_found = next(filter(lambda user: user['id'] == identifier, records))
        records.remove(user_found)
    except StopIteration:
        return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
