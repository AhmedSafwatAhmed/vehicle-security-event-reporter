from flask import Blueprint, request, render_template, jsonify
import datetime
import json
import os

bp = Blueprint('main', __name__)

SECURITY_LOG_FILE = "security_events.log"

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/report_event", methods=["POST"])
def report_event():
    data = request.get_json()

    if not data or "event_type" not in data or "ecu_id" not in data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    event = {
        "timestamp": str(datetime.datetime.utcnow()),
        "ecu_id": data["ecu_id"],
        "event_type": data["event_type"],
        "severity": data.get("severity", "low")
    }

    with open(SECURITY_LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    return jsonify({"status": "event logged", "event": event}), 200

@bp.route("/dashboard")
def dashboard():
    events = []
    if os.path.exists(SECURITY_LOG_FILE):
        with open(SECURITY_LOG_FILE) as f:
            for line in f:
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return render_template("dashboard.html", events=events)
