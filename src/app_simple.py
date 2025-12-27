"""
Minimal working version of Multilingual Summarizer
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Multilingual Summarizer is running!"

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'Multilingual Summarizer',
        'version': '1.0'
    })

@app.route('/test')
def test():
    return jsonify({'message': 'Test endpoint works!'})

if __name__ == '__main__':
    print("🚀 Starting minimal server on port 5001...")
    app.run(host='0.0.0.0', port=5001, debug=True)
