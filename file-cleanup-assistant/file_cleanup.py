import os
import hashlib
import time
from datetime import datetime, timedelta

def hash_file(path):
    """Return SHA256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def find_duplicates(root):
    """Return dict of hash -> list of file paths."""
    hashes = {}
    for folder, _, files in os.walk(root):
        for name in files:
            path = os.path.join(folder, name)
            file_hash = hash_file(path)
            if not file_hash:
                continue
            hashes.setdefault(file_hash, []).append(path)
    return {h: p for h, p in hashes.items() if len(p) > 1}

def find_large_files(root, size_mb=50):
    """Return list of files larger than size_mb."""
    large = []
    threshold = size_mb * 1024 * 1024
    for folder, _, files in os.walk(root):
        for name in files:
            path = os.path.join(folder, name)
            if os.path.getsize(path) >= threshold:
                large.append(path)
    return large

def find_old_files(root, days=180):
    """Return list of files older than N days."""
    old = []
    cutoff = time.time() - (days * 86400)
    for folder, _, files in os.walk(root):
        for name in files:
            path = os.path.join(folder, name)
            if os.path.getmtime(path) < cutoff:
                old.append(path)
    return old

def find_empty_folders(root):
    """Return list of empty folders."""
    empty = []
    for folder, subfolders, files in os.walk(root):
        if not subfolders and not files:
            empty.append(folder)
    return empty

def generate_report(root):
    """Generate a cleanup report for the folder."""
    duplicates = find_duplicates(root)
    large_files = find_large_files(root)
    old_files = find_old_files(root)
    empty_folders = find_empty_folders(root)

    report = []
    report.append(f"FILE CLEANUP REPORT — {root}")
    report.append("=" * 60)

    report.append("\nDUPLICATE FILES:")
    if duplicates:
        for h, paths in duplicates.items():
            report.append(f"\nHash: {h}")
            for p in paths:
                report.append(f"  - {p}")
    else:
        report.append("  None found.")

    report.append("\nLARGE FILES (>50MB):")
    report.extend([f"  - {p}" for p in large_files] or ["  None found."])

    report.append("\nOLD FILES (>180 days):")
    report.extend([f"  - {p}" for p in old_files] or ["  None found."])

    report.append("\nEMPTY FOLDERS:")
    report.extend([f"  - {p}" for p in empty_folders] or ["  None found."])

    return "\n".join(report)

if __name__ == "__main__":
    folder = input("Enter folder path to scan: ").strip()
    print("\nScanning... please wait.\n")
    print(generate_report(folder))