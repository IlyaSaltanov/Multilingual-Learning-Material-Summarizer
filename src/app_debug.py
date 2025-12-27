import os
import sys
import traceback
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Простые функции для теста
def simple_summarize(text, language, compression):
    """Упрощенная суммаризация для отладки"""
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) <= 2:
        return text

    # Берем первое и последнее предложение
    result = []
    if sentences:
        result.append(sentences[0])
    if len(sentences) > 1:
        result.append(sentences[-1])

    return ". ".join(result) + "."


@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error loading template: {str(e)}"


@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        app.logger.info("Summarize endpoint called")

        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()
        app.logger.info(f"Received data: {data}")

        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data.get("text", "").strip()
        if len(text) < 10:
            return jsonify({"error": "Text too short"}), 400

        language = data.get("language", "en")
        compression = data.get("compression", 30)

        # Используем упрощенную суммаризацию
        summary = simple_summarize(text, language, compression)

        response = {
            "success": True,
            "summary": summary,
            "language": language,
            "original_length": len(text.split()),
            "summary_length": len(summary.split()),
        }

        return jsonify(response)

    except Exception as e:
        app.logger.error(f"Error in summarize: {traceback.format_exc()}")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "service": "Debug Version",
            "endpoints": ["/", "/summarize", "/health"],
        }
    )


if __name__ == "__main__":
    print("🔧 Starting debug server on port 5001...")
    print("📁 Template path:", app.template_folder)
    print("📁 Static path:", app.static_folder)

    # Проверим пути
    import os

    print("Current directory:", os.getcwd())
    print("Templates exists:", os.path.exists("templates"))

    app.run(host="0.0.0.0", port=5001, debug=True)
