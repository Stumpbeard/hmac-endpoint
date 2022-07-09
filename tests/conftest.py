"""Pytest fixtures for flask app. This is largely just taken from their docs.
https://flask.palletsprojects.com/en/2.1.x/testing/"""

import pytest
from app import app as current_app


@pytest.fixture()
def app():
    """App fixture with an explicit SECRET_KEY set for consistent results."""
    current_app.config["SECRET_KEY"] = "test"

    yield current_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
