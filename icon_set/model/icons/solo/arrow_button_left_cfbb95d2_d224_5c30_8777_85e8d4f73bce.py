"""Arrow Button Left.

Plan: A single closed triangle, symmetric about the pointing axis; round stroke joins soften the three deliberate corners. HRECT centerlines (4,8)-(44,40), or VRECT (8,4)-(40,44).
Construction references: Lucide play: a single empty triangular contour.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfbb95d2-d224-5c30-8777-85e8d4f73bce'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow button left 2_cfbb95d2-d224-5c30-8777-85e8d4f73bce.svg'
SOURCE_ICON_IDS = ('cfbb95d2-d224-5c30-8777-85e8d4f73bce',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow button left 2_cfbb95d2-d224-5c30-8777-85e8d4f73bce.svg',)
AUTHOR = 'gpt-6'


class ArrowButtonLeft(Solo48):
    icon_id = 'arrow-button-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'button', 'left')

    def build(self) -> None:
        axis = 24
        points = [(4,8),(44,8),(axis,40)]
        points = [(48-y, x) for x,y in points]
        self.add_polyline("button",*points,closed=True)
