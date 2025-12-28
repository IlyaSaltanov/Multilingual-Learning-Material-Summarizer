"""
Тесты Flask приложения
"""

import json
from unittest.mock import patch
from app import app  # Импорт из src/app.py


class TestFlaskApp:
    """Тесты Flask приложения"""

    def setup_method(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_route(self):
        """Тест главной страницы"""
        response = self.client.get("/")
        assert response.status_code == 200

    def test_health_endpoint(self):
        """Тест health check"""
        response = self.client.get("/health")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["status"] == "healthy"

    def test_summarize_no_data(self):
        """Тест без данных"""
        response = self.client.post("/summarize", json={})
        assert response.status_code == 400

    @patch("app.summarize_text_extractive")
    @patch("app.detect_language_simple")
    def test_summarize_success(self, mock_detect, mock_summarize):
        """Тест успешной суммаризации"""
        mock_detect.return_value = {"language": "en", "confidence": 0.9}
        mock_summarize.return_value = "Summary."

        response = self.client.post("/summarize", json={"text": "Test text " * 10})

        assert response.status_code == 200
