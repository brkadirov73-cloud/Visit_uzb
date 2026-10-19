from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Visit Uzbekistan API ishlayapti")

@app.route("/places")
def places():
    return jsonify([
        {"id": 1, "name": "Registon", "city": "Samarqand"},
        {"id": 2, "name": "Ichan Qala", "city": "Xiva"},
        {"id": 3, "name": "Poykand", "city": "Buxoro"},
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
