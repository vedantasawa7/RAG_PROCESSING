from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_query():

    response = client.post(
        "/query",
        json={
            "question":
            "What is the notice period?"
        }
    )

    assert response.status_code == 200