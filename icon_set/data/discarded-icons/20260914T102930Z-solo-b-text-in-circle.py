"""B text in circle (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc52ca8a-3c94-4ea2-a571-d56f66bbeff1'
SOURCE_PATH = 'icons-json/state/b text in circle_bc52ca8a-3c94-4ea2-a571-d56f66bbeff1.json'
AUTHOR = 'json_to_solo'

class BTextInCircle(Solo48):
    icon_id = 'b-text-in-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('b', 'text', 'in', 'circle', 'state')

    def build(self):
        self.add_line('e0', (24, 14), (18, 14))
        self.add_line('e1', (18, 14), (18, 34))
        self.add_line('e2', (18, 34), (22, 34))
        self.add_line('e3', (25, 24), (18, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5-1', (22, 34), (30, 29), radius_x=6, sweep=False)
        self.add_arc('e5-2', (30, 29), (25, 24), radius_x=5, sweep=False)
        self.add_arc('e5-3', (25, 24), (29, 17), radius_x=5, sweep=False)
        self.add_arc('e5-4', (29, 17), (24, 14), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
