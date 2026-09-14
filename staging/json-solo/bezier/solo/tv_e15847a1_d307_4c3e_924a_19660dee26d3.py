"""Tv (tv), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e15847a1-d307-4c3e-924a-19660dee26d3'
SOURCE_PATH = 'icons-json/tv/tv_e15847a1-d307-4c3e-924a-19660dee26d3.json'
AUTHOR = 'json_to_solo'

class Tv(Solo48):
    icon_id = 'tv'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('tv',)

    def build(self):
        self.add_line('sym-e0', (36, 40), (12, 40))
        self.add_line('sym-e1', (12, 40), (10, 40))
        self.add_bezier('sym-e2', (10, 40), ((8.872, 39.473), (8.488, 40.2), (8, 39)))
        self.add_line('sym-e3', (8, 39), (8, 15))
        self.add_bezier('sym-e4', (8, 15), ((8.135, 14.873), (8, 14.118), (8, 14)))
        self.add_bezier('sym-e5', (8, 14), ((8.404, 13.682), (9.512, 14), (10, 14)))
        self.add_line('sym-e6', (10, 14), (24, 14))
        self.add_line('sym-e7', (24, 14), (16, 4))
        self.add_line('sym-e8', (12, 44), (12, 40))
        self.add_line('sym-e9', (32, 4), (24, 14))
        self.add_line('sym-e10', (24, 14), (38, 14))
        self.add_bezier('sym-e11', (38, 14), ((38.488, 14), (39.596, 13.682), (40, 14)))
        self.add_bezier('sym-e12', (40, 14), ((40, 14.118), (39.865, 14.873), (40, 15)))
        self.add_line('sym-e13', (40, 15), (40, 39))
        self.add_bezier('sym-e14', (40, 39), ((39.512, 40.2), (39.128, 39.473), (38, 40)))
        self.add_line('sym-e15', (38, 40), (36, 40))
        self.add_line('sym-e16', (36, 40), (36, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c1', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
