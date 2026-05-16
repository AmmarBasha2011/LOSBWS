import requests
import time
import os
import threading
import uvicorn
from main import app

API_KEY = "ammar123"
BASE_URL = "http://127.0.0.1:8000"

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

def test_endpoints():
    print("--- STARTING OFFLINE TEST ---")
    
    # Start server in thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(5) # Wait for server to start

    results = []

    # 1. Test /open (Creating a dummy file first)
    if not os.path.exists("workdir"):
        os.makedirs("workdir")
    with open("workdir/test_open.txt", "w") as f:
        f.write("This is a test file for the /open endpoint.")
    
    print("\nTesting /open...")
    try:
        r = requests.get(f"{BASE_URL}/open", params={"api_key": API_KEY, "filepath": "test_open.txt"})
        print(f"Response: {r.json()}")
        results.append(r.status_code == 200)
    except Exception as e:
        print(f"Error testing /open: {e}")
        results.append(False)

    # 2. Test /sudo (Running a safe sudo command: whoami)
    print("\nTesting /sudo (whoami)...")
    try:
        r = requests.get(f"{BASE_URL}/sudo", params={"api_key": API_KEY, "command": "whoami"})
        print(f"Response: {r.json()}")
        # Should return "root" in stdout if sudo worked
        results.append(r.status_code == 200 and "root" in r.json().get("stdout", "").lower())
    except Exception as e:
        print(f"Error testing /sudo: {e}")
        results.append(False)

    print("\n--- TEST SUMMARY ---")
    if all(results):
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED.")

if __name__ == "__main__":
    test_endpoints()
