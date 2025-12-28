"""
Тесты модуля суммаризации
"""

from summarizer import TextSummarizer
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))


class TestTextSummarizer:
    """Тесты для класса TextSummarizer"""

    def setup_method(self):
        self.summarizer = TextSummarizer()

    def test_initialization(self):
        """Тест инициализации"""
        assert hasattr(self.summarizer, 'supported_languages')

    def test_extract_sentences_simple(self):
        """Простой тест извлечения предложений"""
        text = "First sentence. Second sentence."
        sentences = self.summarizer.extract_sentences(text, 'en')
        assert isinstance(sentences, list)

    def test_summarize_extractive_simple(self):
        """Простой тест суммаризации"""
        text = "Text to summarize."
        summary = self.summarizer.summarize_extractive(text, 'en', 50)
        assert isinstance(summary, str)

    def test_calculate_statistics_simple(self):
        """Тест расчета статистики"""
        stats = self.summarizer.calculate_statistics("Original", "Summary")
        assert isinstance(stats, dict)
