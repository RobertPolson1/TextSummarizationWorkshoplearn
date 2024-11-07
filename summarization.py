from gensim.summarization import summarize

def generate_summary(text, ratio=0.2):
    """Generate a summary of the text using Gensim's summarize function."""
    try:
        summary = summarize(text, ratio=ratio)
        return summary
    except ValueError:
        return "Text is too short to summarize."

