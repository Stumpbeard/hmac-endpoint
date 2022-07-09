"""Flask app for generating HMAC signatures on posted messages.

HMAC is a kind of simple signing solution, for example of two parties share a key with each other
and want to ensure message integrity.
https://en.wikipedia.org/wiki/HMAC

For the purpose of the technical assessment, this is left lightweight, and heavy on
inline comments for the sake of clarity.

There are choices made (such as putting all functionality in one file) that exist due to the
small size of the assessment. In a real, assumedly much larger backend I would break things
such as endpoints and flask-agnostic utility functions into their own files, and generate
the app with a factory pattern."""

import hashlib
import hmac
import json
import os

from flask import Flask, request

# In a more robust app I'd put initialization in a factory and verify that
# we have a secret key env var
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


@app.route("/generate-token", methods=["POST"])
def generate_token():
    """Main POST endpoint for generating an HMAC token for any message sent to it."""
    # Using get_json() automatically returns a 400 if we do not get a json type post request
    body = request.get_json()

    message = json.dumps(body)
    signature = generate_signature(message, app.config.get("SECRET_KEY"))

    return body | {"signature": signature}


def generate_signature(message: str, key: str) -> str:
    """Wrapper for the python hmac built in, which can be a bit tricky.

    Extracted from the endpoint itself for easier testing separated from flask-app setup."""
    return hmac.new(
        bytes(key, "UTF-8"),
        bytes(message, "UTF-8"),
        hashlib.sha256,
    ).hexdigest()
