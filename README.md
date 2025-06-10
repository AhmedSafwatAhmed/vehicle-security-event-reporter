# vehicle-security-event-reporter
A simple web application that receives data about security events from IdsM or alerts sent from the ECU (as a JSON payload) and displays it in a simple interface. It's more like a backend example of the ECU Communicator or Central Gateway.

A dashboard (/dashboard) shall read a log file of reported events (security_events.log), parses the JSON lines, and renders them into a clean HTML table using Flask's template engine (Jinja2).
Each row shows:

Timestamp – When the event occurred
ECU ID – Identifier of the electronic unit
Event Type – e.g., tamper_detected, flooding, spoofing
Severity – Optional tag (low/medium/high)

# main tech used
- python
- Flask
- JSON
- Jinja2

# A prior part of the project should be AUTOSAR plugin IdsM integration 
and reporting security events after being qualified. TBD