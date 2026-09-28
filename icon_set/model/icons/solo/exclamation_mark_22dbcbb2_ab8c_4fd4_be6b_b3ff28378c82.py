"""Upright exclamation mark with a 4-unit-wide stem and separate round dot.
Custom visible bounds (22,2)-(26,46) preserve the source typography.
No standard SOLO48 envelope has a stroke-width minor axis.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82'
SOURCE_PATH = 'pictographic-primitives/symbol/exclamation_22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82.svg'
AUTHOR = 'gpt-6'


class ExclamationMark(Solo48):
    icon_id = 'exclamation-mark'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('exclamation', 'warning', 'alert', 'attention', 'important', 'error', 'notice', 'caution')

    def build(self) -> None:
        self.add_line('stem', (24,4), (24,31))
        self.add_dot('dot', (24,44))
