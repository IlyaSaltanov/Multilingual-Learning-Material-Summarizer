# 🌍 Multilingual Learning Material Summarizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://github.com/yourusername/Multilingual-Summarizer/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yourusername/Multilingual-Summarizer/actions)

<div align="center">
  <img src="https://via.placeholder.com/800x400/667eea/ffffff?text=AI+Powered+Multilingual+Summarizer" alt="Multilingual Summarizer Banner" width="800"/>
  
  **✨ Интеллектуальный инструмент для суммаризации учебных материалов на нескольких языках ✨**
</div>

## 📋 Содержание

- [🌟 Особенности](#-особенности)
- [🛠 Технологический стек](#-технологический-стек)
- [🚀 Быстрый старт](#-быстрый-старт)
  - [Для macOS](#для-macos)
  - [Для Windows](#для-windows)
- [📦 Установка](#-установка)
- [💻 Использование](#-использование)
- [📖 Документация](#-документация)
- [🧪 Тестирование](#-тестирование)
- [🔧 CI/CD Pipeline](#-cicd-pipeline)
- [📁 Структура проекта](#-структура-проекта)
- [🤝 Вклад в проект](#-вклад-в-проект)
- [📄 Лицензия](#-лицензия)
- [👥 Авторы](#-авторы)

## 🌟 Особенности

**Multilingual Summarizer** — это мощный инструмент для суммаризации учебных материалов, который поддерживает:

- **🔤 Поддержка 3 языков:** Английский (en), Русский (ru), Немецкий (de)
- **🤖 Автоматическое определение языка** с fallback-механизмом
- **📊 Настраиваемый уровень сжатия:** 20%, 30%, 50%
- **🌐 Веб-интерфейс** с современным дизайном
- **📈 Детальная статистика** по суммаризации
- **🔒 Решение проблем SSL на Mac**
- **✅ Полная автоматизация CI/CD**

## 🛠 Технологический стек

| Технология         | Назначение                    | Версия |
| ------------------ | ----------------------------- | ------ |
| **Python**         | Основной язык                 | 3.8+   |
| **Flask**          | Веб-фреймворк                 | 2.3.3  |
| **NLTK**           | Обработка естественного языка | 3.8.1  |
| **LangDetect**     | Определение языка             | 1.0.9  |
| **Pytest**         | Тестирование                  | 7.4.0  |
| **Flake8**         | Линтинг кода                  | 6.0.0  |
| **Black**          | Форматирование кода           | 23.9.1 |
| **Gunicorn**       | Продакшн-сервер               | 20.1.0 |
| **GitHub Actions** | CI/CD                         | -      |

## 🚀 Быстрый старт

### Для macOS

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/yourusername/Multilingual-Summarizer.git
cd Multilingual-Summarizer

# 2. Создайте виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Установите NLTK данные (обход SSL проблем на Mac)
python src/install_nltk.py

# 5. Запустите приложение
python src/app.py
```

### Для Windows

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/yourusername/Multilingual-Summarizer.git
cd Multilingual-Summarizer

# 2. Создайте виртуальное окружение
python -m venv venv
venv\Scripts\activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Запустите установку NLTK
python src/app.py
# Приложение автоматически скачает необходимые данные
```

## 📦 Установка

### Вариант 1: Установка из PyPI (в разработке)

```bash
pip install multilingual-summarizer
```

### Вариант 2: Установка для разработки

```bash
# Клонируйте и установите в режиме разработки
git clone https://github.com/yourusername/Multilingual-Summarizer.git
cd Multilingual-Summarizer
pip install -e .
```

### Вариант 3: Установка с Docker

```dockerfile
# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "src/app.py"]
```

Запуск:
```bash
docker build -t multilingual-summarizer .
docker run -p 5000:5000 multilingual-summarizer
```

## 💻 Использование

### Веб-интерфейс

1. Запустите приложение:
   ```bash
   python src/app.py
   ```
   
2. Откройте браузер и перейдите по адресу:
   ```
   http://localhost:5000
   ```

3. Используйте интерфейс:
   - Введите текст в поле ввода
   - Выберите язык или оставьте "Auto-detect"
   - Выберите уровень сжатия
   - Нажмите "Generate Summary"

### API Endpoints

#### POST `/summarize`
Суммаризация текста через API:

```python
import requests
import json

url = "http://localhost:5000/summarize"
data = {
    "text": "Your text to summarize here...",
    "language": "auto",  # "en", "ru", "de", or "auto"
    "compression": 30    # 20, 30, or 50
}

response = requests.post(url, json=data)
result = response.json()

print(f"Summary: {result['summary']}")
print(f"Language: {result['language_name']}")
print(f"Reduction: {result['reduction']}%")
```

#### GET `/health`
Проверка состояния сервера:

```bash
curl http://localhost:5000/health
```

### Примеры использования

```python
# Пример 1: Суммаризация на английском
from summarizer import TextSummarizer

summarizer = TextSummarizer()
text = """
Artificial intelligence is transforming education in remarkable ways. 
AI-powered tools can personalize learning experiences for each student.
They analyze learning patterns and adapt content accordingly.
This technology helps identify knowledge gaps and provides targeted support.
"""

summary = summarizer.summarize_extractive(text, "en", 30)
print(f"Summary: {summary}")

# Пример 2: Определение языка
from language_detector import LanguageDetector

detector = LanguageDetector()
result = detector.detect_language("Это пример текста на русском языке")
print(f"Detected: {result['language']} with {result['confidence']*100}% confidence")
```

## 📖 Документация

### Архитектура приложения

```
Multilingual Summarizer
├── 📁 src/                    # Исходный код
│   ├── app.py                # Основное Flask приложение
│   ├── summarizer.py         # Логика суммаризации
│   ├── language_detector.py  # Определение языка
│   ├── utils.py              # Вспомогательные функции
│   └── __init__.py          # Пакет Python
├── 📁 tests/                 # Тесты
├── 📁 templates/             # HTML шаблоны
├── 📁 static/               # Статические файлы
└── 📁 docs/                 # Документация
```

### Алгоритм суммаризации

1. **Токенизация текста** с учетом языка
2. **Извлечение предложений** с фильтрацией коротких
3. **Выбор ключевых предложений** по стратегии:
   - Первое предложение (основная идея)
   - Последнее предложение (выводы)
   - Средние по длине предложения (детали)
4. **Сборка результата** с учетом уровня сжатия

### Поддерживаемые языки

| Язык    | Код  | Особенности токенизации |
| ------- | ---- | ----------------------- |
| English | `en` | Стандартный punkt       |
| Русский | `ru` | Русский punkt           |
| Deutsch | `de` | Немецкий punkt          |

## 🧪 Тестирование

### Запуск тестов

```bash
# Все тесты
pytest

# С покрытием кода
pytest --cov=src

# Конкретный тестовый файл
pytest tests/test_app.py -v

# Тесты с HTML отчетом
pytest --cov=src --cov-report=html
```

### Покрытие кода

```bash
# Генерация отчета о покрытии
pytest --cov=src --cov-report=term-missing

# Отчет в HTML формате
pytest --cov=src --cov-report=html
open htmlcov/index.html  # macOS
start htmlcov/index.html # Windows
```

### Линтинг и проверка качества

```bash
# Проверка стиля кода (PEP8)
flake8 src/

# Проверка докстрингов
pydocstyle src/

# Форматирование кода
black src/

# Проверка типов (если используете mypy)
mypy src/
```

## 🔧 CI/CD Pipeline

### Основной Workflow (`.github/workflows/ci-cd.yml`)

```yaml
name: CI/CD Pipeline
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Lint with flake8
        run: |
          flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
          flake8 src/ --count --exit-zero --max-complexity=10 --statistics
      
      - name: Check PEP8 compliance
        run: |
          pycodestyle src/ --max-line-length=100
      
      - name: Test with pytest
        run: |
          pytest tests/ -v --cov=src --cov-report=xml
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
```

### Продвинутый Workflow: Auto-Deploy to Render

```yaml
name: Auto-Deploy to Render
on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Deploy to Render
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
      
      - name: Run Post-Deployment Tests
        run: |
          sleep 30  # Wait for deployment
          curl -f ${{ secrets.PRODUCTION_URL }}/health || exit 1
          echo "✅ Deployment successful!"
      
      - name: Send Discord Notification
        uses: appleboy/discord-action@master
        with:
          webhook_id: ${{ secrets.DISCORD_WEBHOOK_ID }}
          webhook_token: ${{ secrets.DISCORD_WEBHOOK_TOKEN }}
          args: "🚀 New deployment completed! Application is live at ${{ secrets.PRODUCTION_URL }}"
```

### Дополнительные CI/CD техники

1. **Security Scanning** (включено в продвинутый workflow):
   ```yaml
   - name: Security scan with Bandit
     run: |
       pip install bandit
       bandit -r src/ -f json -o bandit-report.json
   ```

2. **Dependency Updates**:
   ```yaml
   - name: Check for outdated dependencies
     run: |
       pip install pip-check
       pip-check -u
   ```

3. **Performance Testing**:
   ```yaml
   - name: Performance test
     run: |
       pip install locust
       locust --headless -u 100 -r 10 -t 1m --host=http://localhost:5000
   ```

### Практическая ценность CI/CD

✅ **Автоматическая проверка качества** при каждом пуше<br>
✅ **Непрерывное развертывание** на продакшн<br>
✅ **Уведомления в Discord/Telegram** о статусе<br>
✅ **Security scanning** для выявления уязвимостей<br>
✅ **Performance testing** для проверки производительности<br>
✅ **Dependency updates** для актуальности зависимостей

## 📁 Структура проекта

```
multilingual-summarizer/
├── 📁 .github/workflows/         # CI/CD конфигурации
│   ├── ci-cd.yml                # Основной workflow
│   └── auto-deploy.yml          # Продвинутый workflow
├── 📁 src/                      # Исходный код
│   ├── __init__.py             # Пакет Python
│   ├── app.py                  # Основное Flask приложение
│   ├── summarizer.py           # Логика суммаризации
│   ├── language_detector.py    # Определение языка
│   ├── utils.py                # Вспомогательные функции
│   └── install_nltk.py         # Скрипт установки NLTK
├── 📁 tests/                    # Тесты
│   ├── __init__.py
│   ├── test_app.py
│   ├── test_summarizer.py
│   ├── test_language_detector.py
│   └── test_utils.py
├── 📁 templates/                # HTML шаблоны
│   └── index.html
├── 📁 static/                   # Статические файлы
├── 📁 docs/                     # Документация
├── 📁 scripts/                  # Вспомогательные скрипты
├── .gitignore                   # Git игнорируемые файлы
├── pytest.ini                   # Конфигурация pytest
├── requirements.txt             # Зависимости Python
├── setup.py                     # Конфигурация пакета
├── README.md                    # Этот файл
└── LICENSE                      # Лицензия MIT
```

## 🤝 Вклад в проект

Мы приветствуем вклады! Пожалуйста, следуйте этим шагам:

1. **Форкните репозиторий**
2. **Создайте feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Внесите изменения** и добавьте тесты
4. **Запустите тесты:**
   ```bash
   pytest tests/ -v
   flake8 src/
   ```
5. **Зафиксируйте изменения:**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Отправьте изменения:**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Откройте Pull Request**

### Руководство по стилю кода

- Следуйте **PEP 8** для Python кода
- Используйте **типизацию** для всех функций
- Добавляйте **докстринги** для всех публичных методов
- Пишите **тесты** для новой функциональности
- Используйте **осмысленные имена переменных**

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

```
MIT License

Copyright (c) 2024 Multilingual Summarizer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👥 Авторы

- **Ваше Имя** – *Разработчик* – [yourusername](https://github.com/yourusername)
- **Иван Иванов** – *Консультант по NLP* – [ivanov](https://github.com/ivanov)

### Благодарности

- [NLTK Project](https://www.nltk.org/) за инструменты обработки естественного языка
- [Flask Team](https://flask.palletsprojects.com/) за отличный веб-фреймворк
- [LangDetect](https://github.com/Mimino666/langdetect) за определение языка

---

<div align="center">

### ⭐ Если этот проект был полезен, поставьте звезду на GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/Multilingual-Summarizer&type=Date)](https://star-history.com/#yourusername/Multilingual-Summarizer&Date)

</div>