from flasgger import Swagger
from flask import Flask, jsonify
from opentelemetry import trace
from opentelemetry._logs import set_logger_provider
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.metrics import get_meter_provider, set_meter_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor, ConsoleLogExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import set_tracer_provider
from utils import get_random_int
import logging

app = Flask(__name__)
Swagger(app)

# Instrument traces
tracer = trace.get_tracer(__name__)
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
set_tracer_provider(tracer_provider)

# Instrument metrics
meter_provider = MeterProvider(metric_readers=[
    PeriodicExportingMetricReader(ConsoleMetricExporter(), export_interval_millis=5000)
])
set_meter_provider(meter_provider)

# Custom metrics
meter = get_meter_provider().get_meter('custom_meter')
counter = meter.create_counter('home_counter')
histogram = meter.create_histogram('flights_histogram')

# Instrument logs
logger_provider = LoggerProvider()
logger_provider.add_log_record_processor(BatchLogRecordProcessor(ConsoleLogExporter()))
set_logger_provider(logger_provider)
handler = LoggingHandler(logger_provider=logger_provider)
logger = logging.getLogger()
logger.addHandler(handler)

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
    counter.add(1)
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
    histogram.record(random_int)

if __name__ == "__main__":
    app.run(debug=True)
