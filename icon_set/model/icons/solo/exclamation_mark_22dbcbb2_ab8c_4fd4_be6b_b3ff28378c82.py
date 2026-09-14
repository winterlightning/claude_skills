"""A standalone exclamation mark. CIRCLE radial envelope reaches y4 and y44 without widening this narrow subject. Straight round-capped construction; no useful exact local Lucide match found."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82'
SOURCE_PATH = 'pictographic-primitives/symbol/exclamation_22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82.svg'
AUTHOR = 'gpt-6'


class ExclamationMark(Solo48):
    icon_id = 'exclamation-mark'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('exclamation', 'warning', 'alert', 'attention', 'important', 'error', 'notice', 'caution')

    def build(self) -> None:
        self.add_line('stem', (24,6), (24,31))
        self.add_dot('dot', (24,42))
