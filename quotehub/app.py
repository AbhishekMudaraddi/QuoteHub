from flask import Flask, jsonify, request

app = Flask(__name__)

quotes = [
    {"id": 1, "text": "Stay hungry, stay foolish."},
    {"id": 2, "text": "Simplicity is the ultimate sophistication."}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to QuoteHub API"})

@app.route("/quotes", methods=["GET"])
def get_quotes():
    return jsonify(quotes)

@app.route("/quotes", methods=["POST"])
def add_quote():
    data = request.get_json()
    new_quote = {
        "id": len(quotes) + 1,
        "text": data.get("text", "")
    }
    quotes.append(new_quote)
    return jsonify(new_quote), 201

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
