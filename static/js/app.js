// Translations for different languages
const translations = {
    en: {
        // Header
        appTitle: "Multilingual Summarizer",
        appSubtitle: "AI-powered text summarization in English, Russian, and German",
        
        // Input section
        inputTitle: "Input Text",
        textPlaceholder: "Enter or paste your text here (minimum 50 characters)...",
        languageLabel: "Language",
        autoOption: "Auto-detect",
        compressionLabel: "Compression Level",
        compress20: "20% (Most detailed)",
        compress30: "30% (Standard)",
        compress50: "50% (Most concise)",
        summarizeBtn: "Generate Summary",
        clearBtn: "Clear",
        
        // Supported languages display
        supportedLangs: "Supported Languages",
        langEnglish: "English",
        langRussian: "Russian",
        langGerman: "German",
        
        // Output section
        outputTitle: "Summary Result",
        placeholderTitle: "Your summary will appear here",
        placeholderText: "Enter text and click \"Generate Summary\" to see the result",
        copyBtn: "Copy Summary",
        generatedSummary: "Generated Summary",
        
        // Stats
        originalWords: "Original Words",
        summaryWords: "Summary Words",
        reduction: "Reduction",
        compression: "Compression",
        
        // Footer
        footerText: "© 2024 Multilingual Summarizer | Powered by Flask & NLTK",
        footerSubtext: "Supports texts up to 10,000 characters",
        
        // Errors and messages
        minCharsError: "Please enter at least 50 characters of text.",
        serverError: "Cannot connect to server. Please make sure Flask server is running.",
        languageMismatchTitle: "Language Mismatch Detected",
        languageMismatchText: "Text appears to be in {{detectedLang}}. Switch to {{detectedLang}} interface or use {{currentLang}} text.",
        switchLanguage: "Switch to {{lang}}",
        keepCurrent: "Keep current",
        processing: "Processing your text...",
        processingSubtext: "Analyzing content and generating summary",
        copySuccess: "Summary copied to clipboard!",
        unknownError: "An unknown error occurred",
        
        // Language names for display
        langNameEn: "English",
        langNameRu: "Russian",
        langNameDe: "German"
    },
    
    ru: {
        // Header
        appTitle: "Многоязычный Суммаризатор",
        appSubtitle: "AI-суммаризация текстов на английском, русском и немецком",
        
        // Input section
        inputTitle: "Входной текст",
        textPlaceholder: "Введите или вставьте текст (минимум 50 символов)...",
        languageLabel: "Язык",
        autoOption: "Автоопределение",
        compressionLabel: "Уровень сжатия",
        compress20: "20% (Подробно)",
        compress30: "30% (Стандарт)",
        compress50: "50% (Кратко)",
        summarizeBtn: "Суммаризировать",
        clearBtn: "Очистить",
        
        // Supported languages display
        supportedLangs: "Поддерживаемые языки",
        langEnglish: "Английский",
        langRussian: "Русский",
        langGerman: "Немецкий",
        
        // Output section
        outputTitle: "Результат суммаризации",
        placeholderTitle: "Здесь появится ваша суммаризация",
        placeholderText: "Введите текст и нажмите \"Суммаризировать\"",
        copyBtn: "Копировать суммаризацию",
        generatedSummary: "Сгенерированная суммаризация",
        
        // Stats
        originalWords: "Слов в оригинале",
        summaryWords: "Слов в суммаризации",
        reduction: "Сокращение",
        compression: "Сжатие",
        
        // Footer
        footerText: "© 2024 Многоязычный Суммаризатор | На основе Flask & NLTK",
        footerSubtext: "Поддерживает тексты до 10 000 символов",
        
        // Errors and messages
        minCharsError: "Пожалуйста, введите минимум 50 символов текста.",
        serverError: "Не удается подключиться к серверу. Убедитесь, что Flask сервер запущен.",
        languageMismatchTitle: "Обнаружено несоответствие языка",
        languageMismatchText: "Текст, похоже, на языке {{detectedLang}}. Переключитесь на интерфейс {{detectedLang}} или используйте текст на {{currentLang}}.",
        switchLanguage: "Переключить на {{lang}}",
        keepCurrent: "Оставить текущий",
        processing: "Обработка вашего текста...",
        processingSubtext: "Анализируем контент и генерируем суммаризацию",
        copySuccess: "Суммаризация скопирована в буфер обмена!",
        unknownError: "Произошла неизвестная ошибка",
        
        // Language names for display
        langNameEn: "Английский",
        langNameRu: "Русский",
        langNameDe: "Немецкий"
    },
    
    de: {
        // Header
        appTitle: "Mehrsprachiger Textzusammenfasser",
        appSubtitle: "KI-gestützte Textzusammenfassung auf Englisch, Russisch und Deutsch",
        
        // Input section
        inputTitle: "Eingabetext",
        textPlaceholder: "Geben Sie Ihren Text hier ein (mindestens 50 Zeichen)...",
        languageLabel: "Sprache",
        autoOption: "Auto-Erkennung",
        compressionLabel: "Komprimierungsgrad",
        compress20: "20% (Am detailliertesten)",
        compress30: "30% (Standard)",
        compress50: "50% (Am prägnantesten)",
        summarizeBtn: "Zusammenfassung generieren",
        clearBtn: "Löschen",
        
        // Supported languages display
        supportedLangs: "Unterstützte Sprachen",
        langEnglish: "Englisch",
        langRussian: "Russisch",
        langGerman: "Deutsch",
        
        // Output section
        outputTitle: "Zusammenfassungsergebnis",
        placeholderTitle: "Ihre Zusammenfassung wird hier erscheinen",
        placeholderText: "Geben Sie Text ein und klicken Sie auf \"Zusammenfassung generieren\"",
        copyBtn: "Zusammenfassung kopieren",
        generatedSummary: "Generierte Zusammenfassung",
        
        // Stats
        originalWords: "Ursprüngliche Wörter",
        summaryWords: "Zusammenfassung Wörter",
        reduction: "Reduzierung",
        compression: "Komprimierung",
        
        // Footer
        footerText: "© 2024 Mehrsprachiger Textzusammenfasser | Powered by Flask & NLTK",
        footerSubtext: "Unterstützt Texte bis zu 10.000 Zeichen",
        
        // Errors and messages
        minCharsError: "Bitte geben Sie mindestens 50 Zeichen Text ein.",
        serverError: "Verbindung zum Server fehlgeschlagen. Stellen Sie sicher, dass der Flask-Server läuft.",
        languageMismatchTitle: "Sprachenkonflikt erkannt",
        languageMismatchText: "Text scheint in {{detectedLang}} zu sein. Wechseln Sie zur {{detectedLang}}-Schnittstelle oder verwenden Sie {{currentLang}}-Text.",
        switchLanguage: "Wechseln zu {{lang}}",
        keepCurrent: "Aktuelle behalten",
        processing: "Verarbeite Ihren Text...",
        processingSubtext: "Analysiere Inhalt und generiere Zusammenfassung",
        copySuccess: "Zusammenfassung in die Zwischenablage kopiert!",
        unknownError: "Ein unbekannter Fehler ist aufgetreten",
        
        // Language names for display
        langNameEn: "Englisch",
        langNameRu: "Russisch",
        langNameDe: "Deutsch"
    }
};

