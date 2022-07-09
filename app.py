import hashlib
import hmac
import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/generate-token", methods=["POST"])
def generate_token():
    body = request.get_json()
    message = json.dumps(body)
    signature = hmac.new(
        bytes("test", "UTF-8"), bytes(message, "UTF-8"), hashlib.sha256
    ).hexdigest()

    return body | {"signature": signature}
