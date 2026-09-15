"""Arrow Button Right.

Plan: A single closed triangle, symmetric about the pointing axis; round stroke joins soften the three deliberate corners. HRECT centerlines (4,8)-(44,40), or VRECT (8,4)-(40,44).
Construction references: Lucide play: a single empty triangular contour.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '388b83b0-6c10-5d3d-a481-473f77f30237'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow button right 2_388b83b0-6c10-5d3d-a481-473f77f30237.svg'
SOURCE_ICON_IDS = ('388b83b0-6c10-5d3d-a481-473f77f30237',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow button right 2_388b83b0-6c10-5d3d-a481-473f77f30237.svg',)
AUTHOR = 'gpt-6'


class ArrowButtonRight(Solo48):
    icon_id = 'arrow-button-right'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'right')

    def build(self) -> None:
        axis = 24
        points = [(4,8),(44,8),(axis,40)]
        points = [(48-y, x) for x,y in points]
        self.add_polyline("button",*points,closed=True)
