"""
WSGI entry point for Render deployment.
"""

import sys
import os

# Добавляем корень проекта в путь Python
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

print(f"✅ Current directory: {current_dir}")
print(f"✅ Files in directory: {os.listdir(current_dir)}")

# Импортируем приложение из src/app.py
try:
    from src.app import app
    print("✅ Successfully imported app from src.app")
except ImportError as e:
    print(f"❌ ImportError: {e}")
    print("🔄 Trying alternative import...")

    # Альтернативный импорт
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "app",
        os.path.join(current_dir, "src", "app.py")
    )
    app_module = importlib.util.module_from_spec(spec)
    sys.modules["app"] = app_module
    spec.loader.exec_module(app_module)
    app = app_module.app
    print("✅ Successfully imported app using importlib")

# Экспортируем для gunicorn
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
