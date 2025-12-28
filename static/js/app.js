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
        languageMismatchTitle: "⚠️ Language Conflict Detected",
        languageMismatchText: "Your text appears to be in {{detectedLang}}, but the interface is set to {{currentLang}}. Please change the interface language or enter text in {{currentLang}}.",
        switchLanguageBtn: "Switch to {{lang}}",
        cancelBtn: "Cancel",
        processing: "Processing your text...",
        processingSubtext: "Analyzing content and generating summary",
        copySuccess: "Summary copied to clipboard!",
        unknownError: "An unknown error occurred",
        
        // Language names for display
        langNameEn: "English",
        langNameRu: "Russian",
        langNameDe: "German",
        
        // Language codes mapping
        langCodeEn: "en",
        langCodeRu: "ru", 
        langCodeDe: "de"
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
        languageMismatchTitle: "⚠️ Обнаружен языковой конфликт",
        languageMismatchText: "Ваш текст, похоже, на языке {{detectedLang}}, но интерфейс настроен на {{currentLang}}. Пожалуйста, смените язык интерфейса или введите текст на {{currentLang}}.",
        switchLanguageBtn: "Переключить на {{lang}}",
        cancelBtn: "Отмена",
        processing: "Обработка вашего текста...",
        processingSubtext: "Анализируем контент и генерируем суммаризацию",
        copySuccess: "Суммаризация скопирована в буфер обмена!",
        unknownError: "Произошла неизвестная ошибка",
        
        // Language names for display
        langNameEn: "Английский",
        langNameRu: "Русский",
        langNameDe: "Немецкий",
        
        // Language codes mapping
        langCodeEn: "en",
        langCodeRu: "ru",
        langCodeDe: "de"
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
        languageMismatchTitle: "⚠️ Sprachenkonflikt erkannt",
        languageMismatchText: "Ihr Text scheint in {{detectedLang}} zu sein, aber die Schnittstelle ist auf {{currentLang}} eingestellt. Bitte ändern Sie die Schnittstellensprache oder geben Sie Text in {{currentLang}} ein.",
        switchLanguageBtn: "Wechseln zu {{lang}}",
        cancelBtn: "Abbrechen",
        processing: "Verarbeite Ihren Text...",
        processingSubtext: "Analysiere Inhalt und generiere Zusammenfassung",
        copySuccess: "Zusammenfassung in die Zwischenablage kopiert!",
        unknownError: "Ein unbekannter Fehler ist aufgetreten",
        
        // Language names for display
        langNameEn: "Englisch",
        langNameRu: "Russisch",
        langNameDe: "Deutsch",
        
        // Language codes mapping
        langCodeEn: "en",
        langCodeRu: "ru",
        langCodeDe: "de"
    }
};

// Current interface language
let currentLang = 'en';
// Store for text content when switching languages
let textContent = {
    en: "Artificial intelligence is transforming many industries around the world. Machine learning algorithms can analyze vast amounts of data and identify patterns that humans might miss. Natural language processing helps computers understand, interpret, and generate human language in a valuable way. These technologies are becoming increasingly important in business, research, and daily life. As AI continues to evolve, it will likely create new opportunities and challenges for society.",
    ru: "Искусственный интеллект меняет многие отрасли по всему миру. Алгоритмы машинного обучения могут анализировать огромные объемы данных и выявлять закономерности, которые люди могут упустить. Обработка естественного языка помогает компьютерам понимать, интерпретировать и генерировать человеческий язык полезным образом. Эти технологии становятся все более важными в бизнесе, исследованиях и повседневной жизни. По мере развития ИИ он, вероятно, создаст новые возможности и вызовы для общества.",
    de: "Künstliche Intelligenz verändert viele Branchen weltweit. Machine-Learning-Algorithmen können riesige Datenmengen analysieren und Muster erkennen, die Menschen übersehen könnten. Die Verarbeitung natürlicher Sprache hilft Computern, menschliche Sprache auf wertvolle Weise zu verstehen, zu interpretieren und zu generieren. Diese Technologien werden in Wirtschaft, Forschung und Alltag immer wichtiger. Da sich KI weiterentwickelt, wird sie voraussichtlich neue Möglichkeiten und Herausforderungen für die Gesellschaft schaffen."
};

// Simple language detection function
function detectTextLanguageSimple(text) {
    if (text.length < 20) return null;
    
    // Count Russian characters
    const ruChars = /[а-яА-ЯёЁ]/g;
    const ruCount = (text.match(ruChars) || []).length;
    
    // Count German characters
    const deChars = /[äöüÄÖÜß]/g;
    const deCount = (text.match(deChars) || []).length;
    
    // Count English words (approximation)
    const enWords = text.split(/\s+/).length;
    
    // If Russian characters are significant
    if (ruCount > 5 && ruCount > text.length * 0.05) {
        return 'ru';
    }
    
    // If German characters are present
    if (deCount > 2 && deCount > text.length * 0.02) {
        return 'de';
    }
    
    // Default to English for long enough texts
    if (enWords > 3) {
        return 'en';
    }
    
    return null;
}

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    // Load saved language preference or default to English
    const savedLang = localStorage.getItem('summarizerLang') || 'en';
    changeLanguage(savedLang);
    
    // Initialize textarea content
    updateTextareaContent();
    
    // Check server connection (silently)
    checkServer().catch(console.warn);
    
    // Add event listeners
    const textInput = document.getElementById('textInput');
    textInput.addEventListener('input', function() {
        // Store current text content
        textContent[currentLang] = this.value;
    });
});

