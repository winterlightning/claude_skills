"""Double comment box (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87416b28-9cd9-4d1f-9509-2f57b7c73823'
SOURCE_PATH = 'icons-json/state/double comment box_87416b28-9cd9-4d1f-9509-2f57b7c73823.json'
AUTHOR = 'json_to_solo'

class DoubleCommentBoxState(Solo48):
    icon_id = 'double-comment-box-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('double', 'comment', 'box', 'state')

    def build(self):
        self.add_line('e0', (30, 27), (30, 37))
        self.add_line('e1', (28, 39), (26, 39))
        self.add_line('e2', (26, 39), (26, 44))
        self.add_line('e3', (26, 44), (21, 39))
        self.add_line('e4', (21, 39), (10, 39))
        self.add_line('e5', (8, 38), (8, 23))
        self.add_line('e6', (10, 20), (13, 20))
        self.add_line('e7', (35, 32), (35, 27))
        self.add_line('e8', (40, 24), (40, 7))
        self.add_line('e9', (37, 4), (16, 4))
        self.add_line('e10', (13, 7), (13, 24))
        self.add_line('e11', (16, 27), (30, 27))
        self.add_line('e12', (30, 27), (35, 32))
        self.add_arc('e13', (30, 37), (28, 39), radius_x=3)
        self.add_arc('e14', (10, 39), (8, 38), radius_x=2)
        self.add_line('e15', (8, 23), (10, 20))
        self.add_arc('e16', (35, 27), (40, 24), radius_x=4, sweep=False)
        self.add_arc('e17', (40, 7), (37, 4), radius_x=3, sweep=False)
        self.add_arc('e18', (16, 4), (13, 7), radius_x=3, sweep=False)
        self.add_arc('e19', (13, 24), (16, 27), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e13', 'e1', 'e2', 'e3', 'e4', 'e14', 'e5', 'e15', 'e6')
        self.add_contour('c1', 'e7', 'e16', 'e8', 'e17', 'e9', 'e18', 'e10', 'e19', 'e11', 'e12', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
