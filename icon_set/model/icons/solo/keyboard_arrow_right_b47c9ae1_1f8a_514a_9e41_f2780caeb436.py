"""Keyboard arrow right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b47c9ae1-1f8a-514a-9e41-f2780caeb436'
SOURCE_PATH = 'icons-json/interface-essential/keyboard arrow right_b47c9ae1-1f8a-514a-9e41-f2780caeb436.json'
AUTHOR = 'gpt-6'

class KeyboardArrowRight(Solo48):
    icon_id = 'keyboard-arrow-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'right', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (44, 17), (35, 26))
        self.add_line('e1', (35, 8), (44, 17))
        self.add_line('e2', (44, 17), (14, 17))
        self.add_line('e3', (15, 40), (23, 40))
        self.add_arc('e4-1', (14, 17), (4, 27), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('e4-2', (4, 27), (6, 34))
        self.add_arc('e4-3', (6, 34), (15, 40), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e3'), closed=False)
