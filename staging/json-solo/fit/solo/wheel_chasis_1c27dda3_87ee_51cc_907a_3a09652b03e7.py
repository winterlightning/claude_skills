"""Wheel chasis (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c27dda3-87ee-51cc-907a-3a09652b03e7'
SOURCE_PATH = 'icons-json/transportation/wheel chasis_1c27dda3-87ee-51cc-907a-3a09652b03e7.json'
AUTHOR = 'json_to_solo'

class WheelChasisTransportation(Solo48):
    icon_id = 'wheel-chasis-transportation'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('wheel', 'chasis', 'transportation')

    def build(self):
        self.add_line('e0', (44, 24), (29, 24))
        self.add_line('e1', (24, 44), (24, 29))
        self.add_line('e2', (19, 24), (4, 24))
        self.add_line('e3', (24, 19), (24, 4))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5-top', (19, 24), (29, 24), radius_x=5)
        self.add_arc('e5-bottom', (29, 24), (19, 24), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c3', 'e5')
        self.relate('connect', 'c3', 'e4')
