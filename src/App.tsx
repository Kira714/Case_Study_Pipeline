import React, { useState, useEffect } from 'react';
import { io } from 'socket.io-client';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { AlertTriangle, TrendingUp, TrendingDown } from 'lucide-react';

const socket = io('http://localhost:5000');

function App() {
  const [stockData, setStockData] = useState([]);
  const [analytics, setAnalytics] = useState({});
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    socket.on('data_update', (data) => {
      setStockData(data.data);
      setAnalytics(data.analytics);
    });

    return () => {
      socket.off('data_update');
    };
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-8">Financial Data Analytics Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Stock Prices</h2>
          <LineChart width={600} height={300} data={stockData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Datetime" />
            <YAxis />
            <Tooltip />
            <Legend />
            {Object.keys(analytics).map((symbol, index) => (
              <Line key={symbol} type="monotone" dataKey={symbol} stroke={`#${Math.floor(Math.random()*16777215).toString(16)}`} />
            ))}
          </LineChart>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Analytics</h2>
          {Object.entries(analytics).map(([symbol, data]) => (
            <div key={symbol} className="mb-4">
              <h3 className="text-lg font-medium">{symbol}</h3>
              <p>Trading Volume: {data.trading_volume.toFixed(2)}</p>
              <p>Volatility: {data.volatility.toFixed(4)}</p>
              <p>Trend: {data.trends === 'upward' ? <TrendingUp className="inline text-green-500" /> : <TrendingDown className="inline text-red-500" />}</p>
            </div>
          ))}
        </div>
      </div>
      
      <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">Alerts</h2>
        {alerts.length > 0 ? (
          <ul>
            {alerts.map((alert, index) => (
              <li key={index} className="flex items-center text-yellow-600">
                <AlertTriangle className="mr-2" />
                {alert}
              </li>
            ))}
          </ul>
        ) : (
          <p>No active alerts</p>
        )}
      </div>
    </div>
  );
}

export default App;