import json
from src import create_app

app = create_app()
client = app.test_client()

def test_valid_event():
    response = client.post("/report_event", json={
        "ecu_id": "ECU_1",
        "event_type": "tamper_detected"
    })
    assert response.status_code == 200

def test_invalid_event():
    response = client.post("/report_event", json={"invalid": "data"})
    assert response.status_code == 400
