## File Cleanup Assistant

A lightweight tool that scans a folder and generates a clear, readable report of digital clutter. It identifies duplicate files, oversized files, old files, and empty folders — without deleting anything.

---

## Purpose

Analyzes a folder to identify duplicates, oversized files, old files, and empty folders.

---

## What It Solves

Prevents cluttered, inconsistent, or bloated folders from slowing down work, wasting storage, or hiding important files.

---

## Features

- **Duplicate Detection**  
  Uses SHA‑256 hashing to identify files with identical content.

- **Large File Finder**  
  Flags files above a configurable size threshold (default: 50 MB).

- **Old File Scanner**  
  Lists files older than a configurable number of days (default: 180 days).

- **Empty Folder Detection**  
  Identifies folders with no files or subfolders.

- **Readable Text Report**  
  Outputs a clean, structured summary.

- **Safe by Design**  
  No files are deleted — this tool only reports.

---

## How It Works

1. Walks the entire directory tree.  
2. Hashes files to detect duplicates.  
3. Compares file sizes to the threshold.  
4. Checks timestamps for old files.  
5. Flags empty folders.  
6. Prints a structured report.

---

## Folder Structure

```
file-cleanup-assistant/
│
├── file_cleanup.py
├── README.md
├── sample_output.txt
└── sample_output_complex.txt
```

---

## How to Use

Run the script:
python file_cleanup.py

Enter the folder path when prompted.

Review the generated report in the terminal.

---

## Sample Outputs

### Standard Sample Output  
A small, easy‑to‑read example demonstrating the basic report format.  
See: `sample_output.txt`

### Complex Sample Output  
A large, enterprise‑scale example showing how the tool handles multi‑year archives, multiple departments, and high‑volume data.  
See: `sample_output_complex.txt`

---

## Future Enhancements

- Optional CSV or JSON export  
- Command‑line arguments for thresholds  
- Ignore‑folder patterns  
- Visual summary (counts, totals, percentages)

---

## Contact

For questions or collaboration, see the main PortfolioTools documentation.
