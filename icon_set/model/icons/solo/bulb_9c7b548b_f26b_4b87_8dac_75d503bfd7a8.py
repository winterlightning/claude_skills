"""Bulb (work), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c7b548b-f26b-4b87-8dac-75d503bfd7a8'
SOURCE_PATH = 'pictographic-primitives/work/bulb_9c7b548b-f26b-4b87-8dac-75d503bfd7a8.svg'
AUTHOR = 'gpt-6'

class Bulb(Solo48):
    icon_id = 'bulb'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('bulb', 'work')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 8), (24, 10))
        self.add_line('e1', (9, 13), (11, 15))
        self.add_line('e2', (4, 26), (6, 26))
        self.add_line('e3', (44, 26), (42, 26))
        self.add_line('e4', (18, 31), (30, 31))
        self.add_line('e5', (21, 40), (27, 40))
        self.add_line('e6', (30, 32), (32, 28))
        self.add_line('e7', (16, 28), (18, 32))
        self.add_line('e8', (37, 14), (39, 13))
        self.add_arc('e9-1', (27, 40), (29, 38), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e9-2', (29, 38), (30, 32), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e10', (32, 28), (16, 28), radius_x=8, radius_y=8, large_arc=True, sweep=False)
        self.add_line('e11-1', (18, 32), (19, 38))
        self.add_line('e11-2', (19, 38), (21, 40))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e8',), closed=False)
        self.add_contour('c3', *('e2',), closed=False)
        self.add_contour('c4', *('e3',), closed=False)
        self.add_contour('c5', *('e4',), closed=False)
        self.add_contour('c6', *('e5', 'e9-1', 'e9-2', 'e6', 'e10', 'e7', 'e11-1', 'e11-2'), closed=True)
        self.relate('connect', *('c5', 'c6'))
