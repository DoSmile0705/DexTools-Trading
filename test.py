from flask import Flask, jsonify, request
import jwt
import datetime


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():

    email = request.json.get('email')
    password = request.json.get('password')

    # Perform authentication logic here
    # Verify the email and password against your user database

    # If authentication is successful, create a JWT token
    if email == 'example@example.com' and password == 'password':
        # Set the expiration time for the token (e.g., 1 day from now)
        print("here")
        expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        print("this isthe sendocde")
        # Create the payload for the token
        payload = {
            'email': email,
            'exp': expiration
        }
        print("sdaffffffffffffffffffffffff")
        # Generate the JWT token
        token = jwt.encode(payload, 'your-secret-key', algorithm='HS256')
        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        # Return the token as a response
        return jsonify({'token': token, 'exp' : payload})

    # If authentication fails, return an error message
    return jsonify({'error': 'Invalid email or password'}), 401
