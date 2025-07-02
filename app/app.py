from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(_name_)
visits = Counter('webapp_visits_total', 'Total visits to the homepage")

@app.route("/")
def hello():
    visits.inc()
    return "Hello, Prometheus!"

@app.route("/metrics")
def metrics():
    return generate_latest()

if _name_ == "_main_ ":
    app.run(host="0.0.0.0", port=8000)