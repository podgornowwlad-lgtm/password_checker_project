from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_password(password: str) -> bool:
    return isinstance(password, str) and len(password) >= 8 and any(ch.isdigit() for ch in password)

@app.route('/', methods=['GET'])
def hello():
    return 'Password Checker'

@app.route('/check', methods=['POST'])
def check_password():
    data = request.json
    if not isinstance(data, dict) or 'password' not in data:
        return jsonify({'status': 'bad input'}), 400

    password = data['password']
    if validate_password(password):
        return jsonify({'status': 'strong'})
    return jsonify({'status': 'weak'})

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
