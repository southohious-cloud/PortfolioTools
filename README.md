# PortfolioTools

A curated collection of small, focused Python utilities designed for clean structure, predictable behavior, and practical workflow automation. Each tool solves a real‑world problem in a simple, reliable way and produces output that is both human‑friendly and machine‑friendly.

Every tool lives in its own folder with:

- its own README  
- a single, well‑structured Python script  
- consistent naming and design philosophy  

This keeps the suite easy to explore, extend, and integrate into larger systems.

---

## Included Tools

### 1. Folder Health Check
Analyzes a target directory and produces a structured report including:

- total file count  
- total size  
- largest files  
- extension breakdown  

Useful for audits, cleanup workflows, and automated monitoring.

**Folder:** [folder-health-check](folder-health-check/)

---

### 2. Document Summarizer
Reads a text‑based document and generates a concise, structured summary. Ideal for:

- meeting notes  
- research documents  
- long‑form text you need to understand quickly  

Outputs are formatted for readability and downstream automation.

**Folder:** [document-summarizer](document-summarizer/)

---

### 3. Daily Automation Runner
Runs daily tasks in a predictable sequence. Designed for:

- scheduled maintenance  
- routine checks  
- multi‑step workflows  

The runner is intentionally minimal so it can be extended or integrated into larger systems.

**Folder:** [daily-automation-runner](daily-automation-runner/)

---

### 4. File Name Standardizer

Cleans and normalizes filenames in a target directory using consistent, automation-friendly rules. Includes:

- removal of problematic characters  
- consistent spacing and casing  
- predictable, clean output for downstream tools  

Useful for organizing messy folders and preparing files for automated workflows.

**Folder:** [filename-standardizer](filename-standardizer/)

---

### 5. Email Triage

Processes exported or text-based emails and produces structured categories including:

- actionable items  
- follow-ups  
- informational messages  
- low-priority or ignorable content  

Helps reduce inbox noise and supports faster decision-making.

**Folder:** [email-triage](email-triage/)

---

### 6. Client Intake Organizer

Creates a standardized client folder structure including:

- normalized client folder name  
- subfolders for documents, assets, notes, and deliverables  
- an auto-generated README with an intake checklist  

Ideal for consistent onboarding workflows and organized client management.

**Folder:** [client-intake-organizer](client-intake-organizer/)

---

### 7. Task Extractor

Extracts actionable tasks from unstructured text, including:

- meeting notes  
- client messages  
- long documents  
- any raw text that needs to be converted into clear next steps  

Ideal for turning messy input into a clean, structured task list ready for planning or automation.


**Folder:** [task-extractor](task-extractor/)

---
### Future Additions

This suite is designed to grow. Planned expansions include:

- additional workflow utilities  
- more automation runners  
- extended reporting formats  
- optional CLI wrappers  
