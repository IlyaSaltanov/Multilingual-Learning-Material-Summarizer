"""Минимальный Multilingual Summarizer для MacBook."""

import os
import ssl
from flask import Flask, render_template, request, jsonify
import nltk
from langdetect import DetectorFactory 

# Импорты из модулей (без src)
from language_detector import detect_language_simple
from summarizer import summarize_text_extractive

# Отключаем SSL проверку для NLTK (решение для Mac)
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Для консистентного определения языка
DetectorFactory.seed = 42


def download_nltk_data():
    """Скачиваем NLTK данные при первом запуске (с SSL bypass)."""
    try:
        nltk.data.find("tokenizers/punkt")
        print("✅ NLTK данные уже загружены")
    except LookupError:
        print("📥 Загружаю NLTK данные...")
        try:
            nltk.download("punkt", quiet=True)
            nltk.download("punkt_tab", quiet=True)
            print("✅ NLTK данные успешно загружены")
        except Exception as e:
            print(f"⚠️  Ошибка загрузки NLTK данных: {e}")
            print("Попробую альтернативный метод...")
            # Попробуем скачать вручную
            import urllib.request
            import tempfile
            import zipfile
            import shutil

            # Скачиваем punkt напрямую
            punkt_url = "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip"
            temp_dir = tempfile.mkdtemp()

            try:
                # Скачиваем архив
                print("Скачиваю punkt напрямую...")
                urllib.request.urlretrieve(
                    punkt_url, os.path.join(temp_dir, "punkt.zip")
                )

                # Распаковываем
                with zipfile.ZipFile(
                    os.path.join(temp_dir, "punkt.zip"), "r"
                ) as zip_ref:
                    zip_ref.extractall(temp_dir)

                # Копируем в папку nltk_data
                nltk_data_dir = os.path.expanduser("~/nltk_data")
                tokenizers_dir = os.path.join(nltk_data_dir, "tokenizers")

                os.makedirs(tokenizers_dir, exist_ok=True)

                # Ищем файлы punkt
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        if "punkt" in file and file.endswith(".pickle"):
                            src = os.path.join(root, file)
                            dst = os.path.join(tokenizers_dir, file)
                            shutil.copy2(src, dst)
                            print(f"Скопирован: {file}")

                print("✅ NLTK данные установлены вручную")
            except Exception as e2:
                print(f"❌ Не удалось установить NLTK данные: {e2}")
                print("Приложение будет использовать fallback токенизацию")


# Загружаем данные
download_nltk_data()

# Указываем явный путь к папке templates и static (на уровень выше в src/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "../templates")
STATIC_DIR = os.path.join(BASE_DIR, "../static")

app = Flask(__name__,
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR)

# Поддерживаемые языки
SUPPORTED_LANGUAGES = {"en": "English", "ru": "Russian", "de": "German"}


@app.route("/")
def home():
    """Главная страница."""
    print(f"📁 Template path: {TEMPLATE_DIR}")
    print(f"📁 Static path: {STATIC_DIR}")
    print(f"📁 Current dir: {os.getcwd()}")
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    """API endpoint для суммаризации."""
    try:
        # Получаем данные
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data["text"].strip()

        if len(text) < 50:
            return jsonify({"error": "Text too short (min 50 characters)"}), 400

        # Определяем язык
        language = data.get("language", "auto")
        if language == "auto":
            detected = detect_language_simple(text)
            language = detected["language"]
            confidence = detected["confidence"]
        else:
            confidence = 1.0

        # Получаем уровень сжатия
        compression = data.get("compression", 30)
        if compression not in [20, 30, 50]:
            compression = 30

        # Суммаризируем текст
        summary = summarize_text_extractive(text, language, compression)

        # Считаем статистику
        original_words = len(text.split())
        summary_words = len(summary.split())

        response = {
            "success": True,
            "summary": summary,
            "language": language,
            "language_name": SUPPORTED_LANGUAGES.get(language, "Unknown"),
            "confidence": round(confidence, 2),
            "compression": compression,
            "original_length": original_words,
            "summary_length": summary_words,
            "reduction": round((1 - summary_words / original_words) * 100, 1)
            if original_words > 0
            else 0,
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "Multilingual Summarizer"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"

    print(f"🚀 Запуск Multilingual Summarizer на порту {port}")
    print(f"🌐 Откройте http://localhost:{port} в браузере")
    print("📝 Поддерживаемые языки: English, Russian, German")
    print(f"📁 Путь к шаблонам: {TEMPLATE_DIR}")
    print(f"📁 Путь к статическим файлам: {STATIC_DIR}")

    app.run(host="0.0.0.0", port=port, debug=debug)
