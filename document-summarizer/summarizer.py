import re

def split_sentences(text):
    """Split text into sentences using simple punctuation rules."""
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    return [s.strip() for s in sentences if s.strip()]

def score_sentences(sentences):
    """Score sentences based on word frequency."""
    word_freq = {}
    for sentence in sentences:
        for word in sentence.lower().split():
            word = re.sub(r'[^a-z0-9]', '', word)
            if len(word) > 3:
                word_freq[word] = word_freq.get(word, 0) + 1

    scores = []
    for sentence in sentences:
        score = 0
        for word in sentence.lower().split():
            word = re.sub(r'[^a-z0-9]', '', word)
            score += word_freq.get(word, 0)
        scores.append((sentence, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores

def load_text(path=None, text=None):
    """Load text from a file path or direct input."""
    if path:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
    if text:
        return text.strip()
    raise ValueError("No text or file path provided.")

def summarize_short(text):
    """Return a short 1–2 sentence summary."""
    sentences = split_sentences(text)
    if not sentences:
        return "No content to summarize."

    ranked = score_sentences(sentences)
    top = [s for s, _ in ranked[:2]]
    return " ".join(top)

def summarize_medium(text):
    """Return a medium-length paragraph summary."""
    sentences = split_sentences(text)
    if not sentences:
        return "No content to summarize."

    ranked = score_sentences(sentences)
    top = [s for s, _ in ranked[:4]]
    return " ".join(top)

def summarize_detailed(text):
    """Return a detailed multi-point summary."""
    sentences = split_sentences(text)
    if not sentences:
        return "No content to summarize."

    ranked = score_sentences(sentences)
    top = [s for s, _ in ranked[:6]]

    bullet_points = [f"- {s}" for s in top]
    return "\n".join(bullet_points)

def extract_keywords(text, num=5):
    """Return a list of keywords based on frequency."""
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    freq = {}

    for w in words:
        freq[w] = freq.get(w, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:num]]

def generate_text_output(summary, keywords=None):
    """Return a clean text report."""
    lines = []
    lines.append("Document Summary Report")
    lines.append("-----------------------")
    lines.append("")
    lines.append("Summary:")
    lines.append(summary)
    lines.append("")

    if keywords:
        lines.append("Keywords:")
        for kw in keywords:
            lines.append(f" - {kw}")
        lines.append("")

    return "\n".join(lines)

def generate_json_output(summary, keywords=None):
    """Return a JSON-serializable dictionary."""
    return {
        "summary": summary,
        "keywords": keywords or []
    }

def main():
    """Orchestrate the document summarizer."""
    print("Document Summarizer Tool")
    print("------------------------")
    print("Choose how you want to provide text:")
    print("  - Type 'file' to load a .txt file")
    print("  - Type 'text' to paste text directly")

    mode = input("Enter 'file' or 'text': ").strip().lower()

    if mode == "file":
        path = input("Enter the file path: ").strip()
        try:
            text = load_text(path=path)
        except FileNotFoundError as e:
            print(str(e))
            return
    elif mode == "text":
        print("Paste your text below. Press Enter when done:")
        text = load_text(text=input())
    else:
        print("Invalid mode.")
        return

    # Prevent empty input from continuing
    if not text.strip():
        print("No text provided. Exiting.")
        return

    level = input("Choose summary level (short, medium, detailed): ").strip().lower()

    if level == "short":
        summary = summarize_short(text)
    elif level == "medium":
        summary = summarize_medium(text)
    elif level == "detailed":
        summary = summarize_detailed(text)
    else:
        print("Invalid summary level.")
        return

    include_keywords = input("Extract keywords? (y/n): ").strip().lower() == "y"
    keywords = extract_keywords(text) if include_keywords else None

    text_output = generate_text_output(summary, keywords)
    json_output = generate_json_output(summary, keywords)

    with open("summary_report.txt", "w", encoding="utf-8") as f:
        f.write(text_output)

    with open("summary_report.json", "w", encoding="utf-8") as f:
        import json
        json.dump(json_output, f, indent=4)

    print("\nSummary complete.")
    print("Reports saved in the current folder:")
    print("  • summary_report.txt")
    print("  • summary_report.json")

if __name__ == "__main__":
    main()