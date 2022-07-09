from app import generate_signature


def test_generate_signature():
    """This is testing that implementation of the HMAC library is correct. Static key+message
    asserted against output from outside source:

    https://www.freeformatter.com/hmac-generator.html"""
    signature = generate_signature("test message", "test key")
    assert (
        signature == "038334a2f762587699e66b1d0c56ebbed0a1170648a086914951a6bfc6e63ed7"
    )


def test_generate_token_endpoint(client):
    """Just testing that endpoint works at all with expected input."""
    response = client.post("/generate-token", json={})
    assert response.status_code == 200


def test_generate_token_endpoint_failure(client):
    """Testing failure if we don't send a json body."""
    response = client.post("/generate-token", data={})
    assert response.status_code == 400


def test_generate_token_output(client):
    """Test with example input, using signatures generated with 'test' as key."""
    request_body = {"id": "MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz"}
    response = client.post(
        "/generate-token",
        json=request_body,
    )
    assert response.json == request_body | {
        "signature": "9723b88960b31ca97149b855a7402e3751e31cf68c049b1b701283af7b90a86f"
    }

    request_body = {
        "message": "Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey."
    }
    response = client.post(
        "/generate-token",
        json=request_body,
    )
    assert response.json == request_body | {
        "signature": "f9083c727f0d01539e58248e1f7d86a01c858c1ea14dab68e1f7b0eea4368530"
    }
