#!/usr/bin/env python3
"""
Скрипт для установки NLTK данных на Mac с проблемами SSL
"""

import os
import sys
import urllib.request
import tempfile
import zipfile
import shutil
import ssl

# Отключаем SSL проверку
ssl._create_default_https_context = ssl._create_unverified_context

def download_and_install():
    """Скачать и установить NLTK данные"""
    
    # Создаем директорию для nltk_data
    nltk_data_dir = os.path.expanduser('~/nltk_data')
    tokenizers_dir = os.path.join(nltk_data_dir, 'tokenizers')
    
    print(f"📁 Директория NLTK данных: {nltk_data_dir}")
    
    # Создаем директории если их нет
    os.makedirs(tokenizers_dir, exist_ok=True)
    
    # Скачиваем punkt
    punkt_url = "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip"
    
    print("📥 Скачиваю punkt...")
    
    try:
        # Создаем временную директорию
        temp_dir = tempfile.mkdtemp()
        punkt_zip = os.path.join(temp_dir, "punkt.zip")
        
        # Скачиваем
        urllib.request.urlretrieve(punkt_url, punkt_zip)
        
        # Распаковываем
        with zipfile.ZipFile(punkt_zip, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # Копируем .pickle файлы
        count = 0
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith('.pickle'):
                    src = os.path.join(root, file)
                    dst = os.path.join(tokenizers_dir, file)
                    shutil.copy2(src, dst)
                    count += 1
                    print(f"  ✅ {file}")
        
        print(f"\n🎉 Успешно установлено {count} файлов punkt")
        print(f"📂 Файлы находятся в: {tokenizers_dir}")
        
        # Очищаем временные файлы
        shutil.rmtree(temp_dir)
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

if __name__ == '__main__':
    print("🔧 Установка NLTK данных для Multilingual Summarizer")
    print("=" * 50)
    
    if download_and_install():
        print("\n✅ Установка завершена успешно!")
        print("\nТеперь можно запустить приложение:")
        print("python app.py")
    else:
        print("\n❌ Установка не удалась")
        sys.exit(1)