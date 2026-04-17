---
name: local-os-bridge
description: Control the local Linux machine via a secure FastAPI bridge with 50+ endpoints.
user-invocable: true
---

# Local OS Bridge Skill for OpenClaw

This skill allows OpenClaw to interact with the local operating system through the "Ultimate Local OS Bridge" (FastAPI).

## CRITICAL INSTRUCTION
**You must get the instance link before working because it changes every time the user runs the script.**

## Prerequisites
1. The user must run the `main.py` script first to start the bridge and the Cloudflare tunnel.
2. Once the script is running, it will print a **PUBLIC LINK** (e.g., `https://random-words.trycloudflare.com`).
3. You must use this link and the `api_key=ammar123` for all requests.

## How to use
- **List files:** `GET {instance_link}/list?api_key=ammar123&directory=.`
- **Read file:** `GET {instance_link}/read?api_key=ammar123&filepath=somefile.txt`
- **Run command:** `GET {instance_link}/run_command?api_key=ammar123&command=ls -la`
- **Check Swagger Docs:** `{instance_link}/docs`

## Setup Instructions for User
If you haven't installed the dependencies yet:
1. Clone the repo: `git clone https://github.com/AmmarBasha2011/LOSBWS`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python main.py`
4. Copy the public URL and provide it to OpenClaw.

For more details, visit: https://github.com/AmmarBasha2011/LOSBWS
