import os
import json
from datetime import datetime
from pathlib import Path

def load_last_run(path):
    """Load last run data from JSON file."""
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_last_run(path, data):
    """Save last run data to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def scan_folder(folder):
    """Scan folder and return file count and total size in MB."""
    total_size = 0
    file_count = 0
    for root, _, files in os.walk(folder):
        for file in files:
            file_count += 1
            fp = Path(root) / file
            total_size += fp.stat().st_size
    return file_count, round(total_size / (1024 * 1024), 2)

def append_text_log(path, entry):
    """Append a human-friendly log entry."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def append_json_log(path, data):
    """Append a machine-friendly JSON log entry."""
    logs = []
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            logs = json.load(f)
    logs.append(data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

def run_daily_snapshot(folder):
    """Run the daily folder snapshot task."""
    folder = Path(folder)
    last_run_path = Path("last_run.json")
    text_log_path = Path("automation_log.txt")
    json_log_path = Path("automation_log.json")

    today = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M")

    last_run = load_last_run(last_run_path)
    if last_run and last_run.get("last_run_date") == today:
        return "Snapshot already taken today."

    file_count, total_size = scan_folder(folder)

    new_files = None
    if last_run and "last_snapshot" in last_run:
        prev = last_run["last_snapshot"]
        new_files = file_count - prev.get("files", 0)

    text_entry = (
        f"{today} {now_time} — Snapshot taken. "
        f"Files: {file_count} "
        f"Total size: {total_size} MB"
        + (f" New files: {new_files}" if new_files is not None else "")
    )

    append_text_log(text_log_path, text_entry)

    json_entry = {
        "date": today,
        "time": now_time,
        "files": file_count,
        "total_size_mb": total_size,
        "new_files": new_files,
        "status": "success"
    }

    append_json_log(json_log_path, json_entry)

    save_last_run(last_run_path, {
        "last_run_date": today,
        "last_snapshot": {
            "files": file_count,
            "total_size_mb": total_size
        }
    })

    return "Daily snapshot completed."

if __name__ == "__main__":
    target_folder = Path(".")
    print(run_daily_snapshot(target_folder))