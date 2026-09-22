"""Typeface membership is independent of whether a symbol has reusable paths."""
import string

# Curly quotes and the degree mark are keyboard punctuation variants.
KEYBOARD_CHARACTERS = frozenset(string.ascii_letters + string.digits
                               + string.punctuation.replace('$', '') + '“”‘’°')


def is_typeface_character(character: str) -> bool:
    """Currency (including keyboard $), specialist marks and icons are not text."""
    return len(character) == 1 and character in KEYBOARD_CHARACTERS
