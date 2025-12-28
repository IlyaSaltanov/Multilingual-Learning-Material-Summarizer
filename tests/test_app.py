"""
Тесты Flask приложения
"""

import json
import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Добавляем src в путь импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app


class TestFlaskApp:
    """Тесты Flask приложения"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.client = app.test_client()
        self.client.testing = True

    def test_home_route(self):
        """Тест главной страницы"""
        response = self.client.get('/')
        assert response.status_code == 200
        assert 'text/html' in response.content_type

    def test_health_endpoint(self):
        """Тест health check endpoint"""
        response = self.client.get('/health')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert data['service'] == 'Multilingual Summarizer'

    def test_summarize_no_data(self):
        """Тест суммаризации без данных"""
        response = self.client.post('/summarize', json={})
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'No text provided' in data['error']

    def test_summarize_short_text(self):
        """Тест суммаризации слишком короткого текста"""
        response = self.client.post('/summarize', json={
            'text': 'This is too short'
        })
        assert response.status_code == 400
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'Text too short' in data['error']

    @patch('app.summarize_text_extractive')
    @patch('app.detect_language_simple')
    def test_summarize_success_auto_language(self, mock_detect, mock_summarize):
        """Тест успешной суммаризации с автоопределением языка"""
        # Мокаем зависимости
        mock_detect.return_value = {'language': 'en', 'confidence': 0.9}
        mock_summarize.return_value = 'Summary of the text.'
        
        text = "This is a test text for summarization. " * 10
        
        response = self.client.post('/summarize', json={
            'text': text,
            'language': 'auto',
            'compression': 30
        })
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['summary'] == 'Summary of the text.'
        assert data['language'] == 'en'
        assert data['language_name'] == 'English'
        assert 'original_length' in data
        assert 'summary_length' in data
        assert 'reduction' in data
        
        mock_detect.assert_called_once()
        mock_summarize.assert_called_once()

    @patch('app.summarize_text_extractive')
    def test_summarize_success_manual_language(self, mock_summarize):
        """Тест успешной суммаризации с указанием языка"""
        mock_summarize.return_value = 'Summary of the text.'
        
        text = "Это тестовый текст для суммаризации. " * 10
        
        response = self.client.post('/summarize', json={
            'text': text,
            'language': 'ru',
            'compression': 30
        })
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['success'] is True
        assert data['language'] == 'ru'
        assert data['language_name'] == 'Russian'
        assert data['confidence'] == 1.0

    def test_summarize_invalid_compression(self):
        """Тест с некорректным процентом сжатия"""
        text = "This is a test text for summarization. " * 10
        
        response = self.client.post('/summarize', json={
            'text': text,
            'compression': 75  # Невалидное значение
        })
        
        assert response.status_code == 200
        
        data = json.loads(response.data)
        # Должен использоваться дефолтный compression (30)
        assert data['compression'] == 30

    @patch('app.summarize_text_extractive')
    def test_summarize_server_error(self, mock_summarize):
        """Тест обработки ошибки сервера"""
        mock_summarize.side_effect = Exception('Test error')
        
        text = "This is a test text for summarization. " * 10
        
        response = self.client.post('/summarize', json={
            'text': text
        })
        
        assert response.status_code == 500
        
        data = json.loads(response.data)
        assert 'error' in data
        assert 'Test error' in data['error']

    def test_summarize_with_special_characters(self):
        """Тест суммаризации с специальными символами"""
        text = "Text with special chars: café, naïve, résumé. " * 5
        
        response = self.client.post('/summarize', json={
            'text': text
        })
        
        # Проверяем что приложение не падает
        assert response.status_code in [200, 400]


if __name__ == '__main__':
    pytest.main()