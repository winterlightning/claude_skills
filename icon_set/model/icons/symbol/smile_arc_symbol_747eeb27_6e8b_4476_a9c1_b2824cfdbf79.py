"""A single upward-curving smile arc without eyes or an outer face circle. Exclude the unlocked padlock.

Plan: Single elliptical lower arc centered on x16; no face or eyes. Bounds (2,10)-(30,22).
Construction reference: No close Lucide subject; use simple connected contours."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '747eeb27-6e8b-4476-a9c1-b2824cfdbf79'
SOURCE_PATH = 'pictographic-primitives/state/unlock 1_747eeb27-6e8b-4476-a9c1-b2824cfdbf79.svg'
SOURCE_ICON_IDS = ('747eeb27-6e8b-4476-a9c1-b2824cfdbf79',)
AUTHOR = 'gpt-6'

class SmileArcSymbol(Symbol32):
    icon_id = 'smile-arc-symbol'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('smile', 'arc', 'symbol')

    def build(self) -> None:
        self.add_arc('smile',(2,10),(30,10),radius_x=14,radius_y=12,sweep=False)
