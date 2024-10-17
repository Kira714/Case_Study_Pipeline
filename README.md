# Financial Data Pipeline Case Study

Hi everyone,  
This is **Sachit Kumbhat**, and here's my case study on how to build a pipeline for a financial company. I have used the `yfinance` library to pull real-time stock data from Yahoo Finance in the `DataMiner` class. This covers the requirement of pulling data from a public API (in this case, Yahoo Finance). The fetched data includes the closing prices for stocks, which are processed and analyzed further. I have also implemented:

- **Analytics Engine**: A simple analytics engine (`AnalyticsEngine`) that processes the mined data and calculates metrics like trading volume, volatility, and trends.
- **Background Task**: A background task using Python’s `threading` library to periodically fetch new stock data and process it. This helps ensure continuous data updates without blocking the main Flask server, optimizing for speed.
- **Efficiency**: Efficient data structures like Pandas DataFrames are used to handle large volumes of stock data. If dealing with significantly larger datasets, performance optimizations like vectorized operations or implementing batch processing where possible could be added.

## Project Setup

### 1. Install Dependencies

To install both Node.js dependencies (for the frontend) and Python dependencies (for the backend), use the following command:

```bash
npm install && pip install -r backend/requirements.txt
```
This will install all necessary packages for both environments.


### 2. Start the Backend Server

To start the Flask backend server with SocketIO, run:

```bash

python backend/main.py
```
This will start the backend server on http://localhost:5000.

### 3. Start the Frontend Development Server

For the frontend, you will use Vite as the development server. Run the following command:

```bash

npm run dev
```
This will start the Vite development server and make the frontend available at the URL provided in the terminal.

### 4. Full Local Setup

Now, the entire pipeline should be running locally. The frontend communicates with the backend at http://localhost:5000.

#### Deployment

### 1. Build the Frontend

Before deploying the frontend, you need to create a production-ready build. Run the following command:

```bash

npm run build
```
This will generate the build in the dist directory.

### 2. Deploy the Frontend

For the frontend, Netlify is a good option for deployment. Here's how you can deploy it:
Build the frontend:

   ``` bash

npx vite build
```
Deploy the frontend to Netlify:

```bash

    netlify
```
### 3. Deploy the Backend

For the backend, you can use Heroku. Here's the typical deployment process:

  Create a Procfile in the root directory with the following content:

   ``` bash

    web: gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 backend.main:app
```
  Add gunicorn and gevent-websocket to your backend/requirements.txt file.

   Deploy to Heroku using the Heroku CLI or through GitHub integration.

### 4. Update Frontend Configuration

Once the backend is deployed, you need to update the frontend to connect to the new backend URL. Update the SocketIO connection in src/App.tsx like so:

```javascript

const socket = io("https://your-deployed-backend-url");
```
After making this change, rebuild and redeploy the frontend.
### Thank you
