from fastapi.testclient import TestClient

from briefbot.api import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_brief_runs_graph():
    r = client.post("/briefs", json={"topic": "vector databases"})
    assert r.status_code == 201
    body = r.json()
    assert body["topic"] == "vector databases"
    assert "vector databases" in body["draft"]


def test_create_brief_validates_topic():
    assert client.post("/briefs", json={"topic": "x"}).status_code == 422
