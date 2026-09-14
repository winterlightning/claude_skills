"""Synchronize arrows (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '180d4acb-d66a-4301-9e3b-037ca7e80db1'
SOURCE_PATH = 'icons-json/interface-essential/synchronize arrows_180d4acb-d66a-4301-9e3b-037ca7e80db1.json'
AUTHOR = 'gpt-6'

class SynchronizeArrows(Solo48):
    icon_id = 'synchronize-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'arrows', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (17, 35), (11, 36))
        self.add_line('e1', (11, 36), (13, 42))
        self.add_line('e2', (33, 6), (35, 13))
        self.add_line('e3', (35, 13), (28, 13))
        self.add_arc('e4-1', (41, 19), (42, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e4-2', (42, 24), (11, 36), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('e5-1', (7, 29), (6, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e5-2', (6, 24), (35, 13), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_contour('c0', *('e4-1', 'e4-2'), closed=False)
        self.add_contour('c1', *('e0', 'e1'), closed=False)
        self.add_contour('c2', *('e2', 'e3'), closed=False)
        self.add_contour('c3', *('e5-1', 'e5-2'), closed=False)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c2', 'c3'))
