import os
import base64
import headless

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/text/get")
def text_get():
    text = headless.execute()
    return text

@app.route("/health")
def health():
    return "OK", 200

port = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
    if port != 0:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True)