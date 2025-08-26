import requests
import time
import random

base_url = "http://fastapi:8000"

def generate_traffic():
    endpoints = ["/", "/slow", "/error", "/health"]
    i = 0
    while True:
        endpoint = random.choice(endpoints)
        try:
            response = requests.get(f"{base_url}{endpoint}")
            print(f"Request {i+1}: {endpoint} -> {response.status_code}")
        except Exception as e:
            print(f"Request {i+1}: {endpoint} -> ERROR: {e}")
        i += 1
        # Random delay between requests
        time.sleep(random.uniform(0.2, 2.0))

if __name__ == "__main__":
    generate_traffic()
