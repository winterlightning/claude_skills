"""Chevron Up with Wide Arms.

Plan: HRECT centerlines (4,8)-(44,40); mirrored arms share one apex and round join.
Construction references: Lucide chevron-up: one open two-segment contour.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc91dbd1-f3e2-55f8-8e78-7f10a6feba69'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow button top 1_bc91dbd1-f3e2-55f8-8e78-7f10a6feba69.svg'
SOURCE_ICON_IDS = ('bc91dbd1-f3e2-55f8-8e78-7f10a6feba69',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow button top 1_bc91dbd1-f3e2-55f8-8e78-7f10a6feba69.svg',)
AUTHOR = 'gpt-6'


class ChevronUpWithWideArms(Solo48):
    icon_id = 'chevron-up-with-wide-arms'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    aliases = ()
    keywords = ('chevron', 'up', 'with', 'wide', 'arms')

    def build(self) -> None:
        axis, half_width, peak, base = 24, 20, 8, 40
        self.add_polyline("chevron",(axis-half_width,base),(axis,peak),(axis+half_width,base))
