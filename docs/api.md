# 📡 API Documentation - Multilingual Summarizer

## 🚀 Overview

The Multilingual Summarizer provides a RESTful API for text summarization in multiple languages. This API supports English, Russian, and German with automatic language detection.

**Base URL:** `http://localhost:5000` (development) or `https://your-domain.com` (production)

## 📋 API Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Description:** Check if the API service is running and healthy.

**Request:**
```http
GET /health HTTP/1.1
Host: localhost:5000
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Multilingual Summarizer",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Status Codes:**
- `200 OK`: Service is healthy
- `500 Internal Server Error`: Service is not healthy

**Example using cURL:**
```bash
curl -X GET http://localhost:5000/health
```

### 2. Text Summarization

**Endpoint:** `POST /summarize`

**Description:** Summarize text in supported languages (English, Russian, German) with configurable compression levels.

**Request Headers:**
```http
Content-Type: application/json
Accept: application/json
```

**Request Body:**
```json
{
  "text": "Text to summarize here...",
  "language": "auto",
  "compression": 30
}
```

**Parameters:**

| Parameter     | Type    | Required | Default  | Description            | Valid Values                     |
| ------------- | ------- | -------- | -------- | ---------------------- | -------------------------------- |
| `text`        | string  | ✅        | -        | Text to summarize      | Min 50 characters                |
| `language`    | string  | ❌        | `"auto"` | Language of the text   | `"auto"`, `"en"`, `"ru"`, `"de"` |
| `compression` | integer | ❌        | `30`     | Compression percentage | `20`, `30`, `50`                 |

**Successful Response (200 OK):**
```json
{
  "success": true,
  "summary": "Summarized text goes here...",
  "language": "en",
  "language_name": "English",
  "confidence": 0.95,
  "compression": 30,
  "original_length": 250,
  "summary_length": 75,
  "reduction": 70.0
}
```

**Response Fields:**

| Field             | Type    | Description                                      |
| ----------------- | ------- | ------------------------------------------------ |
| `success`         | boolean | `true` if summarization was successful           |
| `summary`         | string  | The summarized text                              |
| `language`        | string  | Detected language code                           |
| `language_name`   | string  | Full name of the detected language               |
| `confidence`      | number  | Confidence level of language detection (0.0-1.0) |
| `compression`     | integer | Applied compression level                        |
| `original_length` | integer | Number of words in original text                 |
| `summary_length`  | integer | Number of words in summary                       |
| `reduction`       | float   | Percentage reduction (original → summary)        |

**Error Responses:**

1. **400 Bad Request** - Invalid input:
```json
{
  "error": "Text too short (min 50 characters)"
}
```

2. **400 Bad Request** - Missing required field:
```json
{
  "error": "No text provided"
}
```

3. **500 Internal Server Error** - Server error:
```json
{
  "error": "Internal server error: [error details]"
}
```

**Status Codes:**
- `200 OK`: Summarization successful
- `400 Bad Request`: Invalid input parameters
- `415 Unsupported Media Type`: Wrong content type
- `500 Internal Server Error`: Server error during processing

## 💡 Examples

### Example 1: Basic Summarization (Auto-detect Language)

**Request:**
```bash
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Artificial intelligence is transforming education in remarkable ways. AI-powered tools can personalize learning experiences for each student. They analyze learning patterns and adapt content accordingly. This technology helps identify knowledge gaps and provides targeted support. The future of education looks promising with AI integration.",
    "compression": 30
  }'
```

**Response:**
```json
{
  "success": true,
  "summary": "Artificial intelligence is transforming education in remarkable ways. The future of education looks promising with AI integration.",
  "language": "en",
  "language_name": "English",
  "confidence": 0.98,
  "compression": 30,
  "original_length": 65,
  "summary_length": 20,
  "reduction": 69.2
}
```

### Example 2: Russian Text with Specific Language

**Request:**
```bash
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Искусственный интеллект революционизирует образование. Системы на основе ИИ могут персонализировать обучение для каждого студента. Они анализируют паттерны обучения и адаптируют контент соответствующим образом. Эта технология помогает выявлять пробелы в знаниях и предоставляет целевую поддержку. Будущее образования выглядит многообещающим с интеграцией ИИ.",
    "language": "ru",
    "compression": 50
  }'
