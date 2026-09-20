"""Two plain clock hands meeting at a right angle: one upward and one rightward. Exclude any clock-face circle, phone, and refresh arrows.

Plan: One right-angle run, open clock hands with no dial. Bounds (2,2)-(30,30).
Construction reference: No close Lucide subject; use simple connected contours."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '49a79098-c0be-4d5e-8dd8-ff360a2a7d0d'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone clock_49a79098-c0be-4d5e-8dd8-ff360a2a7d0d.svg'
SOURCE_ICON_IDS = ('49a79098-c0be-4d5e-8dd8-ff360a2a7d0d', 'ab913828-297d-4c94-ab76-5b92952287d3')
AUTHOR = 'gpt-6'

class ClockHandsOnlySymbol(Symbol32):
    icon_id = 'clock-hands-only-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('clock', 'hands', 'only', 'symbol')

    def build(self) -> None:
        self.add_polyline('hands',(2,2),(2,30),(30,30))
