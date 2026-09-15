"""Arrow Button Down.

Plan: A single closed triangle, symmetric about the pointing axis; round stroke joins soften the three deliberate corners. HRECT centerlines (4,8)-(44,40), or VRECT (8,4)-(40,44).
Construction references: Lucide play: a single empty triangular contour.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '740341f1-eafc-5c60-be45-569b15e16c85'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow button bottom 2_740341f1-eafc-5c60-be45-569b15e16c85.svg'
SOURCE_ICON_IDS = ('740341f1-eafc-5c60-be45-569b15e16c85',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow button bottom 2_740341f1-eafc-5c60-be45-569b15e16c85.svg',)
AUTHOR = 'gpt-6'


class ArrowButtonDown(Solo48):
    icon_id = 'arrow-button-down'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'down')

    def build(self) -> None:
        axis = 24
        points = [(4,8),(44,8),(axis,40)]
        self.add_polyline("button",*points,closed=True)
