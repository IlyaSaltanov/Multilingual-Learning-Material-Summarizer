"""
Тесты вспомогательных утилит
"""

from utils import simple_tokenize
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestUtils:
    """Тесты вспомогательных функций"""

    def test_simple_tokenize(self):
        """Тест простой токенизации"""
        sentences = simple_tokenize("First. Second!")
        assert isinstance(sentences, list)
