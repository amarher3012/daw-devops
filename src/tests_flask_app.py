# import pytest
"""
docstring
"""
from app import app  # Flask instance of the API


def test_index_route():
    """docstring"""
    response = app.test_client().get("/status")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "OK"


def test_landing():
    """docstring"""
    landing = app.test_client().get("/")
    html = landing.data.decode()

    assert landing.status_code == 200

    # Check text
    assert "Hello Docker" in html
    assert "It is currently " in html
