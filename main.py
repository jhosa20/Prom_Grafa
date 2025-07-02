from flask import Flask
from prometheus client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNTER = Counter("app_requests_total", "Total requests to root endpoint")

@app.route("/")
def index():
    REQUEST_COUNTER. inc()
    return "Hello from monitored Python app!"

@app. route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == " __main__":
    app.run(host="0.0.0.0", port=8000)

