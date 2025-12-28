"""
Тесты модуля определения языка
"""

from language_detector import LanguageDetector
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


class TestLanguageDetector:
    """Тесты для класса LanguageDetector"""

    def setup_method(self):
        self.detector = LanguageDetector()

    def test_initialization(self):
        """Тест инициализации"""
        assert hasattr(self.detector, 'supported_languages')

    def test_detect_language_simple(self):
        """Простой тест определения языка"""
        result = self.detector.detect_language("Hello world")
        assert isinstance(result, dict)
        assert 'language' in result

    def test_get_language_name(self):
        """Тест получения названия языка"""
        assert self.detector.get_language_name('en') == 'English'
