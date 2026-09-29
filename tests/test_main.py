from fastapi.testclient import TestClient
from main import app, process_query
import pytest

client = TestClient(app)

def test_demo():
    from main import demo
    demo()  # Should not raise

def test_query_success():
    resp = client.post("/query", json={"text": "hello"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["result"] == "HELLO"
    assert "hash" in data

def test_query_empty():
    resp = client.post("/query", json={"text": "   "})
    assert resp.status_code == 400

def test_query_missing_text():
    resp = client.post("/query", json={})
    assert resp.status_code == 422
