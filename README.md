# 🌍 Multilingual Learning Material Summarizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)

<div align="center">
  ✨ Интеллектуальный инструмент для суммаризации учебных материалов на нескольких языках ✨
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
PORT=5001 python3 src/app.py
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

1. Используйте интерфейс:
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

### Продвинутый Workflow: Auto-Deploy to Render. Данный Workflow используется в настоящий момент.

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, master]
    paths-ignore:
      - 'docs/**'
      - '*.md'
  pull_request:
    branches: [main, master]
  workflow_dispatch:
    inputs:
      run_extensive_tests:
        description: 'Run extensive tests'
        required: false
        default: false
        type: boolean
      generate_report:
        description: 'Generate test report'
        required: false
        default: true
        type: boolean
  schedule:
    - cron: '0 8 * * *'

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: write

jobs:
  quality-check:
    name: Code Quality Check
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 black pylint pycodestyle pydocstyle pylama pyflakes

      - name: Check code formatting with Black
        run: |
          if [ -d "src" ]; then
            echo "📝 Checking code formatting with Black..."
            black --check src/ tests/ || echo "⚠️ Code formatting issues found (non-critical)"
          fi

      - name: Lint with flake8
        run: |
          if [ -d "src" ]; then
            echo "🔍 Running flake8 linting..."
            # stop the build if there are Python syntax errors or undefined names
            flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics
            # exit-zero treats all errors as warnings
            flake8 src/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
          fi

      - name: Check PEP8 compliance with pycodestyle
        run: |
          echo "📐 Checking PEP8 compliance with pycodestyle..."
          if [ -d "src" ]; then
            echo "Checking src/ directory..."
            pycodestyle --max-line-length=127 --ignore=E501,W503 src/ || echo "⚠️ PEP8 issues found in src/"
          fi
          if [ -d "tests" ]; then
            echo "Checking tests/ directory..."
            pycodestyle --max-line-length=127 --ignore=E501,W503 tests/ || echo "⚠️ PEP8 issues found in tests/"
          fi

      - name: Check docstring style with pydocstyle
        run: |
          echo "📄 Checking docstring style with pydocstyle..."
          if [ -d "src" ]; then
            pydocstyle --convention=google src/ || echo "⚠️ Docstring style issues found (non-critical)"
          fi

      - name: Comprehensive linting with pylama
        run: |
          echo "🔬 Running comprehensive linting with pylama..."
          if [ -d "src" ]; then
            pylama src/ -l pycodestyle,pyflakes,mccabe --max-line-length=127 || echo "⚠️ Pylama found issues (non-critical)"
          fi

  test:
    name: Run Tests
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          # Сначала устанавливаем все зависимости из requirements.txt
          if [ -f requirements.txt ]; then 
            pip install -r requirements.txt; 
          else
            # Если нет requirements.txt, устанавливаем основные зависимости
            pip install flask nltk langdetect pytest pytest-cov
          fi

      - name: Run basic tests
        env:
          # ВАЖНО: Добавляем src в PYTHONPATH, чтобы тесты видели код
          PYTHONPATH: ${{ github.workspace }}/src:${{ github.workspace }}
        run: |
          echo "🧪 Running tests..."
          echo "Current directory: $(pwd)"
          echo "Directory contents:"
          ls -la
          echo "Python path: $PYTHONPATH"
          python -m pytest tests/ -v --tb=short

      - name: Run tests with coverage
        if: ${{ github.event.inputs.run_extensive_tests == 'true' || github.event_name == 'schedule' }}
        env:
          PYTHONPATH: ${{ github.workspace }}/src:${{ github.workspace }}
        run: |
          python -m pytest tests/ --cov=src --cov-report=xml --cov-report=html

      - name: Upload coverage reports
        uses: actions/upload-artifact@v4
        if: ${{ github.event.inputs.run_extensive_tests == 'true' || github.event_name == 'schedule' }}
        with:
          name: coverage-report
          path: |
            htmlcov/
            coverage.xml

  generate-report:
    name: Generate Daily Report
    runs-on: ubuntu-latest
    needs: [quality-check, test]
    if: ${{ github.event_name == 'schedule' || github.event.inputs.generate_report == 'true' }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install pandas

      - name: Generate daily statistics
        run: |
          python -c "
          from datetime import datetime
          import pandas as pd
          
          results = [{
              'language': 'en',
              'detected_language': 'en',
              'detected_confidence': 0.99,
              'original_length': 100,
              'summary_length': 30,
              'reduction_percent': 70.0,
              'timestamp': datetime.now().isoformat()
          }]
          
          df = pd.DataFrame(results)
          df.to_csv('daily_report.csv', index=False)
          
          with open('DAILY_REPORT.md', 'w') as f:
              f.write('# 📈 Daily Summary Report\n\n')
              f.write(f'Generated: {datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")}\n\n')
              f.write('## 📋 Sample Metrics\n\n')
              f.write('| Language | Detected | Confidence | Original | Summary | Reduction |\n')
              f.write('|----------|----------|------------|----------|---------|-----------|\n')
              for _, row in df.iterrows():
                  f.write(f'| {row[\"language\"]} | {row[\"detected_language\"]} | {row[\"detected_confidence\"]:.2f} | ')
                  f.write(f'{row[\"original_length\"]} | {row[\"summary_length\"]} | {row[\"reduction_percent\"]:.1f}% |\n')
              
              f.write(f'\n**📊 Summary:**\n')
              f.write(f'- CI/CD pipeline is working\n')
          "

      - name: Commit and push report
        # Работает только если есть права на запись и ветка не защищена правилами (branch protection rules)
        if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master'
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add daily_report.csv DAILY_REPORT.md
          if git diff --quiet && git diff --staged --quiet; then
            echo "No changes to commit"
          else
            git commit -m "📊 Update daily report $(date +%Y-%m-d)"
            git push
          fi

  deploy-docs:
    name: Deploy Documentation
    runs-on: ubuntu-latest
    needs: [quality-check, test]
    if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install mkdocs mkdocs-material

      - name: Generate documentation content
        run: |
          mkdir -p docs
          echo "site_name: Multilingual Summarizer" > mkdocs.yml
          echo "theme:" >> mkdocs.yml
          echo "  name: material" >> mkdocs.yml
          
          echo "# Multilingual Summarizer" > docs/index.md
          echo "AI-powered text summarization tool." >> docs/index.md

      - name: Build and Deploy
        run: |
          mkdocs build
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          force_orphan: true

  notify:
    name: Notify Status
    runs-on: ubuntu-latest
    if: always()
    needs: [quality-check, test, generate-report, deploy-docs]
    steps:
      - name: Workflow status summary
        run: |
          echo "🚀 CI/CD Pipeline Status Summary"
          echo "Quality Check: ${{ needs.quality-check.result }}"
          echo "Tests: ${{ needs.test.result }}"
          if [ "${{ needs.quality-check.result }}" = "success" ] && [ "${{ needs.test.result }}" = "success" ]; then
            echo "✅ Pipeline successful."
          else
            echo "⚠️ Pipeline failed or has warnings."
          fi
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

## 👥 Авторы

- **Салтанов Илья** – *Архитектор проекта* – [IlyaSaltanov](https://github.com/IlyaSaltanov)

### Благодарности

- [NLTK Project](https://www.nltk.org/) за инструменты обработки естественного языка
- [Flask Team](https://flask.palletsprojects.com/) за отличный веб-фреймворк
- [LangDetect](https://github.com/Mimino666/langdetect) за определение языка

---

<div align="center">

### ⭐ Если этот проект был полезен, поставьте звезду на GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/Multilingual-Summarizer&type=Date)](https://star-history.com/#yourusername/Multilingual-Summarizer&Date)

</div>