from flask import send_from_directory
from app import app

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')