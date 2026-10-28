import os
from flask import Flask, jsonify

app = Flask(__name__)

REGNO = os.getenv("REGNO", "202401100200132")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")


@app.route("/")
def home():
    return jsonify({
        "application": "FestPass Backend",
        "registration_number": REGNO,
        "version": APP_VERSION
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "registration_number": REGNO,
        "database": False,
        "version": APP_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)