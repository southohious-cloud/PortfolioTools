import re

def extract_tasks(text):
    """
    Extract structured tasks from raw text.

    Args:
        text (str): Input text containing tasks, notes, or instructions.

    Returns:
        list: A list of dictionaries, each representing a task with:
            - description (str)
            - owner (str or None)
            - deadline (str or None)
            - priority (str or None)
            - notes (str or None)
    """
    lines = text.splitlines()
    tasks = []

    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue

        if cleaned.startswith(("-", "*", "•")) or re.search(r"\b(todo|task|action)\b", cleaned, re.IGNORECASE):
            task = {
                "description": cleaned,
                "owner": extract_owner(cleaned),
                "deadline": extract_deadline(cleaned),
                "priority": extract_priority(cleaned),
                "notes": None
            }
            tasks.append(task)

    return tasks


def extract_owner(text):
    """
    Identify the owner of a task if present.
    """
    match = re.search(r"\bfor\s+([A-Z][a-z]+)\b", text)
    return match.group(1) if match else None


def extract_deadline(text):
    """
    Identify a deadline if present.
    """
    match = re.search(r"\bby\s+([A-Za-z0-9 ,/-]+)\b", text)
    return match.group(1) if match else None


def extract_priority(text):
    """
    Identify priority indicators.
    """
    if re.search(r"\b(high|urgent|asap)\b", text, re.IGNORECASE):
        return "high"
    if re.search(r"\b(medium|normal)\b", text, re.IGNORECASE):
        return "medium"
    if re.search(r"\b(low|later)\b", text, re.IGNORECASE):
        return "low"
    return None


def main():
    """
    Command-line entry point for extracting tasks.
    """
    print("Paste text to extract tasks. Press Enter twice to finish.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    tasks = extract_tasks(text)

    print("\nExtracted Tasks:\n")
    for t in tasks:
        print(f"- {t['description']}")
        print(f"  Owner: {t['owner']}")
        print(f  Deadline: {t['deadline']}")
        print(f"  Priority: {t['priority']}")
        print()