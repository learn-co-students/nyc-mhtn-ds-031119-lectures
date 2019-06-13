from flask import render_template, jsonify, json

from dash_package.dashboard import app

@app.server.route('/demo')
def hello():
    return "Oh hello"

@app.server.route('/dash')
def dashboard():
    return app.index()
