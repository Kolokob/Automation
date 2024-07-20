from Steps.steps_api.user import Sender
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/create_sender', methods=['POST'])
def create_sender():
    data = request.json
    sender = Sender(data['email'], data['password'], data['country'])
    try:
        sender.create_sender()
        return jsonify({"message": "Sender created successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    sender = Sender(data['email'], data['password'], data['country'])
    try:
        session_key = sender.login()
        return jsonify({"session_key": session_key}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_token', methods=['POST'])
def get_token():
    data = request.json
    sender = Sender(data['email'], data['password'], data['country'])
    sender.session_key = data['session_key']
    try:
        sender.get_token()
        return jsonify({"token": sender.token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/logout', methods=['POST'])
def logout():
    data = request.json
    sender = Sender(data['email'], data['password'], data['country'])
    sender.session_key = data['session_key']
    try:
        sender.logout()
        return jsonify({"message": "Logged out successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/update_profile', methods=['PUT'])
def update_profile():
    data = request.json
    sender = Sender(data['email'], data['password'], data['country'])
    sender.session_key = data['session_key']
    try:
        sender.update_profile(
            name=data.get('name'),
            surname=data.get('surname'),
            cell=data.get('cell'),
            address_actual=data.get('address_actual')
        )
        return jsonify({"message": "Profile updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

