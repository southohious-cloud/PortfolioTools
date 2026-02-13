# Email Triage Assistant

A lightweight tool that transforms messy email text into a clean, structured triage summary. Designed for clarity, speed, and real‑world workflow support.

---

## Purpose

The Email Triage Assistant analyzes raw email content and produces a categorized summary:

- **Urgent**
- **Waiting on Others**
- **Bills / Receipts**
- **Personal**
- **Spam / Low Priority**
- **Key Dates**

This tool reduces inbox stress and provides instant clarity.

---

## Features

- Normalizes messy email threads
- Detects urgency indicators
- Identifies billing and personal content
- Flags spam‑like language
- Extracts dates and deadlines
- Outputs a clean, client‑friendly summary

---

## Usage

Run the tool from the PortfolioTools root:
python email_triage/email_triage.py

Or run it from inside the tool folder:
cd email_triage python email_triage.py

Paste any email or thread when prompted.

---

## Output Example
Email Triage Summary
Urgent
• 	Please send this ASAP
Waiting On Others
• 	None
Bills
• 	Invoice attached for last month
Personal
• 	None
Spam
• 	None
Key Dates
• 	02/14/2026

---

## Folder Structure
EmailTriageAssistant/ │ ├── email_triage.py ├── README.md └── samples/ └── sample_email.txt

---

## Sample Input

See `samples/sample_email.txt` for a realistic example.