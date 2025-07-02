from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
visits = Counter('web_visits_total', 'Total web visits')

@app. route ('/')
def home():
    visits.inc()
    return "Hello, Prometheus!"

@app. route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

app.run(host='0.0.0.0', port=5000)