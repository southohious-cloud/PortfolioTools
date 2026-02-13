# Folder Health Check Tool

This tool exists to give you a quick, clear snapshot of what’s inside any folder on your system. Instead of manually digging through files, it automatically identifies duplicates, old files, and large files so you can keep your computer organized and clutter‑free.

The Folder Health Check Tool is a lightweight utility that scans any folder on your system and generates a quick diagnostic report. It helps you understand what’s inside a directory without manually digging through files.

## What the tool does:
The script performs three main checks:

### 1. Duplicate Files
Identifies files that share the same name and size.  
Useful for spotting repeated downloads or copied files.

### 2. Old Files
Flags files older than a chosen number of days (default: 180).  
Great for finding outdated documents, installers, or forgotten exports.

### 3. Large Files
Lists files larger than a chosen size threshold (default: 100 MB).  
Helps you locate space‑heavy items like videos, ZIP archives, or installers.

## How it works

1. You run the script and enter a folder path.  
2. The tool scans the folder and gathers metadata (path, size, modified date).  
3. It runs the three checks listed above.  
4. It generates two reports:  
   - **health_report.txt** — human‑friendly summary  
   - **health_report.json** — machine‑friendly structured output  

Both reports are saved in the same directory as the script.