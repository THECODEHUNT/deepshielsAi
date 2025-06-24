from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/verify", methods=["POST"])
def verify_audio():
    file = request.files.get("audio")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Placeholder detection logic
    result = "real"  # or "fake"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)