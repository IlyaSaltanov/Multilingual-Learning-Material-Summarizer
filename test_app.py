import sys
sys.path.insert(0, 'src')

try:
    import app
    print("✅ app.py импортирован")
    
    # Проверим основные функции
    test_text = "Hello world. This is a test sentence."
    
    # Проверка определения языка
    if hasattr(app, 'detect_language_simple'):
        result = app.detect_language_simple(test_text)
        print(f"✅ Language detection: {result}")
    
    # Проверка суммаризации
    if hasattr(app, 'summarize_text_extractive'):
        summary = app.summarize_text_extractive(test_text, 'en', 30)
        print(f"✅ Summarization: {summary[:50]}...")
    
    # Проверка Flask приложения
    with app.app.test_client() as client:
        response = client.get('/health')
        print(f"✅ Health endpoint: {response.status_code}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
