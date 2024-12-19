import requests
from django.test import TestCase

BASE_URL = "http://localhost:8000"

class TripletEndpointTests(TestCase):
    def test_triplet_endpoint_valid(self):
        params = {"a": 3, "b": 4, "c": 5}
        response = requests.get(f"{BASE_URL}/api/triplet/", params=params)
        assert response.status_code == 200
        data = response.json()
        assert data["a"] == 3
        assert data["b"] == 4
        assert data["c"] == 5
        assert data["is_triplet"] is True
        assert "product" in data

    def test_triplet_endpoint_invalid(self):
        params = {"a": 5, "b": 5, "c": 5}
        response = requests.get(f"{BASE_URL}/api/triplet/", params=params)
        assert response.status_code == 200
        data = response.json()
        assert data["a"] == 5
        assert data["b"] == 5
        assert data["c"] == 5
        assert data["is_triplet"] is False
        assert data["message"] == "The numbers do not form a Pythagorean triplet."
