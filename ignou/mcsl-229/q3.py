from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database of users (replace with your actual user database)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/validate_user', methods=['POST'])
def validate_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username] == password:
        return jsonify({'message': 'User validated successfully'})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

        
@app.route('/', methods=['GET'])
def mainapi():
    return jsonify({'message':"Server is running on 8080"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
