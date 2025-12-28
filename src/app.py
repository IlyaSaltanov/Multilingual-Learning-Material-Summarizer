"""Минимальный Multilingual Summarizer для MacBook."""

import os
import re
import ssl
from flask import Flask, render_template, request, jsonify
import nltk
from langdetect import detect, DetectorFactory

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

# Указываем явный путь к папке templates (на уровень выше в src/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "../templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Поддерживаемые языки
SUPPORTED_LANGUAGES = {"en": "English", "ru": "Russian", "de": "German"}


def simple_tokenize(text):
    """Простая токенизация если NLTK не работает."""
    # Разделяем по точкам, восклицательным и вопросительным знакам
    sentences = []
    current_sentence = []

    for char in text:
        current_sentence.append(char)
        if char in ".!?。！？":
            sentences.append("".join(current_sentence).strip())
            current_sentence = []

    if current_sentence:
        sentences.append("".join(current_sentence).strip())

    return [s for s in sentences if s]


def detect_language_simple(text):
    """Простое определение языка."""
    if len(text.strip()) < 20:
        return {"language": "en", "confidence": 0.5}

    try:
        detected = detect(text)
        if detected in SUPPORTED_LANGUAGES:
            return {"language": detected, "confidence": 0.9}
    except Exception:
        pass

    # Простая проверка по символам
    text_lower = text.lower()
    ru_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    de_chars = set("äöüß")

    ru_count = sum(1 for c in text_lower[:200] if c in ru_chars)
    de_count = sum(1 for c in text_lower[:200] if c in de_chars)

    if ru_count > 10:
        return {"language": "ru", "confidence": min(0.9, ru_count / 100)}
    elif de_count > 5:
        return {"language": "de", "confidence": min(0.9, de_count / 50)}

    return {"language": "en", "confidence": 0.5}


def select_sentences_for_summary(cleaned_sentences, target_sentences):
    """Вспомогательная функция для выбора предложений для суммаризации."""
    result_sentences = []

    if not cleaned_sentences:
        return result_sentences

    # Всегда включаем первое предложение
    result_sentences.append(cleaned_sentences[0])

    # Добавляем средние предложения
    if len(cleaned_sentences) > 3:
        middle_idx = len(cleaned_sentences) // 2
        if middle_idx < len(cleaned_sentences) and len(result_sentences) < target_sentences:
            result_sentences.append(cleaned_sentences[middle_idx])

    # Добавляем последнее предложение если есть место
    if len(cleaned_sentences) > 1 and len(result_sentences) < target_sentences:
        result_sentences.append(cleaned_sentences[-1])

    # Добавляем другие предложения если нужно
    if len(result_sentences) < target_sentences and len(cleaned_sentences) > 2:
        for i in range(1, len(cleaned_sentences) - 1):
            if i != middle_idx and len(result_sentences) < target_sentences:
                result_sentences.append(cleaned_sentences[i])

    return result_sentences[:target_sentences]


def summarize_text_extractive(text, language, compression_percent):
    """Простой extractive summarizer."""
    sentences = []

    try:
        # Пробуем NLTK токенизацию
        if language == "ru":
            sentences = nltk.sent_tokenize(text, language="russian")
        elif language == "de":
            sentences = nltk.sent_tokenize(text, language="german")
        else:
            sentences = nltk.sent_tokenize(text, language="english")
    except Exception:
        # Fallback на простую токенизацию
        sentences = simple_tokenize(text)

    if len(sentences) <= 3:
        return text

    # Очищаем предложения
    cleaned_sentences = []
    for sentence in sentences:
        clean_sentence = re.sub(r"\s+", " ", sentence).strip()
        if len(clean_sentence.split()) > 3:
            cleaned_sentences.append(sentence)

    if not cleaned_sentences:
        return text

    # Выбираем предложения на основе длины
    target_sentences = max(
        2, int(len(cleaned_sentences) * (compression_percent / 100)))

    # Получаем предложения для суммаризации
    result_sentences = select_sentences_for_summary(
        cleaned_sentences, target_sentences)

    return " ".join(result_sentences)


@app.route("/")
def home():
    """Главная страница."""
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

    app.run(host="0.0.0.0", port=port, debug=debug)
