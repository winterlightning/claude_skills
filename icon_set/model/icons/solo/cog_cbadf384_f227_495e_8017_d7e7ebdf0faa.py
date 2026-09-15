"""Cog (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cbadf384-f227-495e-8017-d7e7ebdf0faa'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_cbadf384-f227-495e-8017-d7e7ebdf0faa.svg'
AUTHOR = 'gpt-6'

class CogCbadf384(Solo48):
    icon_id = 'cog-cbadf384'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (6, 30), (10, 26))
        self.add_line('e1', (10, 21), (7, 17))
        self.add_line('e2', (20, 11), (21, 8))
        self.add_line('e3', (33, 13), (39, 13))
        self.add_line('e4', (41, 17), (38, 21))
        self.add_line('e5', (39, 26), (42, 30))
        self.add_line('e6', (39, 35), (35, 34))
        self.add_line('e7', (26, 42), (22, 42))
        self.add_line('e8', (14, 34), (9, 35))
        self.add_arc('e9-top', (20, 24), (28, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e9-bottom', (28, 24), (20, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e10-1', (9, 35), (6, 31), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('e10-2', (6, 31), (6, 30))
        self.add_arc('e11', (10, 26), (10, 21), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('e12-1', (7, 17), (6, 16))
        self.add_line('e12-2', (6, 16), (10, 12))
        self.add_arc('e12-3', (10, 12), (20, 11), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e13-1', (21, 8), (24, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('e13-2', (24, 6), (27, 7))
        self.add_arc('e13-3', (27, 7), (29, 12), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e13-4', (29, 12), (33, 13), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('e14', (39, 13), (41, 17), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e15', (38, 21), (39, 26), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('e16-1', (42, 30), (41, 33), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('e16-2', (41, 33), (39, 35))
        self.add_arc('e17-1', (35, 34), (29, 36), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e17-2', (29, 36), (26, 42), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e18-1', (22, 42), (19, 36))
        self.add_arc('e18-2', (19, 36), (14, 34), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_contour('c0', *('e10-1', 'e10-2', 'e0', 'e11', 'e1', 'e12-1', 'e12-2', 'e12-3', 'e2', 'e13-1', 'e13-2', 'e13-3', 'e13-4', 'e3', 'e14', 'e4', 'e15', 'e5', 'e16-1', 'e16-2', 'e6', 'e17-1', 'e17-2', 'e7', 'e18-1', 'e18-2', 'e8'), closed=True)
        self.add_contour('e9', *('e9-top', 'e9-bottom'), closed=True)
