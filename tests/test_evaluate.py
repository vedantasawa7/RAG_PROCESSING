from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_evaluate():

    response = client.post(
        "/evaluate",
        json={
            "test_cases": [
                {
                    "question":"What is the notice period?",
                    "expected_answer":"30 days"
                }
            ]
        }
    )

    assert response.status_code == 200