"""
Тесты модуля определения языка
"""

import sys
import os

# Добавляем src в путь импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from language_detector import LanguageDetector, detect_language_simple


class TestLanguageDetector:
    """Тесты для класса LanguageDetector"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.detector = LanguageDetector()

    def test_initialization(self):
        """Тест инициализации детектора"""
        assert hasattr(self.detector, 'supported_languages')
        assert isinstance(self.detector.supported_languages, list)
        assert 'en' in self.detector.supported_languages
        assert 'ru' in self.detector.supported_languages
        assert 'de' in self.detector.supported_languages

    def test_detect_language_short_text(self):
        """Тест определения языка для короткого текста"""
        result = self.detector.detect_language("Hi")
        
        assert result['language'] == 'en'
        assert result['confidence'] == 0.5
        assert result['method'] == 'fallback'

    def test_detect_language_english(self):
        """Тест определения английского языка"""
        text = "This is a sample text in English language for testing purposes."
        
        result = self.detector.detect_language(text)
        
        assert result['language'] == 'en'
        assert 'confidence' in result
        assert 'method' in result

    def test_detect_language_russian(self):
        """Тест определения русского языка"""
        text = "Это пример текста на русском языке для тестирования определения языка."
        
        result = self.detector.detect_language(text)
        
        assert result['language'] == 'ru'
        assert result['confidence'] > 0
        assert result['method'] in ['langdetect', 'character_analysis']

    def test_detect_language_german(self):
        """Тест определения немецкого языка"""
        text = "Dies ist ein Beispieltext in deutscher Sprache zum Testen der Spracherkennung mit Umlauten ä ö ü und ß."
        
        result = self.detector.detect_language(text)
        
        assert result['language'] == 'de'
        assert result['confidence'] > 0
        assert result['method'] in ['langdetect', 'character_analysis']

    def test_detect_language_unsupported(self):
        """Тест определения неподдерживаемого языка"""
        # Французский текст (не поддерживается)
        text = "Ceci est un texte en français pour tester la détection de langue."
        
        result = self.detector.detect_language(text)
        
        # Должен вернуться английский как fallback
        assert result['language'] == 'en'
        assert result['confidence'] == 0.5

    def test_fallback_detection_russian(self):
        """Тест fallback определения русского языка по символам"""
        text = "текст с русскими буквами " * 10
        
        result = self.detector._fallback_detection(text)
        
        assert result['language'] == 'ru'
        assert 'confidence' in result
        assert result['method'] == 'character_analysis'

    def test_fallback_detection_german(self):
        """Тест fallback определения немецкого языка по символам"""
        # Увеличиваем количество немецких символов для срабатывания порога
        text = "ä ö ü ß " * 5 + "Text mit deutschen Umlauten"
        
        result = self.detector._fallback_detection(text)
        
        assert result['language'] == 'de'
        assert 'confidence' in result
        assert result['method'] == 'character_analysis'

    def test_fallback_detection_default(self):
        """Тест fallback определения по умолчанию"""
        text = "Simple text without specific characters"
        
        result = self.detector._fallback_detection(text)
        
        assert result['language'] == 'en'
        assert result['confidence'] == 0.5
        assert result['method'] == 'default'

    def test_get_language_name(self):
        """Тест получения названия языка по коду"""
        assert self.detector.get_language_name('en') == 'English'
        assert self.detector.get_language_name('ru') == 'Russian'
        assert self.detector.get_language_name('de') == 'German'
        assert self.detector.get_language_name('fr') == 'Unknown'

    def test_detect_language_simple_wrapper(self):
        """Тест функции-обертки для обратной совместимости"""
        text = "This is English text"
        
        result = detect_language_simple(text)
        
        assert 'language' in result
        assert 'confidence' in result
        assert isinstance(result['language'], str)
        assert isinstance(result['confidence'], float)

    def test_mixed_language_text(self):
        """Тест текста со смешанными языками"""
        text = "This is English and это русский текст together."
        
        result = self.detector.detect_language(text)
        
        # Должен определить один из языков
        assert result['language'] in ['en', 'ru']
        assert result['confidence'] > 0

    def test_text_with_numbers_and_symbols(self):
        """Тест текста с числами и символами"""
        text = "Test 123 with numbers !@#$ and symbols 45.6%"
        
        result = self.detector.detect_language(text)
        
        assert result['language'] == 'en'
        assert 'confidence' in result