```

**Response:**
```json
{
  "success": true,
  "summary": "Искусственный интеллект революционизирует образование. Будущее образования выглядит многообещающим с интеграцией ИИ.",
  "language": "ru",
  "language_name": "Russian",
  "confidence": 1.0,
  "compression": 50,
  "original_length": 55,
  "summary_length": 11,
  "reduction": 80.0
}
```

### Example 3: German Text with Maximum Compression

**Request:**
```bash
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Künstliche Intelligenz revolutioniert die Bildung. KI-gestützte Systeme können das Lernen für jeden Schüler personalisieren. Sie analysieren Lernmuster und passen die Inhalte entsprechend an. Diese Technologie hilft, Wissenslücken zu identifizieren und bietet gezielte Unterstützung. Die Zukunft der Bildung sieht mit KI-Integration vielversprechend aus.",
    "language": "de",
    "compression": 20
  }'
```

**Response:**
```json
{
  "success": true,
  "summary": "Künstliche Intelligenz revolutioniert die Bildung. KI-gestützte Systeme können das Lernen für jeden Schüler personalisieren. Sie analysieren Lernmuster und passen die Inhalte entsprechend an. Diese Technologie hilft, Wissenslücken zu identifizieren und bietet gezielte Unterstützung. Die Zukunft der Bildung sieht mit KI-Integration vielversprechend aus.",
  "language": "de",
  "language_name": "German",
  "confidence": 1.0,
  "compression": 20,
  "original_length": 60,
  "summary_length": 48,
  "reduction": 20.0
}
```

## 🔧 Language Support

### Supported Languages

| Language | Code | Detection Method                 | Tokenizer          |
| -------- | ---- | -------------------------------- | ------------------ |
| English  | `en` | Auto-detect + character analysis | NLTK English Punkt |
| Russian  | `ru` | Auto-detect + cyrillic analysis  | NLTK Russian Punkt |
| German   | `de` | Auto-detect + umlaut analysis    | NLTK German Punkt  |

### Language Detection Logic

1. **Primary:** Uses `langdetect` library
2. **Fallback:** Character frequency analysis
3. **Default:** English if detection fails

## 📊 Compression Levels

| Level    | Percentage | Description                   | Use Case                            |
| -------- | ---------- | ----------------------------- | ----------------------------------- |
| Detailed | 20%        | Keeps 80% of original content | Research papers, detailed analysis  |
| Standard | 30%        | Keeps 70% of original content | General summarization, articles     |
| Concise  | 50%        | Keeps 50% of original content | Executive summaries, quick overview |

## 🐍 Code Examples

### Python Example

```python
import requests
import json

class MultilingualSummarizerClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
    
    def summarize(self, text, language="auto", compression=30):
        """Summarize text using the API."""
        url = f"{self.base_url}/summarize"
        payload = {
            "text": text,
            "language": language,
            "compression": compression
        }
        
        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def health_check(self):
        """Check API health."""
        url = f"{self.base_url}/health"
        try:
            response = requests.get(url, timeout=5)
            return response.json()
        except:
            return {"status": "unhealthy"}

# Usage example
if __name__ == "__main__":
    client = MultilingualSummarizerClient()
    
    # Check health
    health = client.health_check()
    print(f"API Status: {health.get('status')}")
    
    # Summarize text
    text = """
    Machine learning is a subset of artificial intelligence that provides 
    systems the ability to automatically learn and improve from experience 
    without being explicitly programmed. It focuses on the development of 
    computer programs that can access data and use it to learn for themselves.
    """
    
    result = client.summarize(text, language="auto", compression=30)
    
    if result.get("success"):
        print(f"Summary: {result['summary']}")
        print(f"Language: {result['language_name']}")
        print(f"Reduction: {result['reduction']}%")
    else:
        print(f"Error: {result.get('error')}")
```

### JavaScript/Node.js Example

```javascript
const axios = require('axios');

class MultilingualSummarizerClient {
    constructor(baseUrl = 'http://localhost:5000') {
        this.baseUrl = baseUrl;
        this.client = axios.create({
            baseURL: baseUrl,
            timeout: 30000,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
    }

    async summarize(text, language = 'auto', compression = 30) {
        try {
            const response = await this.client.post('/summarize', {
                text,
                language,
                compression
            });
            return response.data;
        } catch (error) {
            return {
                success: false,
                error: error.response?.data?.error || error.message
            };
        }
    }

    async healthCheck() {
        try {
            const response = await this.client.get('/health');
            return response.data;
        } catch {
            return { status: 'unhealthy' };
        }
    }
}

// Usage example
(async () => {
    const client = new MultilingualSummarizerClient();
    
    // Check health
    const health = await client.healthCheck();
    console.log(`API Status: ${health.status}`);
    
    // Summarize text
    const text = `Artificial intelligence is transforming many industries...`;
    
    const result = await client.summarize(text, 'auto', 30);
    
    if (result.success) {
        console.log(`Summary: ${result.summary}`);
        console.log(`Language: ${result.language_name}`);
        console.log(`Reduction: ${result.reduction}%`);
    } else {
        console.error(`Error: ${result.error}`);
    }
})();
```

### cURL Examples

**Basic summarization:**
```bash
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your text here...",
    "compression": 30
  }'
```

**With specific language:**
```bash
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Ваш текст здесь...",
    "language": "ru",
    "compression": 50
  }'
