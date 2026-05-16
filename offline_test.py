import requests
import time
import os
import threading
import uvicorn
from main import app

API_KEY = "ammar123"
BASE_URL = "http://127.0.0.1:8000"

def run_server():
    # Set DISPLAY for local testing
    os.environ["DISPLAY"] = ":0"
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

def test_gui_endpoints():
    print("--- STARTING GUI OFFLINE TEST ---")
    
    # Start server in thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(5) # Wait for server to start

    # 1. Test /screenshot
    print("\nTesting /screenshot...")
    try:
        r = requests.get(f"{BASE_URL}/screenshot", params={"api_key": API_KEY})
        if r.status_code == 200 and r.headers.get("content-type") == "image/png":
            print(f"✅ SUCCESS: Screenshot received ({len(r.content)} bytes)")
            with open("test_screenshot_received.png", "wb") as f:
                f.write(r.content)
        else:
            print(f"❌ FAILED: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Error testing /screenshot: {e}")

    # 2. Test /type
    print("\nTesting /type...")
    try:
        # We use a safe string
        r = requests.get(f"{BASE_URL}/type", params={"api_key": API_KEY, "text": "Hello from Bridge Test!"})
        print(f"Response: {r.json()}")
    except Exception as e:
        print(f"Error testing /type: {e}")

    # 3. Test /click
    print("\nTesting /click...")
    try:
        # Clicking at (100, 100)
        r = requests.get(f"{BASE_URL}/click", params={"api_key": API_KEY, "x": 100, "y": 100})
        print(f"Response: {r.json()}")
    except Exception as e:
        print(f"Error testing /click: {e}")

if __name__ == "__main__":
    test_gui_endpoints()
