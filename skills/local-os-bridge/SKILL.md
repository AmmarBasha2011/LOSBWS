---
name: local-os-bridge
description: Comprehensive OS control for AI. Filesystem, System, Network, and Security tools.
repo: https://github.com/AmmarBasha2011/LOSBWS
user-invocable: true
---

# 🚀 COMPREHENSIVE AI SKILL: Local OS Bridge (V5)

This file is your complete manual. You must use it to understand how to install, authorize, and control the host machine.

## 📥 1. Installation & Synchronization
If you are an AI agent, you must first sync with the official code:
- **Repository:** https://github.com/AmmarBasha2011/LOSBWS
- **Action:** Read `main.py` to understand the logic and `SKILL.md` for the interface.

## 🔐 2. Authorization & Instance Setup
You cannot send requests until the bridge is active on the user's machine.
1.  **Ask the User:** "Please provide the Instance Link from the bridge script's popup."
2.  **Base URL:** Once the user provides the URL (e.g., a `.ngrok-free.dev` link), this is your `BASE_URL`.
3.  **BYPASS NGROK WARNING (CRITICAL):**
    Ngrok free domains display an "Abuse Prevention" warning page by default. To bypass this and reach the JSON API, you **MUST** include the following HTTP Header in every request:
    - **Header Key:** `ngrok-skip-browser-warning`
    - **Header Value:** `any-value-here`
4.  **API Key:** Use the `API_KEY` defined in the user's `.env` (Default: `ammar123`). Every request **MUST** include `api_key={KEY}` in the query parameters.

## 📡 3. Sending Requests
- All endpoints use **HTTP GET**.
- Parameters are passed via **Query Strings**.
- **Sandbox:** All file paths are relative to the `workdir/` folder. You cannot go higher than this directory.
- **Example Fetch:**
  `GET {BASE_URL}/list?api_key=your_key`
  *Headers:* `{"ngrok-skip-browser-warning": "true"}`

---

## 🛠️ 4. API Endpoints Reference

### 📁 CORE FILESYSTEM
| Endpoint | Parameters | Description |
| :--- | :--- | :--- |
| `/list` | `directory` | List files and folders. |
| `/read` | `filepath` | Read file as plain text. |
| `/write` | `filepath`, `content` | Write text to a file (overwrites). |
| `/append`| `filepath`, `content` | Add text to the end of a file. |
| `/delete`| `path` | Delete a file or folder. |
| `/mkdir` | `directory` | Create a new folder. |
| `/copy`  | `source`, `destination`| Copy files or folders. |
| `/rename`| `old_path`, `new_path` | Move or rename files/folders. |

### 🔍 SEARCH & DATA
| Endpoint | Parameters | Description |
| :--- | :--- | :--- |
| `/grep` | `directory`, `search_string` | Find text inside multiple files. |
| `/regex_search`| `filepath`, `pattern` | Search file using RegEx. |
| `/diff` | `file1`, `file2` | Get difference between two files. |
| `/csv_to_json`| `filepath` | Parse CSV file into JSON. |
| `/json_to_csv`| `json_filepath`, `output_csv` | Save JSON list as CSV. |

### ⚡ SYSTEM & POWER
| Endpoint | Parameters | Description |
| :--- | :--- | :--- |
| `/run_command`| `command` | Execute any Linux shell command. |
| `/kill` | `pid` | Stop a running process by ID. |
| `/ps` | None | Get top 15 CPU/RAM processes. |
| `/uptime` | None | Check how long system is running. |
| `/git_status` | `directory` | Check git repository status. |

### 🌐 NETWORK & SECURITY
| Endpoint | Parameters | Description |
| :--- | :--- | :--- |
| `/curl` | `url` | Fetch any URL from the host. |
| `/download_url`| `url`, `save_as` | Download a file to `workdir`. |
| `/ip` | None | Get Host's public IP address. |
| `/hash` | `filepath` | Get SHA256 of a file. |
| `/base64_read`| `filepath` | Read binary file as Base64. |

---

## 📂 5. Archive & Compression
- **`/tar`**: `folder_path`, `archive_name` -> Create `.tar.gz`.
- **`/untar`**: `archive_path`, `extract_to` -> Extract `.tar.gz`.
- **`/gzip`**: `filepath` -> Compress to `.gz`.
- **`/gunzip`**: `filepath` -> Decompress `.gz`.

---

## ⚠️ 6. Error Codes
- **401**: You forgot the `api_key=ammar123`.
- **403**: You tried to access files outside the sandbox.
- **404**: The file or path doesn't exist.

---

## 💡 7. Workflow Example
**User:** "Fix the bug in main.py and test it."
1. `GET /read?filepath=main.py&api_key=ammar123` -> Find bug.
2. `GET /write?filepath=main.py&content=...&api_key=ammar123` -> Fix bug.
3. `GET /run_command?command=python3 main.py&api_key=ammar123` -> Test.
4. `GET /git_status?api_key=ammar123` -> Verify changes.
