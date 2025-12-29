# Flask Application

This project is a Flask web application.
Follow the steps below to set it up and run it on macOS or Windows using a virtual environment.

## Prerequisites
- Python 3.8+
- pip

## Setup

1. Create venv and activate:

   macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   Windows (PowerShell):
   python -m venv venv
   venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt
   # or
   pip install flask

3. Set Flask app (if needed):
   macOS/Linux: export FLASK_APP=app.py
   Windows (PowerShell): $env:FLASK_APP="app.py"

4. Run app:
   flask run

5. Access in browser: http://127.0.0.1:5000

6. Deactivate venv when done:
   deactivate

EOL
