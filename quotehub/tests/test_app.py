from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_quotes():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
