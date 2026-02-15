"""
Workflow Snapshot Generator
---------------------------

Generates a structured snapshot of a workflow's current state.
Takes a simple task list (JSON or dict) and produces a readable report.

Core functions:
- load_tasks: read tasks from a JSON file
- group_by_status: organize tasks into status categories
- generate_snapshot: produce a clean text summary
- main: orchestrate the workflow
"""

import json
from pathlib import Path


def load_tasks(path):
    """
    Load tasks from a JSON file.
    Expected format:
    [
        {"task": "Write proposal", "status": "In Progress", "priority": "High"},
        {"task": "Email client", "status": "Not Started"},
        ...
    ]
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def group_by_status(tasks):
    """
    Group tasks into status categories.
    Returns a dict like:
    {
        "Not Started": [...],
        "In Progress": [...],
        "Blocked": [...],
        "Completed": [...]
    }
    """
    categories = {
        "Not Started": [],
        "In Progress": [],
        "Blocked": [],
        "Completed": []
    }

    for task in tasks:
        status = task.get("status", "Not Started")
        if status not in categories:
            categories[status] = []
        categories[status].append(task)

    return categories


def generate_snapshot(grouped):
    """
    Create a clean, readable snapshot report.
    Returns a multi-line string.
    """
    lines = []
    lines.append("WORKFLOW SNAPSHOT")
    lines.append("------------------")
    lines.append("")

    for status, items in grouped.items():
        lines.append(f"{status} ({len(items)})")
        lines.append("-" * len(status))

        if not items:
            lines.append("  • None")
        else:
            for task in items:
                name = task.get("task", "Unnamed Task")
                priority = task.get("priority")
                if priority:
                    lines.append(f"  • {name}  [{priority}]")
                else:
                    lines.append(f"  • {name}")

        lines.append("")

    return "\n".join(lines)


def main():
    """
    Main entry point.
    """
    print("Workflow Snapshot Generator")
    print("---------------------------")

    path = input("Enter path to task JSON file: ").strip()

    try:
        tasks = load_tasks(path)
        grouped = group_by_status(tasks)
        report = generate_snapshot(grouped)
        print("\n" + report)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()