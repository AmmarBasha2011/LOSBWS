from pyngrok import ngrok
import time

AUTHTOKEN = "3CUk8ZA0prhtKdf97ybONQU3b0V_7NwrHbfFB8gXf6sfXQxGB"
DOMAIN = "citrus-trance-exporter.ngrok-free.dev"

print(f"--- TESTING NGROK FREE STABLE DOMAIN ---")
print(f"Setting authtoken...")
ngrok.set_auth_token(AUTHTOKEN)

try:
    print(f"Attempting to start tunnel on domain: {DOMAIN}")
    # We specify the domain and port. Ngrok free tier allows 1 static domain.
    tunnel = ngrok.connect(8000, "http", domain=DOMAIN)
    print(f"✅ SUCCESS! Your tunnel is live at: {tunnel.public_url}")
    print("This means the FREE STABLE DOMAIN works.")
    
    # Close it after 5 seconds
    time.sleep(5)
    ngrok.disconnect(tunnel.public_url)
    print("Tunnel closed.")
except Exception as e:
    print(f"❌ FAILED: {e}")
    print("\nTip: Make sure the domain is correctly created in your Ngrok dashboard.")
