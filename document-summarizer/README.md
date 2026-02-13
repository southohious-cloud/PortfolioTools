# Document Summarizer Tool

This tool exists to give you a quick, clear understanding of any text you provide. Instead of manually reading through long passages, it automatically generates short, medium, or detailed summaries so you can grasp the main ideas instantly.

The Document Summarizer Tool is a lightweight utility that analyzes text, ranks its most meaningful sentences, and produces a concise summary along with optional keyword extraction.

## What the tool does

The script performs two main tasks:

### 1. Text Summarization
Generates short, medium, or detailed summaries based on sentence scoring.  
Useful for quickly understanding long passages, articles, or documents.

### 2. Keyword Extraction
Identifies the most frequent meaningful words (4+ letters).  
Helps highlight the core topics or themes of the text.

It produces two reports:

- **summary_report.txt** — human‑friendly summary  
- **summary_report.json** — machine‑friendly structured output  

Both reports are saved in the same directory as the script.

## How it works

1. You run the script and choose how to provide text (`file` or `text`).  
2. The tool loads the text and splits it into sentences.  
3. It scores each sentence based on word frequency.  
4. It selects the top sentences depending on the chosen summary level.  
5. It optionally extracts keywords.  
6. It generates two reports (text + JSON).