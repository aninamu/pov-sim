from flasgger import Swagger
from flask import Flask, jsonify
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import set_tracer_provider
from utils import get_random_int

app = Flask(__name__)
Swagger(app)

tracer = trace.get_tracer(__name__)
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
set_tracer_provider(tracer_provider)
FlaskInstrumentor().instrument_app(app)

AIRLINES = ["AA", "UA", "DL"]

@app.route("/")
def home():
    """No-op home endpoint
    ---
    responses:
      200:
        description: Returns ok
    """
    return jsonify({"message": "ok"})


@app.route("/airlines/<err>")
def get_airlines(err=None):
    """Get airlines endpoint. Set err to "raise" to trigger an exception.
    ---
    parameters:
      - name: err
        in: path
        type: string
        enum: ["raise"]
        required: false
    responses:
      200:
        description: Returns a list of airlines
    """
    if err == "raise":
        raise Exception("Raise test exception")
    return jsonify({"airlines": AIRLINES})

@app.route("/flights/<airline>/<err>")
def get_flights(airline, err=None):
    """Get flights endpoint. Set err to "raise" to trigger an exception.
    ---
    parameters:
      - name: airline
        in: path
        type: string
        enum: ["AA", "UA", "DL"]
        required: true
      - name: err
        in: path
        type: string
        enum: ["raise"]
        required: false
    responses:
      200:
        description: Returns a list of flights for the selected airline
    """
    if err == "raise":
      raise Exception("Raise test exception")
    with tracer.start_as_current_span('get_random_int'):
      random_int = get_random_int(100, 999)
    return jsonify({airline: [random_int]})

if __name__ == "__main__":
    app.run(debug=True)
