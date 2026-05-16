#!/bin/bash

# Move to the project directory, using quotes for safety
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Ensure log file exists and is writable
touch bridge.log

# --- CHECK FOR VENV ---
if [ ! -d "venv" ]; then
    echo "$(date): Error - Virtual environment not found." >> bridge.log
    exit 1
fi

# --- ACTIVATE VENV & RUN ---
# We run python directly so systemd can track the process
source venv/bin/activate
exec python3 main.py >> bridge.log 2>&1
