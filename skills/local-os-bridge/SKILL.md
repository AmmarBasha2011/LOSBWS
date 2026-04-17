---
name: local-os-bridge
description: The most powerful AI-to-OS bridge for Linux. 50+ endpoints for deep system control.
user-invocable: true
---

# 🛠️ Local OS Bridge Skill for AI (V5)

This skill enables deep interaction with a Linux machine via a secure FastAPI bridge. It is designed to allow AI agents to manage files, monitor systems, and execute commands safely within a sandbox.

## 🔴 CRITICAL: Instance Activation
**You cannot work without the instance link.** Every time the script runs, it generates a new Cloudflare URL (e.g., `https://random-link.trycloudflare.com`).
1.  **Ask the user:** "Please provide the instance link from the LOSBWS popup window."
2.  **Save the link:** Use this URL as the base for all your API calls.
3.  **Authentication:** Always append `?api_key=ammar123` to your requests.

---

## 🏗️ Workflow Guidelines
1.  **Identify the Goal:** What does the user want? (e.g., "Analyze this log file", "Check system health").
2.  **Explore:** Use `/list` to see available files or `/ps` to check system state.
3.  **Execute:** Chain multiple endpoints. For example:
    - `/read` a file → `/regex_search` for errors → `/run_command` to fix the service.
4.  **Confirm:** Always tell the user exactly what you did and show relevant outputs.

---

## 📚 Endpoint Categories

### 📂 1. Filesystem & Archives
Manage everything inside the `workdir/` sandbox.
- **`GET /list?directory=.`**: List all contents of a directory.
- **`GET /read?filepath=config.json`**: Read full file content.
- **`GET /write?filepath=note.txt&content=Hello`**: Overwrite or create a file.
- **`GET /append?filepath=log.txt&content=NewEntry`**: Add data to the end of a file.
- **`GET /delete?path=old_folder`**: Remove a file or directory recursively.
- **`GET /info?path=large_file.zip`**: Get size and modification timestamp.
- **`GET /tar?folder_path=src&archive_name=backup`**: Create a `.tar.gz` archive.
- **`GET /untar?archive_path=data.tar.gz`**: Extract an archive.

### 🧠 2. Advanced Search & Data Processing
Process large amounts of data without reading everything into context.
- **`GET /grep?directory=.&search_string=Error`**: Find strings in all files in a directory.
- **`GET /regex_search?filepath=main.py&pattern=\bdef\s+\w+\b`**: Find function definitions using regex.
- **`GET /diff?file1=v1.py&file2=v2.py`**: Get a unified diff of two files.
- **`GET /csv_to_json?filepath=data.csv`**: Convert tabular data into a JSON list.
- **`GET /split?filepath=big.log&lines_per_chunk=500`**: Break a large file into smaller pieces.

### ⚡ 3. System, Processes & Git
Full control over the OS and development tools.
- **`GET /run_command?command=ls -la`**: Run any shell command in `workdir/`.
- **`GET /ps`**: See the top 15 most resource-heavy processes.
- **`GET /kill?pid=999`**: Terminate a specific process.
- **`GET /git_status`**: Check if the current directory is a git repo and its status.
- **`GET /whoami`**: Verify which Linux user you are running as.

### 🌐 4. Network & Security
Interact with the internet and verify file integrity.
- **`GET /curl?url=https://google.com`**: Make a request from the host machine (useful as a proxy).
- **`GET /download_url?url=...&save_as=app.py`**: Download a file directly to the server.
- **`GET /ip`**: Get the public IP address of the host machine.
- **`GET /hash?filepath=main.py`**: Get the SHA256 signature to verify integrity.
- **`GET /base64_read?filepath=image.png`**: Read binary files as Base64.

---

## ⚠️ Error Handling
- **401 Unauthorized:** Your `api_key` is missing or wrong.
- **403 Forbidden:** You tried to access a path outside of the `workdir/` (Sandbox escape).
- **404 Not Found:** The file or directory does not exist.
- **500 Internal Error:** Something went wrong on the server side (check logs).

---

## 💡 Pro Tip for AI
If you are asked to "Fix a bug", follow this:
1. `GET /list` to find the source.
2. `GET /read` the problematic file.
3. Propose a fix, then `GET /write` the updated content.
4. `GET /run_command` to test if the code works.
