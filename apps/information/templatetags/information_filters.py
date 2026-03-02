import re
from django import template

register = template.Library()


@register.filter
def strip_citations(value):
    """
    Remove Wikipedia-style citation markers like [1], [7], [12] from text.
    Also remove parenthesized pronunciation guides (e.g. IPA or spelled-out).
    """
    if not value or not isinstance(value, str):
        return value
    # Remove citation markers [1], [2], [42], etc.
    text = re.sub(r'\[\d+\]', '', value)
    # Remove multiple spaces left after stripping
    text = re.sub(r'  +', ' ', text)
    # Remove space before punctuation that was left after citation
    text = re.sub(r' \.', '.', text)
    text = re.sub(r' ,', ',', text)
    text = text.strip()
    return text


@register.filter
def clean_wiki_text(value):
    """
    Clean text that may have been copied from Wikipedia:
    - Strip citation markers [1], [7], etc.
    - Remove parenthesized IPA pronunciation ( / ... / ).
    """
    if not value or not isinstance(value, str):
        return value
    # Remove citation markers
    text = re.sub(r'\[\d+\]', '', value)
    # Remove parenthesized IPA pronunciation blocks: ( / ... / ) or ( ... /.../ ... )
    text = re.sub(r'\s*\([^)]*/[^)]*/[^)]*\)', '', text)
    # Normalize whitespace
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r' \.', '.', text)
    text = re.sub(r' ,', ',', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
