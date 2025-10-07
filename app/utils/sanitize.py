import re
import html
import unicodedata
import bleach

# Allowed tags/attributes (adjust depending on your needs)
ALLOWED_TAGS = []  # no HTML allowed at all (safest)
ALLOWED_ATTRS = {}  # empty = disallow all attributes


def sanitize_string(value: str) -> str | None:
    """
    Args:
        value (str): The input string to sanitize.


    Returns:
        str: A cleaned, safe string.
    """
    if value is None:
        return None

    cleaned = unicodedata.normalize("NFC", value)
    cleaned = cleaned.strip()
    cleaned = bleach.clean(cleaned, tags=[], strip=True)
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = html.escape(cleaned)

    return cleaned


def enforce_positive(value: int) -> int:
    """Ensure a number is positive."""
    if value < 0:
        raise ValueError("Value must be positive")
    return value
