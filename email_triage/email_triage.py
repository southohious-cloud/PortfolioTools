import re
from datetime import datetime
from typing import List, Dict


def extract_email_text(raw_input: str) -> str:
    """
    Normalize raw email text by removing signatures, long quoted threads,
    and formatting noise. Returns a cleaned text block.
    """
    cleaned = re.sub(r"(?i)(from:.*?subject:)", "", raw_input, flags=re.DOTALL)
    cleaned = re.sub(r"(?i)(sent from my iphone|best regards|thanks,.*)", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def categorize_email(text: str) -> Dict[str, List[str]]:
    """
    Categorize email content into urgency, waiting, billing, personal,
    and spam indicators. Returns a dictionary of category lists.
    """
    categories = {
        "urgent": [],
        "waiting_on_others": [],
        "bills": [],
        "personal": [],
        "spam": []
    }

    lines = text.split(". ")
    for line in lines:
        lower = line.lower()

        if any(word in lower for word in ["urgent", "asap", "immediately", "deadline"]):
            categories["urgent"].append(line)

        if any(word in lower for word in ["waiting", "follow up", "get back", "pending"]):
            categories["waiting_on_others"].append(line)

        if any(word in lower for word in ["invoice", "receipt", "payment", "bill"]):
            categories["bills"].append(line)

        if any(word in lower for word in ["birthday", "family", "dinner", "personal"]):
            categories["personal"].append(line)

        if any(word in lower for word in ["unsubscribe", "promotion", "limited offer", "sale"]):
            categories["spam"].append(line)

    return categories


def extract_dates(text: str) -> List[str]:
    """
    Extract date-like patterns from the email text. Returns a list of
    detected date strings.
    """
    patterns = [
        r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
        r"\b\d{1,2}-\d{1,2}-\d{2,4}\b",
        r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]* \d{1,2}\b"
    ]
    dates = []
    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        dates.extend(matches)
    return dates


def generate_summary(categories: Dict[str, List[str]], dates: List[str]) -> str:
    """
    Generate a structured triage summary from categorized email content
    and extracted dates. Returns a formatted summary string.
    """
    summary = []
    summary.append("Email Triage Summary\n")

    for section, items in categories.items():
        title = section.replace("_", " ").title()
        summary.append(f"{title}")
        if items:
            for item in items:
                summary.append(f"- {item}")
        else:
            summary.append("- None")
        summary.append("")

    summary.append("Key Dates")
    if dates:
        for d in dates:
            summary.append(f"- {d}")
    else:
        summary.append("- None")

    return "\n".join(summary)


def run_triage(raw_input: str) -> str:
    """
    Execute the full triage pipeline: extract text, categorize content,
    detect dates, and generate a formatted summary.
    """
    cleaned = extract_email_text(raw_input)
    categories = categorize_email(cleaned)
    dates = extract_dates(cleaned)
    return generate_summary(categories, dates)


if __name__ == "__main__":
    sample = input("Paste email text:\n\n")
    print("\n" + run_triage(sample))