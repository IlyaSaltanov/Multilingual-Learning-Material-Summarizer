"""Минимальный Multilingual Summarizer для MacBook."""

import os
import ssl
import sys
from flask import Flask, render_template, request, jsonify
import nltk
from langdetect import DetectorFactory

# 🔧 ВАЖНО: Добавляем пути для корректного импорта
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Добавляем родительскую директорию в Python path
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Добавляем текущую директорию (src/) в Python path
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

print(f"🔧 Python path настроен:")
print(f"   - Current dir: {current_dir}")
print(f"   - Parent dir: {parent_dir}")
print(f"   - In sys.path: {'src' in ' '.join(sys.path)}")

# 🔧 ИСПРАВЛЕННЫЕ ИМПОРТЫ:
# Способ 1: Пробуем относительные импорты
try:
    from .language_detector import detect_language_simple
    from .summarizer import summarize_text_extractive
    print("✅ Успешно импортировали модули через относительные импорты")
except ImportError as e:
    print(f"⚠️  Относительные импорты не сработали: {e}")

    # Способ 2: Пробуем абсолютные импорты
    try:
        from src.language_detector import detect_language_simple
        from src.summarizer import summarize_text_extractive
        print("✅ Успешно импортировали модули через абсолютные импорты")
    except ImportError as e2:
        print(f"⚠️  Абсолютные импорты не сработали: {e2}")

        # Способ 3: Прямые импорты (для локальной разработки)
        try:
            from language_detector import detect_language_simple
            from summarizer import summarize_text_extractive
            print("✅ Успешно импортировали модули напрямую")
        except ImportError as e3:
            print(f"❌ Все методы импорта не сработали: {e3}")
            print("🔄 Проверяю содержимое директории:")
            print(f"   Файлы в {current_dir}: {os.listdir(current_dir)}")

            # Последняя попытка: динамический импорт
            import importlib.util

            # Импортируем language_detector
            ld_path = os.path.join(current_dir, 'language_detector.py')
            spec = importlib.util.spec_from_file_location(
                "language_detector", ld_path)
            ld_module = importlib.util.module_from_spec(spec)
            sys.modules["language_detector"] = ld_module
            spec.loader.exec_module(ld_module)
            detect_language_simple = ld_module.detect_language_simple

            # Импортируем summarizer
            sum_path = os.path.join(current_dir, 'summarizer.py')
            spec = importlib.util.spec_from_file_location(
                "summarizer", sum_path)
            sum_module = importlib.util.module_from_spec(spec)
            sys.modules["summarizer"] = sum_module
            spec.loader.exec_module(sum_module)
            summarize_text_extractive = sum_module.summarize_text_extractive

            print("✅ Успешно импортировали модули через importlib")

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
    return jsonify({
        "status": "healthy",
        "service": "Multilingual Summarizer",
        "python_version": sys.version.split()[0]
    })


@app.route("/debug")
def debug():
    """Debug endpoint для проверки путей."""
    return jsonify({
        "current_dir": os.path.dirname(os.path.abspath(__file__)),
        "template_dir": TEMPLATE_DIR,
        "static_dir": STATIC_DIR,
        "template_exists": os.path.exists(TEMPLATE_DIR),
        "static_exists": os.path.exists(STATIC_DIR),
        "sys_path": sys.path,
        "import_success": "language_detector" in sys.modules and "summarizer" in sys.modules
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    debug = os.environ.get("FLASK_ENV") == "development"

    print(f"🚀 Запуск Multilingual Summarizer на порту {port}")
    print(f"🌐 Откройте http://localhost:{port} в браузере")
    print("📝 Поддерживаемые языки: English, Russian, German")
    print(
        f"📁 Путь к шаблонам: {TEMPLATE_DIR} (существует: {os.path.exists(TEMPLATE_DIR)})")
    print(
        f"📁 Путь к статическим файлам: {STATIC_DIR} (существует: {os.path.exists(STATIC_DIR)})")

    app.run(host="0.0.0.0", port=port, debug=debug)