// Change interface language
function changeLanguage(lang) {
    if (currentLang === lang) return;
    
    // Save text content from current language
    const textInput = document.getElementById('textInput');
    if (textInput) {
        textContent[currentLang] = textInput.value;
    }
    
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
    if (!t) return;
    
    console.log('Updating text elements for language:', currentLang);
    
    // Update all elements by ID
    const elementsToUpdate = {
        'app-title': t.appTitle,
        'app-subtitle': t.appSubtitle,
        'input-title': t.inputTitle,
        'language-label': t.languageLabel,
        'compression-label': t.compressionLabel,
        'supported-langs-label': t.supportedLangs,
        'output-title': t.outputTitle,
        'placeholder-title': t.placeholderTitle,
        'placeholder-text': t.placeholderText,
        'footer-text': t.footerText,
        'footer-subtext': t.footerSubtext,
        'lang-english': t.langEnglish,
        'lang-russian': t.langRussian,
        'lang-german': t.langGerman
    };
    
    // Update text content
    for (const [id, text] of Object.entries(elementsToUpdate)) {
        const element = document.getElementById(id);
        if (element) {
            element.textContent = text;
        }
    }
    
    // Update placeholder
    const textInput = document.getElementById('textInput');
    if (textInput) {
        textInput.placeholder = t.textPlaceholder;
    }
    
    // Update auto-option
    const autoOption = document.getElementById('auto-option');
    if (autoOption) {
        autoOption.textContent = t.autoOption;
    }
    
    // Update compression options
    const compressionSelect = document.getElementById('compression');
    if (compressionSelect && compressionSelect.options.length >= 3) {
        compressionSelect.options[0].text = t.compress20;
        compressionSelect.options[1].text = t.compress30;
        compressionSelect.options[2].text = t.compress50;
    }
    
    // Update button texts
    const summarizeBtn = document.getElementById('summarize-btn');
    if (summarizeBtn) {
        const span = summarizeBtn.querySelector('span');
        if (span) span.textContent = t.summarizeBtn;
    }
    
    const clearBtn = document.getElementById('clear-btn');
    if (clearBtn) {
        const span = clearBtn.querySelector('span');
        if (span) span.textContent = t.clearBtn;
    }
}

// Update textarea content based on current language
function updateTextareaContent() {
    const textarea = document.getElementById('textInput');
    if (textarea) {
        textarea.value = textContent[currentLang] || '';
    }
}

// Check if server is reachable
async function checkServer() {
    try {
        const response = await fetch('/health');
        return response.ok;
    } catch (error) {
        return false;
    }
}

// Main summarize function with language check
async function summarize() {
    const text = document.getElementById('textInput').value.trim();
    const compression = parseInt(document.getElementById('compression').value);
    const languageSelect = document.getElementById('language').value;
    
    // Store current text
    textContent[currentLang] = text;
    
    // Validation
    if (text.length < 50) {
        showError(translations[currentLang].minCharsError);
        return;
    }
    
    // Check for language mismatch
    const detectedLang = detectTextLanguageSimple(text);
    console.log('Detected language:', detectedLang, 'Interface language:', currentLang);
    
    if (detectedLang && detectedLang !== currentLang && languageSelect === 'auto') {
        // Show language mismatch warning
        showLanguageMismatchWarning(detectedLang);
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
                language: languageSelect
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

// Show language mismatch warning
function showLanguageMismatchWarning(detectedLang) {
    const t = translations[currentLang];
    const detectedLangName = translations[detectedLang]?.langNameEn || detectedLang;
    const currentLangName = t.langNameEn || currentLang;
    
    const container = document.getElementById('resultContainer');
    container.innerHTML = `
        <div class="warning">
            <h3>${t.languageMismatchTitle}</h3>
            <p>${t.languageMismatchText
                .replace('{{detectedLang}}', detectedLangName)
                .replace('{{currentLang}}', currentLangName)}</p>
            <div style="margin-top: 15px; display: flex; gap: 10px; flex-wrap: wrap;">
                <button class="btn btn-primary" onclick="forceSwitchLanguage('${detectedLang}')" style="padding: 8px 16px;">
                    ${t.switchLanguageBtn.replace('{{lang}}', detectedLangName)}
                </button>
                <button class="btn btn-secondary" onclick="clearWarning()" style="padding: 8px 16px;">
                    ${t.cancelBtn}
                </button>
            </div>
        </div>
    `;
}

// Force switch language and resubmit
function forceSwitchLanguage(lang) {
    changeLanguage(lang);
    // Auto-submit after language change
    setTimeout(() => summarize(), 100);
}

// Clear warning and show placeholder
function clearWarning() {
    clearResult();
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
    let detectedLangName = data.language_name;
    if (data.language === 'en') detectedLangName = t.langNameEn;
    if (data.language === 'ru') detectedLangName = t.langNameRu;
    if (data.language === 'de') detectedLangName = t.langNameDe;
    
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
    const textInput = document.getElementById('textInput');
    if (textInput) {
        textInput.value = '';
    }
    clearResult();
}

// Clear result display
function clearResult() {
    const t = translations[currentLang];
    const container = document.getElementById('resultContainer');
    if (container) {
        container.innerHTML = `
            <div class="placeholder">
                <div class="placeholder-icon">📄</div>
                <h3>${t.placeholderTitle}</h3>
                <p>${t.placeholderText}</p>
            </div>
        `;
    }
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

// Debug function to check translations
function debugTranslations() {
    console.log('Current language:', currentLang);
    console.log('Translations available:', Object.keys(translations));
    console.log('Elements found:');
    ['app-title', 'input-title', 'output-title'].forEach(id => {
        const el = document.getElementById(id);
        console.log(`${id}:`, el ? 'found' : 'NOT FOUND');
    });
}

// Add debug button for testing (remove in production)
document.addEventListener('DOMContentLoaded', function() {
    // Uncomment to debug
    // setTimeout(debugTranslations, 1000);
});