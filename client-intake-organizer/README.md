# Client Intake Organizer

A simple automation tool that creates a clean, standardized folder structure for new clients. Designed to streamline onboarding and keep project files organized from day one.

---

## Purpose

This tool generates a ready‑to‑use client folder with:

- A normalized folder name  
- A standard subfolder layout  
- A starter README with an intake checklist  

Ideal for onboarding workflows, consulting, project management, and any environment where new client folders are created regularly.

---

## Features

- Normalizes client names (lowercase, underscores, safe characters)  
- Creates a consistent folder structure  
- Generates a starter README/checklist  
- Prevents accidental overwrites if a folder already exists  

---

## Usage

From the PortfolioTools root:

```bash
python client-intake-organizer/intake_organizer.py

you will be prompted for:

The root directory where client folders should be created

The client name

Example:

Input:
Root folder: C:\Users\you\Clients
Client name: John Doe

Output folder structure:
clients/
└── john_doe/
    ├── 01_documents/
    ├── 02_assets/
    ├── 03_notes/
    ├── 04_deliverables/
    └── README.md

Folder Structure
client-intake-organizer/
│
├── intake_organizer.py
├── README.md
└── templates/
    └── intake_readme.md

