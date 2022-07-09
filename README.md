# hmac-endpoint
Technical assessment implementing an endpoint for signing payloads with an HMAC token

## Pre-requisites
* Python 3.9 or greater
* [pipenv](https://pipenv.pypa.io/en/latest/)
* An environment variable called `SECRET_KEY`. This is used as your HMAC key.

## Installation
1. Clone repo, navigate into it
2. Install the dependencies and create a virtual environment for the repo by running `pipenv install --dev` in your terminal.

## Running and testing the app
Enter your new virtual environment with `pipenv shell`.

From there you can run the app with the script `./run.sh` in your terminal. If you'd like to set the HMAC key at runtime, type something like `SECRET_KEY=test ./run.sh`

To test, make sure you're in your virtual environment and type `pytest`. The server does not need to be running for this.

You can also test manually with `curl` when the server is up, with commands such as:
```
curl --request POST \
--url http://localhost:8081/generate-token \
--header 'Content-Type: application/json' \
--data '{
"id":
"MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz"
}'
```
