"""Wheat (farming), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '685deb0b-da5b-471f-aa90-b602ca4b7697'
SOURCE_PATH = 'icons-json/farming/wheat_685deb0b-da5b-471f-aa90-b602ca4b7697.json'
AUTHOR = 'json_to_solo'

class Wheat685deb0b(Solo48):
    icon_id = 'wheat-685deb0b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'farming'
    aliases = ()
    keywords = ('wheat', 'farming')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 34))
        self.add_line('sym-e1', (24, 34), (24, 31))
        self.add_line('sym-e2', (24, 31), (24, 29))
        self.add_line('sym-e3', (24, 29), (24, 19))
        self.add_bezier('sym-e4', (24, 19), ((25.888, 18.118), (27.464, 18.091), (29, 17)))
        self.add_bezier('sym-e5', (29, 17), ((33.176, 14.045), (33.096, 9.964), (29, 7)))
        self.add_bezier('sym-e6', (29, 7), ((28.329, 6.512), (24.922, 4.108), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((23.078, 4.108), (19.671, 6.512), (19, 7)))
        self.add_bezier('sym-e8', (19, 7), ((14.904, 9.964), (14.824, 14.045), (19, 17)))
        self.add_bezier('sym-e9', (19, 17), ((20.536, 18.091), (22.112, 18.118), (24, 19)))
        self.add_bezier('sym-e10', (40, 21), ((30.464, 22.136), (28.016, 24.255), (24, 29)))
        self.add_bezier('sym-e11', (24, 29), ((19.984, 24.255), (17.536, 22.136), (8, 21)))
        self.add_bezier('sym-e12', (8, 21), ((8, 21.936), (8, 23.064), (8, 24)))
        self.add_bezier('sym-e13', (8, 24), ((8, 30.045), (14.48, 32.727), (24, 34)))
        self.add_bezier('sym-e14', (24, 34), ((33.52, 32.727), (40, 30.045), (40, 24)))
        self.add_bezier('sym-e15', (40, 24), ((40, 23.064), (40, 21.936), (40, 21)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