```

**Using environment variables:**
```bash
export TEXT="Your long text here..."
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$TEXT\", \"compression\": 30}"
```

## ⚠️ Error Handling

### Common Errors and Solutions

1. **Text too short error:**
   - **Error:** `"Text too short (min 50 characters)"`
   - **Solution:** Ensure input text has at least 50 characters

2. **Server not responding:**
   - **Error:** Connection timeout or connection refused
   - **Solution:** Check if the Flask server is running on port 5000

3. **Invalid JSON:**
   - **Error:** `400 Bad Request` with JSON parsing error
   - **Solution:** Ensure JSON is properly formatted

4. **Unsupported language:**
   - **Error:** Language detection fails or returns unsupported language
   - **Solution:** Specify language explicitly or use only supported languages

### Retry Logic Example

```python
import requests
import time

def summarize_with_retry(text, max_retries=3):
    """Summarize text with retry logic."""
    url = "http://localhost:5000/summarize"
    payload = {"text": text, "compression": 30}
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, timeout=30)
            if response.status_code == 200:
                return response.json()
            elif response.status_code >= 500:
                # Server error, retry
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            else:
                # Client error, don't retry
                return response.json()
        except requests.exceptions.RequestException:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
    
    return {"success": False, "error": "Max retries exceeded"}
```

## 🔐 Rate Limiting

The API implements basic rate limiting to prevent abuse:

- **Default limits:** 100 requests per day per IP
- **Burst limit:** 10 requests per hour
- **API Key:** Not required for basic usage

For production usage, consider:
1. Using API keys (contact for access)
2. Implementing your own rate limiting
3. Using batch processing for large volumes

## 📈 Performance Guidelines

### Best Practices

1. **Text Length:**
   - Optimal: 500-2000 characters
   - Maximum: 10,000 characters
   - Minimum: 50 characters

2. **Batch Processing:**
   - For multiple texts, send requests sequentially
   - Consider implementing client-side batching

3. **Caching:**
   - Cache results for identical texts
   - Implement TTL (Time To Live) for cached results

### Example with Caching

```python
from functools import lru_cache
import hashlib

class CachedSummarizerClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.client = MultilingualSummarizerClient(base_url)
    
    @lru_cache(maxsize=1000)
    def summarize_cached(self, text, language="auto", compression=30):
        """Summarize with caching based on text hash."""
        return self.client.summarize(text, language, compression)
    
    def _get_cache_key(self, text, language, compression):
        """Generate cache key from parameters."""
        content = f"{text}:{language}:{compression}"
        return hashlib.md5(content.encode()).hexdigest()
```

## 🚀 Production Deployment

### Environment Variables

```bash
# Production configuration
export FLASK_ENV=production
export PORT=5000
export WORKERS=4
export MAX_CONTENT_LENGTH=10485760  # 10MB
```

### Load Balancer Configuration

```nginx
# Nginx configuration for load balancing
upstream summarizer_backend {
    server 127.0.0.1:5000;
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
}

server {
    listen 80;
    server_name api.your-domain.com;
    
    location / {
        proxy_pass http://summarizer_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # Timeouts
        proxy_connect_timeout 30s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
    }
}
```

## 🔄 API Versioning

The current API is version 1.0. All endpoints are under the root path. Future versions may use path-based versioning:

- Current: `POST /summarize`
- Future: `POST /v2/summarize`

## 📞 Support

For API support, issues, or feature requests:

- **GitHub Issues:** [API Issues](https://github.com/yourusername/Multilingual-Summarizer/issues)
- **Email:** api-support@yourdomain.com
- **Documentation:** [Full Documentation](https://github.com/yourusername/Multilingual-Summarizer/docs)

---

## 📄 License

This API is provided under the MIT License. See the LICENSE file for details.

## 🔗 Related Resources

- [GitHub Repository](https://github.com/yourusername/Multilingual-Summarizer)
- [Web Interface](http://localhost:5000)
- [Python SDK](https://pypi.org/project/multilingual-summarizer/)
- [Postman Collection](https://www.postman.com/your-workspace)

---

*API Version: 1.0.0*    
*Base URL: http://localhost:5000*