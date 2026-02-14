# Task Extractor

## Overview
Task Extractor analyzes any block of text—emails, meeting notes, summaries, client messages—and identifies actionable tasks. It returns structured fields including description, owner, deadline, and priority.

## Features
- Detects task-like lines automatically
- Extracts owners (e.g., “for John”)
- Extracts deadlines (e.g., “by Friday”)
- Detects priority indicators (high, medium, low)
- Outputs a clean, structured list

## How to Run
python task_extractor.py

Paste text when prompted, then press Enter twice.

## Output Format
Each task is returned as:
{ "description": "...", "owner": "...", "deadline": "...", "priority": "...", "notes": None }

## Use Cases
- Email triage follow-up extraction  
- Meeting notes cleanup  
- Client intake processing  
- Document summarization post-processing  