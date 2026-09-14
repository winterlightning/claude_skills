"""Planting (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9455f205-a8f4-5254-8cd0-5d2ae9ba19ea'
SOURCE_PATH = 'icons-json/outdoors/planting_9455f205-a8f4-5254-8cd0-5d2ae9ba19ea.json'
AUTHOR = 'json_to_solo'

class PlantingOutdoors(Solo48):
    icon_id = 'planting-outdoors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('planting', 'outdoors')

    def build(self):
        self.add_line('e0', (25, 26), (25, 32))
        self.add_line('e1', (25, 18), (27, 14))
        self.add_line('e2', (30, 20), (25, 20))
        self.add_line('e3', (25, 18), (25, 26))
        self.add_line('e4', (10, 44), (40, 44))
        self.add_arc('e5-1', (25, 18), (19, 7), radius_x=20, sweep=False)
        self.add_line('e5-2', (19, 7), (16, 5))
        self.add_line('e5-3', (16, 5), (10, 4))
        self.add_arc('e5-4', (10, 4), (8, 4), radius_x=56)
        self.add_line('e5-5', (8, 4), (8, 6))
        self.add_line('e5-6', (8, 6), (10, 14))
        self.add_line('e5-7', (10, 14), (13, 18))
        self.add_arc('e5-8', (13, 18), (21, 22), radius_x=22, sweep=False)
        self.add_arc('e5-9', (21, 22), (25, 26), radius_x=17)
        self.add_arc('e6-1', (27, 14), (33, 6), radius_x=15)
        self.add_arc('e6-2', (33, 6), (37, 5), radius_x=8)
        self.add_arc('e6-3', (37, 5), (40, 6), radius_x=2)
        self.add_arc('e6-4', (40, 6), (30, 20), radius_x=15)
        self.add_arc('e7-1', (40, 44), (24, 32), radius_x=16, sweep=False)
        self.add_arc('e7-2', (24, 32), (10, 44), radius_x=15, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9', 'e0')
        self.add_contour('c1', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e7-1', 'e7-2', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
