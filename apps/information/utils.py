import re


def clean_wiki_text(value):
    """
    Clean text that may have been copied from Wikipedia:
    - Strip all citation markers [1], [7], [48][49], etc.
    - Remove parenthesized pronunciation guides (e.g. (/'i:lpn/EE-lon;) or IPA).
    - Normalize whitespace.
    """
    if not value or not isinstance(value, str):
        return value
    # Remove all citation markers like [6], [7], [48], [49] (every [digits] in the text)
    text = re.sub(r'\[\d+\]', '', value)
    # Remove parenthesized pronunciation: ( ... /... ) or ( /.../ ... ) — at least one slash inside parens
    text = re.sub(r'\s*\([^)]*/[^)]*\)', '', text)
    # Remove any remaining parentheses that look like pronunciation (e.g. (EE-lon) after slash removal)
    # Only remove if it's a short fragment that's likely pronunciation, e.g. (US: ...) or (UK: ...)
    text = re.sub(r'\s*\((?:US|UK):[^)]*\)', '', text)
    # Grammar: "He is most [adj] profession was" -> "His most [adj] profession was"
    text = re.sub(r'\bHe is most (\w+) profession (was|were)\b', r'His most \1 profession \2', text, flags=re.IGNORECASE)
    # Grammar: "He is most [adj] career was" -> "His most [adj] career was"
    text = re.sub(r'\bHe is most (\w+) career (was|were)\b', r'His most \1 career \2', text, flags=re.IGNORECASE)
    # Grammar: "She is most [adj] profession was" -> "Her most [adj] profession was"
    text = re.sub(r'\bShe is most (\w+) profession (was|were)\b', r'Her most \1 profession \2', text, flags=re.IGNORECASE)
    # Grammar: "She is most [adj] career was" -> "Her most [adj] career was"
    text = re.sub(r'\bShe is most (\w+) career (was|were)\b', r'Her most \1 career \2', text, flags=re.IGNORECASE)
    # Grammar: "He is best known profession was" -> "His best known profession was"
    text = re.sub(r'\bHe is best known profession (was|were)\b', r'His best known profession \1', text, flags=re.IGNORECASE)
    # Grammar: "She is best known profession was" -> "Her best known profession was"
    text = re.sub(r'\bShe is best known profession (was|were)\b', r'Her best known profession \1', text, flags=re.IGNORECASE)
    # Grammar: "He is best known career was" -> "His best known career was"
    text = re.sub(r'\bHe is best known career (was|were)\b', r'His best known career \1', text, flags=re.IGNORECASE)
    # Grammar: "She is best known career was" -> "Her best known career was"
    text = re.sub(r'\bShe is best known career (was|were)\b', r'Her best known career \1', text, flags=re.IGNORECASE)
    # Normalize whitespace
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r' \.', '.', text)
    text = re.sub(r' ,', ',', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
