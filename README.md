# PortfolioTools

A curated collection of small, focused Python utilities designed for clean structure, predictable behavior, and practical workflow automation. Each tool solves a real‑world problem in a simple, reliable way and produces output that is both human‑friendly and machine‑friendly.

Every tool lives in its own folder with:

- its own README  
- a single, well‑structured Python script  
- consistent naming and design philosophy  

This keeps the suite easy to explore, extend, and integrate into larger systems.

---

## Table of Contents

- [Included Tools](#included-tools)

- [Workflow Integration Examples](#workflow-integration-examples)
  - [Full Workflow Diagram](#full-workflow-diagram)

- [Future Additions](#future-additions)

---

# Included Tools

- [Folder Health Check](#folder-health-check)

- [Document Summarizer](#document-summarizer)

- [Daily Automation Runner](#daily-automation-runner)

- [File Name Standardizer](#file-name-standardizer)

- [Email Triage Assistant](#email-triage-assistant)

- [Client Intake Organizer](#client-intake-organizer)

- [Task Extractor](#task-extractor)

---

## Folder Health Check
**1. Folder Health Check**

Analyzes a target directory and produces a structured report including:

- total file count  
- total size  
- largest files  
- extension breakdown  

Useful for audits, cleanup workflows, and automated monitoring.

**Folder:** [folder-health-check](folder-health-check/)

---

## Document Summarizer
**2. Document Summarizer**
Reads a text‑based document and generates a concise, structured summary. Ideal for:

- meeting notes  
- research documents  
- long‑form text you need to understand quickly  

Outputs are formatted for readability and downstream automation.

**Folder:** [document-summarizer](document-summarizer/)

---

## Daily Automation Runner
**3. Daily Automation Runner**
Runs daily tasks in a predictable sequence. Designed for:

- scheduled maintenance  
- routine checks  
- multi‑step workflows  

The runner is intentionally minimal so it can be extended or integrated into larger systems.

**Folder:** [daily-automation-runner](daily-automation-runner/)

---

## File Name Standardizer
**4. File Name Standardizer**

Cleans and normalizes filenames in a target directory using consistent, automation-friendly rules. Includes:

- removal of problematic characters  
- consistent spacing and casing  
- predictable, clean output for downstream tools  

Useful for organizing messy folders and preparing files for automated workflows.

**Folder:** [filename-standardizer](filename-standardizer/)

---

## Email Triage Assistant
**5. Email Triage Assistant**

Processes exported or text-based emails and produces structured categories including:

- actionable items  
- follow-ups  
- informational messages  
- low-priority or ignorable content  

Helps reduce inbox noise and supports faster decision-making.

**Folder:** [email-triage](email-triage/)

---

## Client Intake Organizer
**6. Client Intake Organizer**

Creates a standardized client folder structure including:

- normalized client folder name  
- subfolders for documents, assets, notes, and deliverables  
- an auto-generated README with an intake checklist  

Ideal for consistent onboarding workflows and organized client management.

**Folder:** [client-intake-organizer](client-intake-organizer/)

---

## Task Extractor
**7. Task Extractor**

Extracts actionable tasks from unstructured text, including:

- meeting notes  
- client messages  
- long documents  
- any raw text that needs to be converted into clear next steps  

Ideal for turning messy input into a clean, structured task list ready for planning or automation.


**Folder:** [task-extractor](task-extractor/)


---

## Workflow Integration Examples

Below are six modular workflow examples that demonstrate how the tools in this project can be combined into lightweight, repeatable systems. Each example shows how individual tools can operate independently or connect into a larger workflow.

---

### 1. Intake → File Name Standardizer  
**Use case:** A client uploads documents with inconsistent names.

**Flow:**
- Intake form receives files  
- Files pass through the Standardizer  
- Output is a clean, consistent set of names ready for storage or processing  

**Value:** Reduces chaos, prevents duplicates, and creates predictable structure.

---

### 2. Document Summarizer → Email Triage Assistant  
**Use case:** A client receives long attachments and needs quick decisions.

**Flow:**
- Summarizer extracts key points  
- Triage Assistant generates action options (reply, delegate, archive, follow‑up)  

**Value:** Faster decisions, less cognitive load, clearer next steps.

---

### 3. Folder Health Check → File Name Standardizer  
**Use case:** A messy folder needs cleanup and consistency.

**Flow:**
- Health Check identifies issues (duplicates, missing extensions, inconsistent patterns)  
- Standardizer applies naming rules to fix inconsistencies  

**Value:** A clean, predictable workspace with minimal manual effort.

---

### 4. Intake → Workflow Map Routing  
**Use case:** A client wants tasks automatically sorted into the correct lane.

**Flow:**
- Intake captures request details  
- Classification assigns the correct lane (A/B/C/D)  
- Optional automations trigger based on lane  

**Value:** Zero ambiguity — every task starts in the right place.

---

### 5. Summarizer → Output Layer Templates  
**Use case:** Turning raw content into polished deliverables.

**Flow:**
- Summarizer extracts the core content  
- Output Layer applies formatting rules and templates  

**Value:** Faster production of clean, client‑ready documents.

---

### 6. Multi‑Tool Mini Workflow (Premium Example)  
**Use case:** A client wants a repeatable, semi‑automated content pipeline.

**Flow:**
- Intake receives topic or request  
- Classification routes to Content Lane  
- Summarizer processes research  
- Output Layer formats the final draft  

**Value:** A lightweight, scalable system that feels like a custom internal workflow.

A full **stacked‑vertical workflow diagram** is also included to visually summarize all six integrations on a single page.

### Full Workflow Diagram

```

Workflow Integration — Full Vertical Diagram (Examples 1–6)

┌────────────┐
│ Intake     │
└─────┬──────┘
      ▼
┌────────────────────────┐
│ File Name Standardizer │ (Example 1 & 3)
└─────┬──────────────────┘
      ▼
┌──────────────────────────┐
│ Document Summarizer      │ (Example 2 & 5)
└─────┬────────────────────┘
      ▼
┌──────────────────────────┐
│ Email Triage Assistant   │ (Example 2)
└─────┬────────────────────┘
      ▼
┌──────────────────────────┐
│ Workflow Map Routing     │ (Example 4)
└─────┬────────────────────┘
      ▼
┌──────────────────────────┐
│ Output Layer Templates   │ (Example 5 & 6)
└─────┬────────────────────┘
      ▼
┌───────────────┐
│ Final Output   │
└───────────────┘

```

These examples are part of the client‑facing binder and help illustrate how PortfolioTools can scale from simple utilities to complete workflow systems.

---

### Future Additions

This suite is designed to grow. Planned expansions include:

- additional workflow utilities  
- more automation runners  
- extended reporting formats  
- optional CLI wrappers  
