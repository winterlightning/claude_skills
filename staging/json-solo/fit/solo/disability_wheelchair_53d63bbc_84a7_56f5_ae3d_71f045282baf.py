"""Disability wheelchair (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53d63bbc-84a7-56f5-ae3d-71f045282baf'
SOURCE_PATH = 'icons-json/wayfinding/disability wheelchair_53d63bbc-84a7-56f5-ae3d-71f045282baf.json'
AUTHOR = 'json_to_solo'

class DisabilityWheelchairWayfinding(Solo48):
    icon_id = 'disability-wheelchair-wayfinding'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('disability', 'wheelchair', 'wayfinding')

    def build(self):
        self.add_line('e0', (16, 13), (19, 32))
        self.add_line('e1', (19, 32), (32, 29))
        self.add_line('e2', (32, 29), (36, 41))
        self.add_line('e3', (36, 41), (40, 40))
        self.add_line('e4', (27, 22), (17, 23))
        self.add_arc('e5-top', (12, 9), (20, 9), radius_x=4, radius_y=5)
        self.add_arc('e5-bottom', (20, 9), (12, 9), radius_x=4, radius_y=5)
        self.add_arc('e6-1', (15, 24), (9, 29), radius_x=11, sweep=False)
        self.add_line('e6-2', (9, 29), (8, 34))
        self.add_arc('e6-3', (8, 34), (18, 44), radius_x=10, sweep=False)
        self.add_arc('e6-4', (18, 44), (27, 33), radius_x=10, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e6-4')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'c1')