// Current interface language
let currentLang = 'en';
// Store for text content when switching languages
let textContent = {
    en: "Artificial intelligence is transforming many industries around the world. Machine learning algorithms can analyze vast amounts of data and identify patterns that humans might miss. Natural language processing helps computers understand, interpret, and generate human language in a valuable way. These technologies are becoming increasingly important in business, research, and daily life. As AI continues to evolve, it will likely create new opportunities and challenges for society.",
    ru: "",
    de: ""
};

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    // Load saved language preference or default to English
    const savedLang = localStorage.getItem('summarizerLang') || 'en';
    changeLanguage(savedLang);
    
    // Initialize textarea content
    updateTextareaContent();
    
    // Check server connection
    checkServer();
    
    // Add event listeners
    const textInput = document.getElementById('textInput');
    textInput.addEventListener('input', function() {
        // Store current text content
        textContent[currentLang] = this.value;
    });
    
    textInput.addEventListener('click', function() {
        if (this.value === this.defaultValue) {
            this.select();
        }
    });
});

// Change interface language
async function changeLanguage(lang) {
    if (currentLang === lang) return;
    
    // Save text content from current language
    textContent[currentLang] = document.getElementById('textInput').value;
    
    // Update current language
    currentLang = lang;
    
    // Update active button
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('data-lang') === lang) {
            btn.classList.add('active');
        }
    });
    
    // Update all text elements
    updateTextElements();
    
    // Update textarea content
    updateTextareaContent();
    
    // Reset result display
    clearResult();
    
    // Save preference to localStorage
    localStorage.setItem('summarizerLang', lang);
}

// Update all text elements with translations
function updateTextElements() {
    const t = translations[currentLang];
    
    // Header
    document.getElementById('app-title').textContent = t.appTitle;
    document.getElementById('app-subtitle').textContent = t.appSubtitle;
    
    // Input section
    document.getElementById('input-title').textContent = t.inputTitle;
    document.getElementById('textInput').placeholder = t.textPlaceholder;
    document.getElementById('language-label').textContent = t.languageLabel;
    document.getElementById('auto-option').textContent = t.autoOption;
    document.getElementById('compression-label').textContent = t.compressionLabel;
    document.getElementById('supported-langs-label').textContent = t.supportedLangs;
    
    // Compression options
    const compressionSelect = document.getElementById('compression');
    compressionSelect.options[0].text = t.compress20;
    compressionSelect.options[1].text = t.compress30;
    compressionSelect.options[2].text = t.compress50;
    
    // Buttons
    document.getElementById('summarize-btn').querySelector('span').textContent = t.summarizeBtn;
    document.getElementById('clear-btn').querySelector('span').textContent = t.clearBtn;
    
    // Language tags
    document.getElementById('lang-english').textContent = t.langEnglish;
    document.getElementById('lang-russian').textContent = t.langRussian;
    document.getElementById('lang-german').textContent = t.langGerman;
    
    // Output section
    document.getElementById('output-title').textContent = t.outputTitle;
    document.getElementById('placeholder-title').textContent = t.placeholderTitle;
    document.getElementById('placeholder-text').textContent = t.placeholderText;
    
    // Footer
    document.getElementById('footer-text').textContent = t.footerText;
    document.getElementById('footer-subtext').textContent = t.footerSubtext;
}

