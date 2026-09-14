"""Earth 1 (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd670eb75-f1dd-5bf4-9a7e-58d5a10de8f0'
SOURCE_PATH = 'icons-json/maps/earth 1_d670eb75-f1dd-5bf4-9a7e-58d5a10de8f0.json'
AUTHOR = 'json_to_solo'

class Earth1Maps(Solo48):
    icon_id = 'earth-1-maps'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_line('e0', (40, 13), (39, 12))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2-1', (13, 23), (18, 24), radius_x=13)
        self.add_line('e2-2', (18, 24), (24, 28))
        self.add_arc('e2-3', (24, 28), (25, 32), radius_x=3)
        self.add_arc('e2-4', (25, 32), (19, 40), radius_x=48)
        self.add_line('e2-5', (19, 40), (17, 42))
        self.add_line('e2-6', (17, 42), (17, 41))
        self.add_line('e2-7', (17, 41), (16, 35))
        self.add_line('e2-8', (16, 35), (12, 28))
        self.add_arc('e2-9', (12, 28), (13, 24), radius_x=16)
        self.add_arc('e2-10', (13, 24), (12, 23), radius_x=1, sweep=False)
        self.add_arc('e2-11', (12, 23), (5, 19), radius_x=10)
        self.add_arc('e3-1', (39, 12), (29, 20), radius_x=8, sweep=False)
        self.add_arc('e3-2', (29, 20), (31, 25), radius_x=4, sweep=False)
        self.add_arc('e3-3', (31, 25), (37, 27), radius_x=6)
        self.add_arc('e3-4', (37, 27), (41, 34), radius_x=16, sweep=False)
        self.add_arc('e4-1', (12, 23), (12, 18), radius_x=5)
        self.add_arc('e4-2', (12, 18), (17, 14), radius_x=20)
        self.add_arc('e4-3', (17, 14), (18, 13), radius_x=6)
        self.add_line('e4-4', (18, 13), (19, 5))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11')
        self.add_contour('c1', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c1', 'e1')
        self.relate('connect', 'c1', 'e1')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'e1')
