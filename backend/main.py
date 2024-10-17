import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, jsonify
from flask_socketio import SocketIO
import threading
import time
from data_mining import DataMiner
from analytics_engine import AnalyticsEngine
from monitoring import Monitor

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

data_miner = DataMiner()
analytics_engine = AnalyticsEngine()
monitor = Monitor()

@app.route('/api/stock-data')
def get_stock_data():
    return jsonify(data_miner.get_latest_data())

def background_task():
    while True:
        data = data_miner.fetch_data()
        analytics_results = analytics_engine.process_data(data)
        monitor.update_metrics(data, analytics_results)
        socketio.emit('data_update', {'data': data.to_dict(), 'analytics': analytics_results})
        time.sleep(60)  # Update every minute

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    threading.Thread(target=background_task, daemon=True).start()
    socketio.run(app, debug=True, port=5000)