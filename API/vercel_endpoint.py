from http.server import BaseHTTPRequestHandler
import json
import numpy as np

# Load the data once when the function initializes
DATA = [
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 116.88,
    "uptime_pct": 97.761,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 147.03,
    "uptime_pct": 97.788,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 130.55,
    "uptime_pct": 98.626,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 145.31,
    "uptime_pct": 98.712,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 221.98,
    "uptime_pct": 98.589,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 141.26,
    "uptime_pct": 98.58,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 176.47,
    "uptime_pct": 97.966,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 207.9,
    "uptime_pct": 98.261,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 117.12,
    "uptime_pct": 98.332,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 203.08,
    "uptime_pct": 97.328,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 140.78,
    "uptime_pct": 98.16,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 182.52,
    "uptime_pct": 97.698,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 144.39,
    "uptime_pct": 98.034,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 186.57,
    "uptime_pct": 97.275,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 137.08,
    "uptime_pct": 97.417,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 159.18,
    "uptime_pct": 97.429,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 158.32,
    "uptime_pct": 97.398,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 206.44,
    "uptime_pct": 98.888,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 208.51,
    "uptime_pct": 99.37,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 196.81,
    "uptime_pct": 99.07,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 231.51,
    "uptime_pct": 98.899,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 188.93,
    "uptime_pct": 99.072,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 236.45,
    "uptime_pct": 99.314,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 198.92,
    "uptime_pct": 99.083,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 217.72,
    "uptime_pct": 99.154,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 231.63,
    "uptime_pct": 98.191,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 198.99,
    "uptime_pct": 97.125,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 181.53,
    "uptime_pct": 97.843,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 99.58,
    "uptime_pct": 97.972,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 198.1,
    "uptime_pct": 97.19,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 200.7,
    "uptime_pct": 97.994,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 136.23,
    "uptime_pct": 98.18,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 176.11,
    "uptime_pct": 98.548,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 209.7,
    "uptime_pct": 98.731,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 227.55,
    "uptime_pct": 99.099,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 122.27,
    "uptime_pct": 98.272,
    "timestamp": 20250312
  }
]

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Set CORS headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Parse request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        request_body = json.loads(post_data.decode('utf-8'))
        
        regions = request_body.get('regions', [])
        threshold_ms = request_body.get('threshold_ms', 0)
        
        # Calculate metrics for each region
        result = {}
        for region in regions:
            region_data = [d for d in DATA if d['region'] == region]
            
            if region_data:
                latencies = [d['latency_ms'] for d in region_data]
                uptimes = [d['uptime_pct'] for d in region_data]
                breaches = sum(1 for lat in latencies if lat > threshold_ms)
                
                result[region] = {
                    'avg_latency': round(np.mean(latencies), 2),
                    'p95_latency': round(np.percentile(latencies, 95), 2),
                    'avg_uptime': round(np.mean(uptimes), 2),
                    'breaches': breaches
                }
        
        self.wfile.write(json.dumps(result).encode('utf-8'))
        
    def do_OPTIONS(self):
        # Handle preflight CORS requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
