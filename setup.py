"""
Setup configuration for Multilingual Learning Material Summarizer
"""

from setuptools import setup, find_packages
import os

# Читаем README файл
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Читаем requirements.txt
def read_requirements():
    """Read requirements from requirements.txt file."""
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(requirements_path):
        with open(requirements_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    # Основная информация о проекте
    name="multilingual-summarizer",
    version="0.1.0",
    author="Your Name or Organization",
    author_email="your.email@example.com",
    description="A multilingual text summarization tool for learning materials",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # Ссылки на проект
    url="https://github.com/yourusername/Multilingual-Learning-Material-Summarizer",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/Multilingual-Learning-Material-Summarizer/issues",
        "Source Code": "https://github.com/yourusername/Multilingual-Learning-Material-Summarizer",
    },
    
    # Классификаторы (для PyPI)
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: Flask",
    ],
    
    # Ключевые слова для поиска
    keywords="summarization, multilingual, education, nlp, text-processing",
    
    # Пакеты для включения
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # Включаем не-Python файлы
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.ini"],
    },
    
    # Зависимости
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.3.0",
        "nltk>=3.8.0",
        "langdetect>=1.0.9",
    ],
    
    # Опциональные зависимости для разработки
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "flake8>=6.0.0",
            "black>=23.9.1",
            "pylint>=2.17.4",
        ],
        "test": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
        "full": [
            "pandas>=1.5.3",
            "matplotlib>=3.7.2",
            "numpy>=1.24.3",
            "gunicorn>=20.1.0",
            "python-dotenv>=1.0.0",
        ],
    },
    
    # Точки входа (командная строка)
    entry_points={
        "console_scripts": [
            "summarizer=app:main",  # Если в app.py есть функция main()
        ],
    },
    
    # Скрипты
    scripts=[
        "scripts/run_summarizer.py",  # Если у вас есть скрипты
    ],
    
    # Лицензия
    license="MIT",
    
    # Прочая информация
    platforms=["any"],
    zip_safe=False,
)