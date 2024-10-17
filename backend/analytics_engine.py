import pandas as pd
import numpy as np
from typing import Dict, Any

class AnalyticsEngine:
    def __init__(self):
        pass

    def process_data(self, data: pd.DataFrame) -> Dict[str, Any]:
        results = {}
        for column in data.columns:
            if column != 'Datetime':
                results[column] = {
                    'trading_volume': self.calculate_trading_volume(data[column]),
                    'volatility': self.calculate_volatility(data[column]),
                    'trends': self.identify_trends(data[column])
                }
        return results

    def calculate_trading_volume(self, prices: pd.Series) -> float:
        return np.sum(np.abs(np.diff(prices)))

    def calculate_volatility(self, prices: pd.Series) -> float:
        return np.std(prices)

    def identify_trends(self, prices: pd.Series) -> str:
        if prices.iloc[-1] > prices.iloc[0]:
            return 'upward'
        elif prices.iloc[-1] < prices.iloc[0]:
            return 'downward'
        else:
            return 'stable'

    def detect_anomalies(self, prices: pd.Series, threshold: float = 2.0) -> pd.Series:
        rolling_mean = prices.rolling(window=5).mean()
        rolling_std = prices.rolling(window=5).std()
        z_scores = (prices - rolling_mean) / rolling_std
        return z_scores[abs(z_scores) > threshold]