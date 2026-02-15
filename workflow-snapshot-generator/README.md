# Workflow Snapshot Generator

A lightweight utility that produces a clean, structured snapshot of a workflow’s current state. It reads a simple task list (JSON) and generates a readable report showing what’s Not Started, In Progress, Blocked, and Completed. This tool is designed for quick standups, client updates, project check‑ins, and documenting workflow state before handoff.

---

## Purpose

Creates a clear, at‑a‑glance summary of a workflow’s current status using a simple, predictable input format.

---

## What It Solves

Provides a fast, consistent way to understand:

- what work has started  
- what is blocked  
- what is complete  
- what still needs attention  

This eliminates ambiguity and supports clean communication with clients and teams.

---

## Features

- **Task Loading**  
  Reads tasks from a JSON file with fields like `task`, `status`, and `priority`.

- **Status Grouping**  
  Automatically organizes tasks into Not Started, In Progress, Blocked, and Completed.

- **Priority Awareness**  
  Displays optional priority tags when provided.

- **Readable Snapshot Report**  
  Produces a clean text summary suitable for sharing, printing, or saving.

- **Simple, Predictable Design**  
  Uses only Python’s standard library and follows the same modular structure as the rest of the suite.

---

## How It Works

1. Loads tasks from a JSON file.  
2. Groups tasks by status.  
3. Formats the grouped tasks into a structured snapshot.  
4. Prints the final report to the console.

---

## Folder Structure
workflow-snapshot-generator/ │ ├── workflow_snapshot.py ├── README.md ├── sample_input.json └── sample_output.txt

---

## How to Use

Run the script:
python workflow_snapshot.py

Enter the path to a JSON file containing tasks.

A snapshot report will be printed to the terminal.

---

## Sample Input

See: `sample_input.json`

---

## Sample Output

See: `sample_output.txt`

---

## Future Enhancements

- Optional CSV export  
- Additional status categories  
- Timestamp support  
- CLI flags for input/output paths  

---

## Contact

For questions or collaboration, see the main PortfolioTools documentation.