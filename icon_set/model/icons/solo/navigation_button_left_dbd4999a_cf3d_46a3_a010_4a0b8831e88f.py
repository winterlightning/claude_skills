"""Navigation button left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbd4999a-cf3d-46a3-a010-4a0b8831e88f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation button left_dbd4999a-cf3d-46a3-a010-4a0b8831e88f.svg'
AUTHOR = 'gpt-6'

class NavigationButtonLeft(Solo48):
    icon_id = 'navigation-button-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'button', 'left', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (19, 18), (13, 24))
        self.add_line('e1', (19, 30), (13, 24))
        self.add_line('e2', (35, 24), (13, 24))
        self.add_line('e3', (41, 8), (7, 8))
        self.add_line('e4', (4, 11), (4, 37))
        self.add_line('e5', (7, 40), (41, 40))
        self.add_line('e6', (44, 37), (44, 11))
        self.add_arc('e7', (7, 8), (4, 11), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e8', (4, 37), (7, 40), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e9', (41, 40), (44, 37), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e10', (44, 11), (41, 8), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10'), closed=True)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
