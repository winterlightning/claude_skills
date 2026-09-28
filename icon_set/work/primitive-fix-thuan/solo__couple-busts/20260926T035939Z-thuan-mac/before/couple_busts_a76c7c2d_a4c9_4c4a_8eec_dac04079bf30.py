"""Couple. Keeps two equal head-and-shoulder busts; drops the small hair division to preserve the head openings.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide users-round: round heads and broad shoulder arches; the supplied source calls for equal side-by-side busts.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a76c7c2d-a4c9-4c4a-8eec-dac04079bf30'
SOURCE_PATH = 'pictographic-primitives/symbol/couple_a76c7c2d-a4c9-4c4a-8eec-dac04079bf30.svg'
AUTHOR = 'gpt-6'


class CoupleBusts(Solo48):
    icon_id = 'couple-busts'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('couple', 'people', 'man', 'woman', 'partners', 'users', 'relationship', 'pair')

    def build(self) -> None:
        self.add_arc('left-head-right', (11, 8), (11, 20), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('left-head-left', (11, 20), (11, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('left-head', 'left-head-right', 'left-head-left', closed=True)
        self.add_arc('left-shoulders', (4, 40), (18, 40), radius_x=7, radius_y=8, sweep=True)
        self.add_arc('right-head-right', (37, 8), (37, 20), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('right-head-left', (37, 20), (37, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('right-head', 'right-head-right', 'right-head-left', closed=True)
        self.add_arc('right-shoulders', (30, 40), (44, 40), radius_x=7, radius_y=8, sweep=True)
