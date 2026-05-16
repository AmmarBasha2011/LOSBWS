import requests
import time
import os
import threading
import uvicorn
from main import app
import pyautogui

API_KEY = "ammar123"
BASE_URL = "http://127.0.0.1:8000"

def run_server():
    os.environ["DISPLAY"] = ":0"
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

def test_gui():
    print("--- TESTING GUI ENDPOINTS ---")
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(3)

    # 1. Screenshot
    print("\nTesting /screenshot...")
    r = requests.get(f"{BASE_URL}/screenshot", params={"api_key": API_KEY})
    print(f"Screenshot Status: {r.status_code}")
    
    # 2. Type
    print("\nTesting /type...")
    r = requests.get(f"{BASE_URL}/type", params={"api_key": API_KEY, "text": "Test"})
    print(f"Type Response: {r.json()}")

    # 3. Click
    print("\nTesting /click...")
    r = requests.get(f"{BASE_URL}/click", params={"api_key": API_KEY, "x": 10, "y": 10})
    print(f"Click Response: {r.json()}")

if __name__ == "__main__":
    test_gui()
