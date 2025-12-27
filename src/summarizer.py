"""
Модуль для суммаризации текста на разных языках
"""

import re
import nltk
from typing import List, Dict, Optional


class TextSummarizer:
    """Класс для извлечения и абстрактивной суммаризации текста"""

    def __init__(self):
        self.supported_languages = {"en": "english", "ru": "russian", "de": "german"}

    def extract_sentences(self, text: str, language: str) -> List[str]:
        """
        Извлекает предложения из текста с учетом языка

        Args:
            text: Входной текст
            language: Код языка ('en', 'ru', 'de')

        Returns:
            Список предложений
        """
        try:
            nltk_lang = self.supported_languages.get(language, "english")
            sentences = nltk.sent_tokenize(text, language=nltk_lang)
        except:
            # Fallback простая токенизация
            sentences = self._simple_tokenize(text)

        # Фильтруем короткие предложения
        return [s for s in sentences if len(s.split()) > 3]

    def _simple_tokenize(self, text: str) -> List[str]:
        """Простая токенизация если NLTK не работает"""
        sentences = []
        current = []

        for char in text:
            current.append(char)
            if char in ".!?。！？":
                sentence = "".join(current).strip()
                if sentence:
                    sentences.append(sentence)
                current = []

        if current:
            sentences.append("".join(current).strip())

        return sentences

    def summarize_extractive(
        self, text: str, language: str = "en", compression_percent: int = 30
    ) -> str:
        """
        Извлекающая суммаризация текста

        Args:
            text: Входной текст
            language: Код языка
            compression_percent: Процент сжатия (20, 30, 50)

        Returns:
            Суммаризированный текст
        """
        sentences = self.extract_sentences(text, language)

        if len(sentences) <= 3:
            return text

        # Вычисляем сколько предложений оставить
        target_count = max(2, int(len(sentences) * (compression_percent / 100)))

        # Стратегия выбора предложений:
        # 1. Первое предложение (обычно содержит основную идею)
        # 2. Последнее предложение (часто содержит вывод)
        # 3. Средние предложения по длине (содержат детали)

        selected_indices = [0]  # Всегда первое предложение

        if len(sentences) > 1:
            selected_indices.append(-1)  # Последнее предложение

        # Добавляем средние по длине предложения
        if len(sentences) > 3:
            # Находим средние по длине предложения
            lengths = [len(s.split()) for s in sentences]
            avg_length = sum(lengths) / len(lengths)

            # Индексы предложений средней длины
            middle_indices = [
                i
                for i, length in enumerate(lengths)
                if i not in selected_indices
                and abs(length - avg_length) <= avg_length * 0.5
            ]

            # Добавляем пока не достигнем нужного количества
            for idx in middle_indices:
                if len(selected_indices) < target_count:
                    selected_indices.append(idx)

        # Собираем результат в оригинальном порядке
        selected_indices.sort()
        result = [sentences[i] for i in selected_indices[:target_count]]

        return " ".join(result)

    def calculate_statistics(
        self, original_text: str, summary_text: str
    ) -> Dict[str, any]:
        """
        Вычисляет статистику суммаризации

        Returns:
            Словарь со статистикой
        """
        original_words = len(original_text.split())
        summary_words = len(summary_text.split())

        if original_words == 0:
            reduction = 0
        else:
            reduction = round((1 - summary_words / original_words) * 100, 1)

        return {
            "original_length": original_words,
            "summary_length": summary_words,
            "reduction_percent": reduction,
            "compression_ratio": f"{summary_words}:{original_words}",
        }


# Для обратной совместимости с старым кодом
def summarize_text_extractive(
    text: str, language: str, compression_percent: int
) -> str:
    """Функция-обертка для обратной совместимости"""
    summarizer = TextSummarizer()
    return summarizer.summarize_extractive(text, language, compression_percent)
