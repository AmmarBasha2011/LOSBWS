# Ultimate Local OS Bridge (V5 RAT)

The most advanced API for AI to control a Linux machine safely with 50+ endpoints.

## Features
- **File Operations:** List, read, write, append, delete, mkdir, copy, rename.
- **Advanced Filesystem:** Info, find by extension, split, merge, symlink, empty directory.
- **Data Processing:** Grep search, regex search, file diff, CSV to JSON, JSON to CSV.
- **System Control:** Run commands, kill processes, whoami, uptime, process list, git status.
- **Network Tools:** Download from URL, curl proxy, public IP fetch, open ports check.
- **Security:** SHA256/MD5 hashing, Base64 read/write.
- **Compression:** Tar, untar, gzip, gunzip.

## Quick Start
1. **Clone the project:**
   ```bash
   git clone https://github.com/AmmarBasha2011/LOSBWS
   cd LOSBWS
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```
4. **Copy the Public URL:** The script will automatically start a Cloudflare tunnel and print a public link.

## API Documentation (Swagger)
Once the script is running, visit:
`{PUBLIC_URL}/docs`

## AI Skill for OpenClaw
This project includes an OpenClaw-optimized skill located in `skills/local-os-bridge/`. 

**Prompt to install this skill in OpenClaw:**
> "Please install the 'local-os-bridge' skill. You can find the instructions in the `skills/local-os-bridge/SKILL.md` file. Remember that you must get the instance link from me after I run the script, as it changes every time."

## Security Notice
- The API is protected by an API Key (`api_key=ammar123` by default).
- The `BASE_DIR` is set to `workdir/` to prevent directory traversal attacks.

## GitHub Repository
[https://github.com/AmmarBasha2011/LOSBWS](https://github.com/AmmarBasha2011/LOSBWS)
