"""Keyboard arrow bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '921d7bfe-d6be-588f-ad4e-a75efb840443'
SOURCE_PATH = 'pictographic-primitives/arrows/keyboard arrow bottom_921d7bfe-d6be-588f-ad4e-a75efb840443.svg'
AUTHOR = 'gpt-6'

class KeyboardArrowBottom(Solo48):
    icon_id = 'keyboard-arrow-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'bottom', 'arrows')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (31, 44), (22, 35))
        self.add_line('e1', (40, 35), (31, 44))
        self.add_line('e2', (31, 44), (31, 14))
        self.add_line('e3', (8, 15), (8, 23))
        self.add_arc('e4-1', (31, 14), (21, 4), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('e4-2', (21, 4), (14, 6))
        self.add_arc('e4-3', (14, 6), (8, 15), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e3'), closed=False)
