# File Name Standardizer

A lightweight tool that cleans and standardizes file names in a folder. Designed to reduce clutter, enforce
consistent naming, and make folders easier to scan and maintain.

---

## Purpose

The File Name Standardizer takes a target folder and applies a consistent naming scheme to all files:

- Normalizes case  
- Replaces spaces with underscores  
- Removes problematic characters  
- Applies an optional prefix  
- Avoids name collisions safely  

This tool is ideal for client folders, shared drives, and any workflow that benefits from predictable file names.

---

## Features

- Converts file names to lowercase  
- Replaces spaces with underscores  
- Strips unsafe/special characters  
- Preserves file extensions  
- Adds an optional prefix to all files  
- Prevents collisions by auto‑incrementing duplicates  
- Supports dry‑run mode for safe preview  

---

## Usage

From the PortfolioTools root:

```bash
python file-name-standardizer/file_name_standardizer.py

Or from inside the tool folder:
cd file-name-standardizer
python file_name_standardizer.py

You will be prompted for:
• 	The target folder path
• 	An optional prefix (or leave blank)
• 	Whether to run in dry‑run mode or apply changes

Example
Input folder:
• 	Final Report V2.DOCX
• 	Client Notes (John).txt
• 	Screenshot 2026-02-13 10.15.22.png
With prefix: clientA_
Output:
• 	clienta_final_report_v2.docx
• 	clienta_client_notes_john.txt
• 	clienta_screenshot_2026-02-13_10_15_22.png

Folder Structure
file-name-standardizer/
│
├── file_name_standardizer.py
├── README.md
└── samples/
    └── sample_files.txt
    