---
name: local-os-bridge
description: The ultimate master manual for OS control. 50+ endpoints for Filesystem, GUI, System, and Network.
repo: https://github.com/AmmarBasha2011/LOSBWS
user-invocable: true
---

# 👑 MASTER MANUAL: Ultimate Local OS Bridge (V5)

This is the definitive guide for AI agents to control the host Linux machine. You must use this file to understand every capability, parameter, and expected response.

## 🔴 1. CRITICAL ACTIVATION & AUTH
1.  **Instance Link:** Ask the user for the "Instance Link" from their bridge script.
2.  **Ngrok Warning:** You **MUST** send the header `ngrok-skip-browser-warning: true` with every request.
3.  **API Key:** Append `?api_key=ammar123` (or the user's custom key) to every request.
4.  **Sandbox:** You are restricted to the `workdir/` folder for file operations. Use relative paths.

---

## 🏗️ 2. GUI AUTOMATION WORKFLOW
To control the user's screen, follow this cycle:
1.  **Get Context:** `GET /screen_info` to get resolution.
2.  **Vision:** `GET /screenshot?grid=true&b64=true` to see the desktop with a coordinate grid.
    - Using `grid=true` adds red/yellow X/Y markers.
    - Using `b64=true` returns a JSON string that is easy for AI agents (like n8n) to "read".
3.  **Analyze:** Find target coordinates (X, Y) using the red/yellow markers on the image.
4.  **Action:** Use `/click`, `/type`, or `/open`.
5.  **Verify:** `GET /screenshot` (without grid) to confirm the result.

---

## 📚 3. COMPLETE ENDPOINT REFERENCE

### 🖱️ A. GUI & Desktop Control
| Endpoint | Inputs | Description | Example Output |
| :--- | :--- | :--- | :--- |
| `/screen_info`| None | Get screen size & mouse pos. | `{"width": 1920, ...}` |
| `/screenshot` | `grid` (bool), `b64` (bool) | Capture screen. Set `grid=true` for markers. Set `b64=true` to get AI-friendly JSON. | `{"base64": "...", "mime_type": "image/png"}` |
| `/click` | `x`, `y` | Hardware-level mouse click. | `{"message": "Clicked..."}` |
| `/type` | `text` | Simulate keyboard typing. | `{"message": "Typed text: Hello"}` |
| `/open` | `filepath` | Open file in default app (Brave, etc). | `{"message": "Opening file.html..."}` |

### ⚡ B. System & OS Power
| Endpoint | Inputs | Description | Example Output |
| :--- | :--- | :--- | :--- |
| `/sudo` | `command` | Run command as root (installs, etc). | `{"stdout": "root", "exit_code": 0}` |
| `/run_command`| `command` | Execute shell command in `workdir`. | `{"stdout": "...", "exit_code": 0}` |
| `/ps` | None | List top 15 resource-heavy processes. | `{"processes": "PID CMD CPU%..."}` |
| `/kill` | `pid` (int) | Terminate a process by ID. | `{"message": "Process 1234 killed"}` |
| `/whoami` | None | Check which user you are. | `{"user": "ammar"}` |
| `/uptime` | None | Check system uptime. | `{"uptime": "up 3 hours"}` |
| `/git_status` | `directory` | Check git repo status. | `{"git_output": "On branch main..."}` |

### 📁 C. Core Filesystem (Inside `workdir/`)
| Endpoint | Inputs | Description | Example Output |
| :--- | :--- | :--- | :--- |
| `/list` | `directory` | List contents of a folder. | `{"files": ["app.py", "data/"]}` |
| `/read` | `filepath` | Read full text of a file. | `{"content": "..."}` |
| `/write` | `filepath`, `content` | Create/Overwrite file. | `{"message": "Wrote to file.txt"}` |
| `/append` | `filepath`, `content` | Add text to end of file. | `{"message": "Appended"}` |
| `/delete` | `path` | Delete file or folder recursively. | `{"message": "Deleted"}` |
| `/mkdir` | `directory` | Create a new folder. | `{"message": "Directory Created"}` |
| `/copy` | `src`, `dest` | Copy file or folder. | `{"message": "Copied"}` |
| `/rename` | `old`, `new` | Move or rename file/folder. | `{"message": "Renamed"}` |
| `/info` | `path` | Get file size & modified date. | `{"size_bytes": 500, "modified": "..."}` |

### 🔍 D. Data Processing & Search
| Endpoint | Inputs | Description | Example Output |
| :--- | :--- | :--- | :--- |
| `/grep` | `dir`, `search_string` | Search text in all files in a folder. | `{"results": {"f1.txt": ["line 5"]}}` |
| `/regex_search`| `filepath`, `pattern`| Find matches in a file using RegEx. | `{"match_count": 3, "matches": [...]}` |
| `/diff` | `file1`, `file2` | Get unified diff of two files. | `{"diff": "--- a\n+++ b..."}` |
| `/csv_to_json`| `filepath` | Convert CSV file to JSON list. | `{"data": [{"name": "A"}]}` |
| `/json_to_csv`| `json_path`, `out` | Save JSON list as a CSV file. | `{"message": "Converted"}` |

### 📦 E. Archives & Compression
| Endpoint | Inputs | Description | Example Output |
| :--- | :--- | :--- | :--- |
| `/tar` | `path`, `name` | Create a `.tar.gz` of a folder. | `{"message": "Tar created"}` |
| `/untar` | `path`, `dest` | Extract a `.tar.gz` archive. | `{"message": "Untarred"}` |
| `/gzip` | `filepath` | Compress single file to `.gz`. | `{"message": "Compressed"}` |
| `/gunzip` | `filepath` | Decompress `.gz` file. | `{"message": "Extracted"}` |

### 🌐 F. Network Tools
| Endpoint | Inputs | Description | Example Output |
| :--- | :--- | :--- | :--- |
| `/curl` | `url` | Make GET request from host (Proxy). | `{"status": 200, "body": "..."}` |
| `/download_url`| `url`, `save_as` | Download file to `workdir`. | `{"message": "Downloaded"}` |
| `/ip` | None | Get Host's public IP. | `{"public_ip": "1.2.3.4"}` |
| `/ports` | None | List open ports (ss -tuln). | `{"ports": "..."}` |

### 🔐 G. Security & Encoding
| Endpoint | Inputs | Description | Example Output |
| :--- | :--- | :--- | :--- |
| `/hash` | `filepath` | Get SHA256 of a file. | `{"sha256": "..."}` |
| `/md5` | `filepath` | Get MD5 of a file. | `{"md5": "..."}` |
| `/base64_read`| `filepath` | Read file as Base64 string. | `{"base64": "..."}` |
| `/base64_write`| `filepath`, `b64` | Write Base64 string to binary file. | `{"message": "Binary written"}` |

---

## 💡 4. PRO TIPS FOR AI
- **Combine Commands:** Read a file -> Edit it -> Run it -> Check Uptime.
- **Root Tasks:** Use `/sudo` for anything involving `apt`, `systemctl`, or `/etc/`.
- **Large Files:** Use `/split` to break files if they are too big for your context window.
- **Errors:**
    - `401`: Check your `api_key`.
    - `403`: You tried to escape the `workdir/`. Stay in the sandbox!
    - `500`: System error (e.g., file not found or invalid command).
