from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_ingest():

    response = client.post(
        "/ingest",
        json={
            "title": "Test",
            "content": "Notice period is 30 days."
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"