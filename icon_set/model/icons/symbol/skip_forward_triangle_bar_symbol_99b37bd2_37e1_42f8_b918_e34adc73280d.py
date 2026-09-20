"""An outlined right-pointing triangle followed by one separate vertical end bar. Exclude any circle or television frame.

Plan: One outlined triangle and one separated end bar. Bounds (2,4)-(30,28).
Construction reference: Lucide skip-forward: triangle and separated vertical terminal bar."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '99b37bd2-37e1-42f8-b918-e34adc73280d'
SOURCE_PATH = 'pictographic-primitives/other/tv control next_99b37bd2-37e1-42f8-b918-e34adc73280d.svg'
SOURCE_ICON_IDS = ('99b37bd2-37e1-42f8-b918-e34adc73280d',)
AUTHOR = 'gpt-6'

class SkipForwardTriangleBarSymbol(Symbol32):
    icon_id = 'skip-forward-triangle-bar-symbol'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('skip', 'forward', 'triangle', 'bar', 'symbol')

    def build(self) -> None:
        self.add_polyline('triangle',(2,4),(22,16),(2,28),closed=True)
        self.add_line('bar',(30,4),(30,28))
