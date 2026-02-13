import os
import time
import json

def scan_folder(path):
    """Scan a folder and return file metadata.

    Returns a dictionary in the form:
    {
        "filename.ext": {
            "path": "/full/path/to/file",
            "size": 123456,
            "modified": 1707700000.0
        },
        ...
    }
    """
    file_data = {}

    if not os.path.exists(path):
        raise FileNotFoundError(f"Path does not exist: {path}")

    if not os.path.isdir(path):
        raise NotADirectoryError(f"Not a directory: {path}")

    for root, _, files in os.walk(path):
        for filename in files:
            full_path = os.path.join(root, filename)

            try:
                size = os.path.getsize(full_path)
                modified = os.path.getmtime(full_path)
            except OSError:
                continue

            file_data[filename] = {
                "path": full_path,
                "size": size,
                "modified": modified
            }

    return file_data


def find_duplicates(file_data):
    """Return a list of duplicate filenames based on name and size."""
    seen = {}
    duplicates = []

    for filename, info in file_data.items():
        key = (filename, info["size"])

        if key in seen:
            duplicates.append(filename)
        else:
            seen[key] = info["path"]

    return duplicates


def find_old_files(file_data, days=180):
    """Return a list of files older than the given number of days."""
    old_files = []
    cutoff = time.time() - (days * 86400)

    for filename, info in file_data.items():
        if info["modified"] < cutoff:
            old_files.append(filename)

    return old_files


def find_large_files(file_data, size_mb=100):
    """Return a list of large files above the given size threshold."""
    large_files = []
    threshold_bytes = size_mb * 1024 * 1024

    for filename, info in file_data.items():
        if info["size"] > threshold_bytes:
            large_files.append({
                "name": filename,
                "size_mb": round(info["size"] / (1024 * 1024), 2)
            })

    return large_files


def generate_text_report(results):
    """Return a human-readable text report."""
    lines = []
    lines.append("Folder Health Check Report")
    lines.append("---------------------------")

    lines.append("\nDuplicates:")
    if results["duplicates"]:
        for item in results["duplicates"]:
            lines.append(f" - {item}")
    else:
        lines.append(" None")

    lines.append("\nOld Files:")
    if results["old_files"]:
        for item in results["old_files"]:
            lines.append(f" - {item}")
    else:
        lines.append(" None")

    lines.append("\nLarge Files:")
    if results["large_files"]:
        for item in results["large_files"]:
            lines.append(f" - {item['name']} ({item['size_mb']} MB)")
    else:
        lines.append(" None")

    return "\n".join(lines)


def generate_json_report(results):
    """Return a JSON-serializable dictionary."""
    return results


def main():
    """Orchestrate the folder health check."""
    folder = input("Enter the folder path to scan: ").strip()

    file_data = scan_folder(folder)

    duplicates = find_duplicates(file_data)
    old_files = find_old_files(file_data)
    large_files = find_large_files(file_data)

    results = {
        "duplicates": duplicates,
        "old_files": old_files,
        "large_files": large_files
    }

    text_report = generate_text_report(results)
    json_report = generate_json_report(results)

    with open("health_report.txt", "w") as f:
        f.write(text_report)

    with open("health_report.json", "w") as f:
        json.dump(json_report, f, indent=4)

    print("\nReports generated:")
    print(" - health_report.txt")
    print(" - health_report.json")


if __name__ == "__main__":
    main()