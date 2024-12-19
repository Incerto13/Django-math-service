import requests
from django.test import TestCase

BASE_URL = "http://localhost:8000"

class IntegrationTests(TestCase):
    def test_difference_endpoint(self):
        number = 6
        response = requests.get(f"{BASE_URL}/api/difference/", params={"number": number})
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
