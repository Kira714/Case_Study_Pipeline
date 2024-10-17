import time
from typing import Dict, Any

class Monitor:
    def __init__(self):
        self.metrics = {
            'data_retrieval_latency': [],
            'processing_time': [],
            'error_count': 0
        }

    def update_metrics(self, data: Any, analytics_results: Dict[str, Any]):
        self.metrics['data_retrieval_latency'].append(time.time() - data['Datetime'].max().timestamp())
        self.metrics['processing_time'].append(time.time())

    def check_thresholds(self):
        alerts = []
        if len(self.metrics['data_retrieval_latency']) > 0 and self.metrics['data_retrieval_latency'][-1] > 5:
            alerts.append("High data retrieval latency detected")
        if len(self.metrics['processing_time']) > 1:
            processing_time = self.metrics['processing_time'][-1] - self.metrics['processing_time'][-2]
            if processing_time > 1:
                alerts.append(f"High processing time detected: {processing_time:.2f} seconds")
        return alerts

    def log_error(self, error_message: str):
        self.metrics['error_count'] += 1
        print(f"Error: {error_message}")

    def get_performance_metrics(self) -> Dict[str, Any]:
        return {
            'avg_data_retrieval_latency': sum(self.metrics['data_retrieval_latency']) / len(self.metrics['data_retrieval_latency']) if self.metrics['data_retrieval_latency'] else 0,
            'avg_processing_time': sum(self.metrics['processing_time']) / len(self.metrics['processing_time']) if self.metrics['processing_time'] else 0,
            'error_count': self.metrics['error_count']
        }