"""Rtf format (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '63768576-e3c2-41a6-925a-10bbe0f0af14'
SOURCE_PATH = 'icons-json/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.json'
AUTHOR = 'gpt-6'

class RtfFormat(Solo48):
    icon_id = 'rtf-format'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rtf', 'format', 'state')

    def build(self):
        self.add_line('e0', (40, 13), (39, 11))
        self.add_line('e1', (39, 11), (33, 6))
        self.add_line('e2', (33, 6), (32, 4))
        self.add_line('e3', (32, 4), (12, 4))
        self.add_line('e4', (8, 9), (8, 39))
        self.add_line('e5', (11, 44), (36, 44))
        self.add_line('e7', (18, 24), (30, 24))
        self.add_line('e8', (28, 34), (20, 34))
        self.add_line('e9', (18, 32), (18, 16))
        self.add_line('e10', (20, 14), (28, 14))
        self.add_line('e11', (30, 16), (30, 32))
        self.add_line('e12-1', (12, 4), (9, 5))
        self.add_line('e12-2', (9, 5), (8, 9))
        self.add_line('e13-1', (8, 39), (9, 43))
        self.add_line('e13-2', (9, 43), (11, 44))
        self.add_arc('e14-1', (36, 44), (40, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('e14-2', (40, 40), (40, 13))
        self.add_arc('e15', (20, 34), (18, 32), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e16', (18, 16), (20, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e17', (28, 14), (30, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('e18', (30, 32), (28, 34), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e12-1', 'e12-2', 'e4', 'e13-1', 'e13-2', 'e5', 'e14-1', 'e14-2', closed=True)
        self.add_contour('c1', 'e7', closed=False)
        self.add_contour('c2', 'e8', 'e15', 'e9', 'e16', 'e10', 'e17', 'e11', 'e18', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
