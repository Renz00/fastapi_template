from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app # use the app instance inside main.py
from backend.routes.user import router # use the router instance to get url paths dynamically

client = TestClient(app)


def test_store_user():
    response = client.post(router.url_path_for('store_user'),
    json={'username': 'tony'})
    assert response.status_code == 201
    assert response.json() == {"success": True}