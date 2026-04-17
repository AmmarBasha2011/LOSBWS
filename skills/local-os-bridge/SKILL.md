---
name: local-os-bridge
description: Control the local Linux machine via a secure FastAPI bridge with 50+ endpoints.
user-invocable: true
---

# Local OS Bridge Skill for OpenClaw

This skill allows OpenClaw to interact with the local operating system through the "Ultimate Local OS Bridge" (FastAPI).

## CRITICAL INSTRUCTION
**You must get the instance link from the user before working because it changes every time the user runs the script.** The link will look like `https://some-name.trycloudflare.com`.

## Authentication
Every request MUST include `api_key=ammar123` as a query parameter.

---

## 1. Core File Operations
| Endpoint | Description | Inputs | Example Output |
| :--- | :--- | :--- | :--- |
| `/list` | List files in a directory | `directory` (default: ".") | `{"files": ["main.py", "README.md"]}` |
| `/read` | Read file content | `filepath` | `{"content": "file text here..."}` |
| `/write` | Overwrite file with content | `filepath`, `content` | `{"message": "Wrote to test.txt"}` |
| `/append` | Add content to end of file | `filepath`, `content` | `{"message": "Appended"}` |
| `/delete` | Delete file or directory | `path` | `{"message": "Deleted"}` |
| `/mkdir` | Create new directory | `directory` | `{"message": "Directory Created"}` |
| `/copy` | Copy file or directory | `source`, `destination` | `{"message": "Copied to backup/"}` |
| `/rename` | Rename/Move file/dir | `old_path`, `new_path` | `{"message": "Renamed"}` |

## 2. Advanced Filesystem
| Endpoint | Description | Inputs | Example Output |
| :--- | :--- | :--- | :--- |
| `/info` | Get file size and modified time | `path` | `{"size_bytes": 1024, "modified": "2026-04-17T..."}` |
| `/find_ext` | Search files by extension | `ext`, `directory` | `{"matches": ["src/app.py", "test.py"]}` |
| `/split` | Split large file into parts | `filepath`, `lines_per_chunk` | `{"chunks_created": ["f.part0", "f.part1"]}` |
| `/merge` | Merge multiple files | `file_paths_comma_sep`, `output_file`| `{"message": "Merged into all.txt"}` |
| `/empty_dir`| Delete all contents in directory | `directory` | `{"message": "Directory emptied..."}` |
| `/symlink` | Create a symbolic link | `target_path`, `link_name` | `{"message": "Symlink created..."}` |

## 3. Data Processing & Search
| Endpoint | Description | Inputs | Example Output |
| :--- | :--- | :--- | :--- |
| `/grep` | Search text in all files in a dir | `directory`, `search_string` | `{"results": {"main.py": ["line 10: ..."]}}` |
| `/regex_search`| Search file with regex pattern | `filepath`, `pattern` | `{"match_count": 5, "matches": ["abc"]}` |
| `/diff` | Compare two files | `file1`, `file2` | `{"diff": "--- file1\n+++ file2..."}` |
| `/csv_to_json`| Convert CSV file to JSON data | `filepath` | `{"data": [{"id": 1, "name": "A"}]}` |
| `/json_to_csv`| Convert JSON list to CSV file | `json_filepath`, `output_csv` | `{"message": "Converted..."}` |

## 4. System & OS Power
| Endpoint | Description | Inputs | Example Output |
| :--- | :--- | :--- | :--- |
| `/run_command`| Execute shell command | `command` | `{"stdout": "output", "exit_code": 0}` |
| `/kill` | Kill process by PID | `pid` | `{"message": "Process 1234 killed..."}` |
| `/whoami` | Get current OS user | None | `{"user": "ammar"}` |
| `/uptime` | Get system uptime | None | `{"uptime": "up 2 hours"}` |
| `/ps` | List top processes | None | `{"processes": "PID CMD..."}` |
| `/git_status`| Get git status of a directory | `directory` | `{"git_output": "On branch main..."}` |

## 5. Network Tools
| Endpoint | Description | Inputs | Example Output |
| :--- | :--- | :--- | :--- |
| `/download_url`| Download file from URL | `url`, `save_as` | `{"message": "Downloaded"}` |
| `/curl` | Make GET request (Host proxy) | `url` | `{"status": 200, "body": "..."}` |
| `/ip` | Get host public IP | None | `{"public_ip": "1.2.3.4"}` |
| `/ports` | List open ports (ss -tuln) | None | `{"ports": "Netid State..."}` |

## 6. Security & Encoding
| Endpoint | Description | Inputs | Example Output |
| :--- | :--- | :--- | :--- |
| `/hash` | Get SHA256 of file | `filepath` | `{"sha256": "abcdef..."}` |
| `/md5` | Get MD5 of file | `filepath` | `{"md5": "123456..."}` |
| `/base64_read`| Read file as Base64 string | `filepath` | `{"base64": "SGVsbG8..."}` |
| `/base64_write`| Write Base64 string to file | `filepath`, `b64_string` | `{"message": "Binary written"}` |

## 7. Archive & Compression
| Endpoint | Description | Inputs | Example Output |
| :--- | :--- | :--- | :--- |
| `/tar` | Create .tar.gz of a folder | `folder_path`, `archive_name` | `{"message": "Tar created"}` |
| `/untar` | Extract .tar.gz archive | `archive_path`, `extract_to` | `{"message": "Untarred"}` |
| `/gzip` | Compress single file to .gz | `filepath` | `{"message": "Compressed to..."}` |
| `/gunzip` | Decompress .gz file | `filepath` | `{"message": "Extracted to..."}` |

---

## Setup Instructions for User
1. Clone repo: `git clone https://github.com/AmmarBasha2011/LOSBWS`
2. Run script: `./run.sh`
3. Wait for the popup window, copy the link, and paste it to OpenClaw.

Visit: https://github.com/AmmarBasha2011/LOSBWS for more info.
