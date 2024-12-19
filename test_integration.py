import requests

BASE_URL = "http://localhost:8000"

def test_difference_endpoint():
    number = 6
    response = requests.get(f"{BASE_URL}/difference", params={"number": number})
    assert response.status_code == 200
    data = response.json()

    # Verify the keys and values
    assert "datetime" in data
    assert "value" in data
    assert "number" in data
    assert "occurrences" in data
    assert "last_datetime" in data
    assert data["number"] == number
    assert isinstance(data["value"], int)
    assert isinstance(data["occurrences"], int)

def test_triplet_endpoint_valid():
    params = {"a": 3, "b": 4, "c": 5}
    response = requests.get(f"{BASE_URL}/triplet", params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["a"] == 3
    assert data["b"] == 4
    assert data["c"] == 5
    assert data["is_triplet"] is True
    assert "product" in data

def test_triplet_endpoint_invalid():
    params = {"a": 5, "b": 5, "c": 5}
    response = requests.get(f"{BASE_URL}/triplet", params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["a"] == 5
    assert data["b"] == 5
    assert data["c"] == 5
    assert data["is_triplet"] is False
    assert data["message"] == "The numbers do not form a Pythagorean triplet."
