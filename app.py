from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your simple Python API!"})

@app.route('/health')
def health():
    return jsonify({"status": "UP"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)