// Update textarea content based on current language
function updateTextareaContent() {
    const textarea = document.getElementById('textInput');
    textarea.value = textContent[currentLang] || '';
}

// Check if server is reachable
async function checkServer() {
    try {
        const response = await fetch('/health');
        if (!response.ok) {
            console.warn('Server health check failed');
            return false;
        }
        return true;
    } catch (error) {
        console.warn('Server connection error:', error);
        return false;
    }
}

// Main summarize function
async function summarize() {
    const text = document.getElementById('textInput').value.trim();
    const compression = parseInt(document.getElementById('compression').value);
    const language = document.getElementById('language').value;
    
    // Store current text
    textContent[currentLang] = text;
    
    // Validation
    if (text.length < 50) {
        showError(translations[currentLang].minCharsError);
        return;
    }
    
    // Show loading state
    showLoading();
    
    try {
        const response = await fetch('/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                text: text,
                compression: compression,
                language: language
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || translations[currentLang].unknownError);
        }
        
        if (data.success) {
            showResult(data);
        } else {
            showError(data.error || translations[currentLang].unknownError);
        }
        
    } catch (error) {
        console.error('Summarization error:', error);
        showError(`${error.message}`);
    }
}

// Show loading indicator
function showLoading() {
    const t = translations[currentLang];
    const container = document.getElementById('resultContainer');
    container.innerHTML = `
        <div class="loading">
            <div class="loading-spinner"></div>
            <h3>${t.processing}</h3>
            <p>${t.processingSubtext}</p>
        </div>
    `;
}

// Show results
function showResult(data) {
    const container = document.getElementById('resultContainer');
    const t = translations[currentLang];
    
    // Format reduction with arrow
    const reductionArrow = data.reduction > 0 ? '↓' : '↑';
    const reductionColor = data.reduction > 0 ? '#10b981' : '#ef4444';
    
    // Get language name from translation
    const langNameKey = `langName${data.language.toUpperCase()}`;
    const detectedLangName = t[langNameKey] || data.language_name;
    
    container.innerHTML = `
        <div class="result-container">
            <div class="result-header">
                <h3>${t.generatedSummary}</h3>
                <div class="language-badge">
                    ${detectedLangName} (${Math.round(data.confidence * 100)}%)
                </div>
            </div>
            
            <div class="summary-text">
                ${data.summary}
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value">${data.original_length}</div>
                    <div class="stat-label">${t.originalWords}</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-value">${data.summary_length}</div>
                    <div class="stat-label">${t.summaryWords}</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-value" style="color: ${reductionColor}">
                        ${reductionArrow} ${data.reduction}%
                    </div>
                    <div class="stat-label">${t.reduction}</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-value">${data.compression}%</div>
                    <div class="stat-label">${t.compression}</div>
                </div>
            </div>
            
            <div style="margin-top: 20px; text-align: center;">
                <button class="btn btn-secondary" onclick="copySummary()">
                    <span>${t.copyBtn}</span>
                </button>
            </div>
        </div>
    `;
}

// Show error message
function showError(message) {
    const container = document.getElementById('resultContainer');
    container.innerHTML = `
        <div class="error">
            <h3>Error</h3>
            <p>${message}</p>
            <p class="error-details">
                Please check if the server is running and try again.
            </p>
        </div>
    `;
}

// Clear text area
function clearText() {
    textContent[currentLang] = '';
    document.getElementById('textInput').value = '';
    clearResult();
}

// Clear result display
function clearResult() {
    const t = translations[currentLang];
    document.getElementById('resultContainer').innerHTML = `
        <div class="placeholder">
            <div class="placeholder-icon">📄</div>
            <h3>${t.placeholderTitle}</h3>
            <p>${t.placeholderText}</p>
        </div>
    `;
}

// Copy summary to clipboard
function copySummary() {
    const t = translations[currentLang];
    const summaryText = document.querySelector('.summary-text')?.innerText;
    if (summaryText) {
        navigator.clipboard.writeText(summaryText).then(() => {
            alert(t.copySuccess);
        }).catch(err => {
            console.error('Failed to copy:', err);
        });
    }
}