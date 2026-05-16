import requests
import time
import threading
import uvicorn
from main import app

API_KEY = "ammar123"
BASE_URL = "http://127.0.0.1:8000"

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

def test_sudo():
    print("--- TESTING REWRITTEN SUDO ---")
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(3)

    try:
        # Testing a command that requires sudo and returns clear output
        r = requests.get(f"{BASE_URL}/sudo", params={"api_key": API_KEY, "command": "whoami"})
        data = r.json()
        print(f"Response: {data}")
        if data.get("stdout") == "root":
            print("✅ SUDO FIX VERIFIED: /sudo whoami returned 'root'")
        else:
            print("❌ SUDO FIX FAILED: Did not return 'root'")
    except Exception as e:
        print(f"Test Error: {e}")

if __name__ == "__main__":
    test_sudo()
