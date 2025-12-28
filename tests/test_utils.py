"""
Тесты вспомогательных утилит
"""

import sys
import os
import pytest

# Добавляем src в путь импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import (
    simple_tokenize, 
    validate_text_length, 
    split_into_chunks
)


class TestUtils:
    """Тесты вспомогательных функций"""

    def test_simple_tokenize_basic(self):
        """Тест простой токенизации"""
        text = "First sentence. Second sentence! Third sentence?"
        
        sentences = simple_tokenize(text)
        
        assert isinstance(sentences, list)
        assert len(sentences) == 3
        assert "First sentence." in sentences[0]
        assert "Second sentence!" in sentences[1]
        assert "Third sentence?" in sentences[2]

    def test_simple_tokenize_no_punctuation(self):
        """Тест токенизации без пунктуации"""
        text = "This is a single sentence without ending punctuation"
        
        sentences = simple_tokenize(text)
        
        assert isinstance(sentences, list)
        assert len(sentences) == 1
        assert sentences[0] == text

    def test_simple_tokenize_empty(self):
        """Тест токенизации пустого текста"""
        sentences = simple_tokenize("")
        
        assert isinstance(sentences, list)
        assert len(sentences) == 0

    def test_simple_tokenize_multiple_spaces(self):
        """Тест токенизации с множественными пробелами"""
        text = "Sentence  one.  Sentence   two!"
        
        sentences = simple_tokenize(text)
        
        assert isinstance(sentences, list)
        assert len(sentences) == 2
        # Проверяем что пробелы сохраняются внутри предложения
        assert "Sentence  one." in sentences[0]

    def test_validate_text_length_valid(self):
        """Тест валидации корректной длины текста"""
        text = "A" * 100  # 100 символов
        
        is_valid, message = validate_text_length(text, min_len=50, max_len=1000)
        
        assert is_valid is True
        assert message == ""

    def test_validate_text_length_too_short(self):
        """Тест валидации слишком короткого текста"""
        text = "Short"
        
        is_valid, message = validate_text_length(text, min_len=50, max_len=1000)
        
        assert is_valid is False
        assert "too short" in message.lower()
        assert "50" in message

    def test_validate_text_length_too_long(self):
        """Тест валидации слишком длинного текста"""
        text = "A" * 15000
        
        is_valid, message = validate_text_length(text, min_len=50, max_len=10000)
        
        assert is_valid is False
        assert "too long" in message.lower()
        assert "10000" in message

    def test_validate_text_length_custom_limits(self):
        """Тест валидации с пользовательскими лимитами"""
        text = "A" * 75
        
        # Слишком короткий для min_len=100
        is_valid1, _ = validate_text_length(text, min_len=100, max_len=1000)
        assert is_valid1 is False
        
        # Корректный для min_len=50
        is_valid2, _ = validate_text_length(text, min_len=50, max_len=1000)
        assert is_valid2 is True

    def test_split_into_chunks_basic(self):
        """Тест разделения на части"""
        text = "word1 word2 word3 word4 word5 word6 word7 word8"
        
        chunks = split_into_chunks(text, max_chunk_size=20)
        
        assert isinstance(chunks, list)
        assert len(chunks) > 1  # Должен разделиться на несколько частей
        assert all(isinstance(chunk, str) for chunk in chunks)
        
        # Проверяем что все слова сохранились
        all_words = " ".join(chunks).split()
        assert len(all_words) == 8

    def test_split_into_chunks_single_chunk(self):
        """Тест когда текст помещается в одну часть"""
        text = "Short text"
        
        chunks = split_into_chunks(text, max_chunk_size=100)
        
        assert isinstance(chunks, list)
        assert len(chunks) == 1
        assert chunks[0] == text

    def test_split_into_chunks_empty(self):
        """Тест разделения пустого текста"""
        chunks = split_into_chunks("", max_chunk_size=100)
        
        assert isinstance(chunks, list)
        # Для пустого текста может вернуться пустой список или список с пустой строкой
        # Оба варианта приемлемы
        if chunks:
            assert len(chunks) == 1
            assert chunks[0] == ""
        else:
            assert len(chunks) == 0

    def test_split_into_chunks_with_long_words(self):
        """Тест с очень длинными словами"""
        text = "a" * 100 + " " + "b" * 100  # Два очень длинных слова
        
        chunks = split_into_chunks(text, max_chunk_size=50)
        
        # Каждое слово должно быть в отдельном чанке или оба в одном
        # Зависит от реализации
        assert len(chunks) >= 1
        # Проверяем что все символы сохранились
        reconstructed = " ".join(chunks)
        assert len(reconstructed.replace(" ", "")) == 200

    def test_split_preserves_word_order(self):
        """Тест что порядок слов сохраняется"""
        text = "one two three four five six seven eight nine ten"
        
        chunks = split_into_chunks(text, max_chunk_size=15)
        
        # Объединяем и проверяем порядок
        reconstructed = " ".join(chunks)
        assert reconstructed == text


if __name__ == '__main__':
    pytest.main()