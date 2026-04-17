#!/bin/bash

# --- CHECK FOR VENV ---
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment (venv) not found. Please run install instructions first."
    exit 1
fi

# --- ACTIVATE VENV ---
source venv/bin/bin/activate 2>/dev/null || source venv/bin/activate

# --- HELPER TO CAPTURE URL AND SHOW GUI ---
# We run main.py in the background, capture its output, find the tunnel URL,
# then show a Tkinter window with the URL and a copy button.

python3 - <<EOF &
import subprocess
import re
import sys
import tkinter as tk
from tkinter import messagebox

def show_gui(url):
    root = tk.Tk()
    root.title("LOSBWS - Instance Link")
    root.geometry("500x150")
    root.eval('tk::PlaceWindow . center')
    
    label = tk.Label(root, text="🚀 Your AI Bridge is LIVE!", font=("Arial", 12, "bold"))
    label.pack(pady=10)
    
    entry = tk.Entry(root, width=50, justify='center')
    entry.insert(0, url)
    entry.config(state='readonly')
    entry.pack(pady=5)
    
    def copy_and_close():
        root.clipboard_clear()
        root.clipboard_append(url)
        messagebox.showinfo("Success", "Link copied to clipboard! Closing window...")
        root.destroy()
        # We don't exit the whole script here, just the GUI.
        # But for this specific helper, we want the GUI to go away.

    copy_btn = tk.Button(root, text="Copy Link & Close", command=copy_and_close, bg="#4CAF50", fg="white")
    copy_btn.pack(pady=10)
    
    root.mainloop()

# Start main.py and monitor stdout
process = subprocess.Popen([sys.executable, "main.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

print("⏳ Starting Local OS Bridge with Stable URL...")

for line in process.stdout:
    print(line, end="") # Still print to console
    # Look for the Ngrok or Cloudflare URL
    match = re.search(r"https://[a-zA-Z0-9.-]+\.(ngrok-free\.dev|trycloudflare\.com)", line)
    if match:
        url = match.group(0)
        show_gui(url)
        # After GUI closes, we keep main.py running
        break

# Keep printing output if any
for line in process.stdout:
    print(line, end="")

process.wait()
EOF

# Wait for background process
wait
