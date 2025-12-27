"""
Вспомогательные утилиты
"""

import os
import nltk
import urllib.request
import tempfile
import zipfile
import shutil
import ssl
from typing import List, Tuple

def disable_ssl():
    """Отключаем SSL проверку"""
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

def setup_nltk():
    """Устанавливаем NLTK данные если их нет"""
    print("🔧 Настройка NLTK...")
    
    disable_ssl()  # Отключаем SSL для всех операций
    
    # Проверяем наличие данных
    try:
        nltk.data.find('tokenizers/punkt')
        print("✅ NLTK данные уже установлены")
        return True
    except LookupError:
        print("📥 NLTK данные не найдены, пробую установить...")
    
    try:
        # Пробуем скачать
        print("Скачиваю punkt...")
        nltk.download('punkt', quiet=True)
        
        # Для русского и немецкого
        try:
            nltk.download('punkt_tab', quiet=True)
        except:
            print("⚠️  punkt_tab недоступен, использую стандартный punkt")
        
        print("✅ NLTK данные установлены")
        return True
        
    except Exception as e:
        print(f"⚠️  Ошибка установки NLTK: {e}")
        print("Приложение будет использовать fallback токенизацию")
        return False

def simple_tokenize(text: str) -> List[str]:
    """Простая токенизация если NLTK не работает"""
    sentences = []
    current = []
    
    for char in text:
        current.append(char)
        if char in '.!?。！？':
            sentence = ''.join(current).strip()
            if sentence:
                sentences.append(sentence)
            current = []
    
    if current:
        sentences.append(''.join(current).strip())
    
    return [s for s in sentences if s]

def validate_text_length(text: str, min_len: int = 50, max_len: int = 10000) -> Tuple[bool, str]:
    """
    Валидация длины текста
    
    Returns:
        (is_valid, error_message)
    """
    length = len(text)
    
    if length < min_len:
        return False, f"Text too short (min {min_len} characters)"
    
    if length > max_len:
        return False, f"Text too long (max {max_len} characters)"
    
    return True, ""

def split_into_chunks(text: str, max_chunk_size: int = 5000) -> List[str]:
    """Разделяет длинный текст на части"""
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        current_chunk.append(word)
        current_size += len(word) + 1
        
        if current_size >= max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_size = 0
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks
