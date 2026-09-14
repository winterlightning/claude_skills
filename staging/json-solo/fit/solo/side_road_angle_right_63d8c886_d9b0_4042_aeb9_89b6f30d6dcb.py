"""Side road angle right (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63d8c886-d9b0-4042-aeb9-89b6f30d6dcb'
SOURCE_PATH = 'icons-json/transportation/side road angle right_63d8c886-d9b0-4042-aeb9-89b6f30d6dcb.json'
AUTHOR = 'json_to_solo'

class SideRoadAngleRight63d8c886(Solo48):
    icon_id = 'side-road-angle-right-63d8c886'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('side', 'road', 'angle', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (8, 9), (14, 6))
        self.add_line('e1', (18, 44), (18, 20))
        self.add_line('e2', (40, 34), (18, 20))
        self.add_line('e3', (27, 9), (18, 4))
        self.add_line('e4', (18, 20), (18, 4))
        self.add_line('e5', (16, 5), (18, 4))
        self.add_arc('e6', (16, 5), (14, 6), radius_x=11, sweep=False)
        self.add_arc('e7', (16, 5), (14, 6), radius_x=11, sweep=False)
        self.add_contour('c0', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e0')
        self.add_contour('c4', 'e1')
        self.add_contour('c5', 'e2')
        self.add_contour('c6', 'e3')
        self.add_contour('c7', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c7')
