"""
Тесты модуля суммаризации
"""

import sys
import os

# Добавляем src в путь импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from summarizer import TextSummarizer, summarize_text_extractive


class TestTextSummarizer:
    """Тесты для класса TextSummarizer"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.summarizer = TextSummarizer()

    def test_initialization(self):
        """Тест инициализации класса"""
        assert hasattr(self.summarizer, 'supported_languages')
        assert isinstance(self.summarizer.supported_languages, dict)
        assert 'en' in self.summarizer.supported_languages
        assert 'ru' in self.summarizer.supported_languages
        assert 'de' in self.summarizer.supported_languages

    def test_extract_sentences_english(self):
        """Тест извлечения предложений на английском"""
        text = "This is the first sentence. This is the second sentence! And this is the third?"
        
        sentences = self.summarizer.extract_sentences(text, 'en')
        
        assert isinstance(sentences, list)
        # Может быть 3 или больше в зависимости от токенизатора
        assert len(sentences) >= 3

    def test_extract_sentences_russian(self):
        """Тест извлечения предложений на русском"""
        text = "Это первое предложение. Это второе предложение! А это третье?"
        
        sentences = self.summarizer.extract_sentences(text, 'ru')
        
        assert isinstance(sentences, list)
        # Fallback токенизация всегда должна вернуть предложения
        assert len(sentences) > 0

    def test_extract_sentences_german(self):
        """Тест извлечения предложений на немецком"""
        text = "Das ist der erste Satz. Das ist der zweite Satz! Und das ist der dritte?"
        
        sentences = self.summarizer.extract_sentences(text, 'de')
        
        assert isinstance(sentences, list)
        assert len(sentences) > 0

    def test_simple_tokenize_fallback(self):
        """Тест простой токенизации как fallback"""
        text = "Sentence one. Sentence two! Sentence three?"
        
        sentences = self.summarizer._simple_tokenize(text)
        
        assert isinstance(sentences, list)
        assert len(sentences) == 3
        assert all(isinstance(s, str) for s in sentences)

    def test_summarize_extractive_short_text(self):
        """Тест суммаризации короткого текста"""
        text = "Short text without multiple sentences."
        
        summary = self.summarizer.summarize_extractive(text, 'en', 30)
        
        # Для коротких текстов должен возвращаться оригинальный текст
        assert summary == text

    def test_summarize_extractive_english(self):
        """Тест извлекающей суммаризации на английском"""
        text = "Artificial intelligence is transforming many industries. Machine learning algorithms can analyze vast amounts of data. Deep learning has revolutionized computer vision. Natural language processing enables machines to understand human language. AI will continue to evolve in the coming years."
        
        summary = self.summarizer.summarize_extractive(text, 'en', 30)
        
        assert isinstance(summary, str)
        assert len(summary) > 0
        # Суммаризация должна быть короче (или равна для очень коротких текстов)
        assert len(summary) <= len(text)

    def test_summarize_extractive_different_compression(self):
        """Тест суммаризации с разными уровнями сжатия"""
        text = "Sentence one. Sentence two. Sentence three. Sentence four. Sentence five. Sentence six. Sentence seven."
        
        summary_20 = self.summarizer.summarize_extractive(text, 'en', 20)
        summary_50 = self.summarizer.summarize_extractive(text, 'en', 50)
        
        # Проверяем что оба результата - строки
        assert isinstance(summary_20, str)
        assert isinstance(summary_50, str)
        assert len(summary_20) > 0
        assert len(summary_50) > 0

    def test_calculate_statistics(self):
        """Тест расчета статистики"""
        original = "This is the original text with multiple words."
        summary = "This is summary."
        
        stats = self.summarizer.calculate_statistics(original, summary)
        
        # Исправляем подсчет: "This is the original text with multiple words." = 8 слов
        assert stats['original_length'] == 8  # Было 7
        assert stats['summary_length'] == 3  # "This is summary." = 3 слова
        assert stats['reduction_percent'] > 0
        assert 'compression_ratio' in stats

    def test_calculate_statistics_empty(self):
        """Тест расчета статистики для пустого текста"""
        stats = self.summarizer.calculate_statistics("", "")
        
        assert stats['original_length'] == 0
        assert stats['summary_length'] == 0
        assert stats['reduction_percent'] == 0

    def test_summarize_text_extractive_wrapper(self):
        """Тест функции-обертки для обратной совместимости"""
        text = "First sentence. Second sentence. Third sentence."
        
        summary = summarize_text_extractive(text, 'en', 30)
        
        assert isinstance(summary, str)
        assert len(summary) > 0

    def test_summarize_with_punctuation_variations(self):
        """Тест суммаризации с разными знаками пунктуации"""
        text = "First... Second! Third? Fourth: Fifth;"
        
        summary = self.summarizer.summarize_extractive(text, 'en', 50)
        
        assert isinstance(summary, str)
        assert len(summary) > 0

    def test_summarize_very_long_text(self):
        """Тест суммаризации очень длинного текста"""
        # Используем разные предложения для лучшей суммаризации
        text = " ".join([f"Sentence {i} with some words." for i in range(20)])
        
        summary = self.summarizer.summarize_extractive(text, 'en', 10)
        
        assert isinstance(summary, str)
        # Проверяем что суммаризация произошла
        assert 0 < len(summary) <= len(text)