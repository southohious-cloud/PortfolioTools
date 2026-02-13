# Daily Automation Runner

This tool exists to give you a simple, reliable way to automate a small daily task. Instead of manually checking a folder or tracking changes over time, it automatically takes a daily snapshot and records what has changed so you can monitor activity without any effort.

The Daily Automation Runner is a lightweight utility that scans a chosen folder once per day and generates a quick snapshot report. It helps you understand how a directory is changing over time without manually comparing files or sizes.

## What the tool does

The script performs one automated action each day:

### 1. Daily Folder Snapshot
Scans a target folder and records the total number of files, the combined folder size, and how many new files appeared since yesterday.
Useful for tracking growth, activity, or changes in any directory over time.

### 2. Daily Logging
Appends a new entry to two logs:
- **automation_log.txt** — human‑friendly summary  
- **automation_log.json** — machine‑friendly structured log  
Great for keeping a clear history of daily folder activity.

### 3. Once‑Per‑Day Enforcement
Ensures the snapshot only runs once per calendar day.
Prevents duplicate runs and keeps the logs clean and predictable.

## How it works

1. You run the script.  
2. The tool checks `last_run.json` to see if today’s snapshot has already been taken.  
3. If not, it scans the target folder and gathers file count and total size.  
4. It compares today’s snapshot to yesterday’s (if available).  
5. It generates two reports:
   - **automation_log.txt** — human‑friendly summary  
   - **automation_log.json** — machine‑friendly structured output  
6. It updates `last_run.json` with today’s snapshot so tomorrow’s comparison works correctly.

All log files are saved in the same directory as the script.