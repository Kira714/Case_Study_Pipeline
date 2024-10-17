import yfinance as yf
import pandas as pd
from typing import List

class DataMiner:
    def __init__(self, symbols: List[str] = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']):
        self.symbols = symbols
        self.data = pd.DataFrame()

    def fetch_data(self) -> pd.DataFrame:
        data = yf.download(self.symbols, period="1d", interval="1m")
        self.data = data['Close'].reset_index()
        return self.data

    def get_latest_data(self) -> dict:
        return self.data.to_dict(orient='records')

    def find_sudden_price_spikes(self, threshold: float = 0.02) -> List[dict]:
        spikes = []
        for symbol in self.symbols:
            prices = self.data[symbol].values
            for i in range(1, len(prices)):
                if abs(prices[i] - prices[i-1]) / prices[i-1] > threshold:
                    spikes.append({
                        'symbol': symbol,
                        'time': self.data['Datetime'][i],
                        'price_change': prices[i] - prices[i-1]
                    })
        return spikes

    def calculate_moving_average(self, window: int = 5) -> pd.DataFrame:
        return self.data.rolling(window=window).mean()