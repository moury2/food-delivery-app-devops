from flask import Flask, jsonify

# Create a Flask web app
app = Flask(__name__)

# Create a simple route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Food Delivery App!"})

@app.route("/menu")
def menu():
    return jsonify({"items": ["Pizza", "Burger", "Idli", "Dosa"]})

# Run the app when the script is executed
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
