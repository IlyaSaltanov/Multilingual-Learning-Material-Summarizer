"""
Модуль для определения языка текста
"""

from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from typing import Dict


class LanguageDetector:
    """Класс для определения языка текста"""

    def __init__(self):
        # Для консистентности результатов
        DetectorFactory.seed = 42
        self.supported_languages = ["en", "ru", "de"]

    def detect_language(self, text: str) -> Dict[str, any]:
        """
        Определяет язык текста

        Args:
            text: Входной текст (минимум 20 символов)

        Returns:
            Словарь с результатом определения
        """
        if len(text.strip()) < 20:
            return {"language": "en", "confidence": 0.5, "method": "fallback"}

        # Пробуем langdetect
        try:
            detected = detect(text)
            confidence = 0.9

            # Если язык не поддерживается, возвращаем английский
            if detected not in self.supported_languages:
                detected = "en"
                confidence = 0.5

            return {
                "language": detected,
                "confidence": confidence,
                "method": "langdetect",
            }

        except (LangDetectException, Exception):
            # Fallback: простая проверка по символам
            return self._fallback_detection(text)

    def _fallback_detection(self, text: str) -> Dict[str, any]:
        """Резервный метод определения языка по символам"""
        text_lower = text.lower()

        # Русские символы
        ru_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        ru_count = sum(1 for c in text_lower[:200] if c in ru_chars)

        # Немецкие специфические символы
        de_chars = set("äöüß")
        de_count = sum(1 for c in text_lower[:200] if c in de_chars)

        if ru_count > 10:
            confidence = min(0.9, ru_count / 100)
            return {
                "language": "ru",
                "confidence": confidence,
                "method": "character_analysis",
            }
        elif de_count > 5:
            confidence = min(0.9, de_count / 50)
            return {
                "language": "de",
                "confidence": confidence,
                "method": "character_analysis",
            }
        else:
            return {"language": "en", "confidence": 0.5, "method": "default"}

    def get_language_name(self, code: str) -> str:
        """Возвращает название языка по коду"""
        names = {"en": "English", "ru": "Russian", "de": "German"}
        return names.get(code, "Unknown")


# Функции для обратной совместимости
def detect_language_simple(text: str) -> Dict[str, any]:
    """Простая функция для обратной совместимости"""
    detector = LanguageDetector()
    result = detector.detect_language(text)
    return {"language": result["language"], "confidence": result["confidence"]}
