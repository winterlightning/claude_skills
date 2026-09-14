"""Synchronize arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '185b4c70-8b6e-44d8-a39b-cf7d4767f520'
SOURCE_PATH = 'icons-json/interface-essential/synchronize arrow_185b4c70-8b6e-44d8-a39b-cf7d4767f520.json'
AUTHOR = 'json_to_solo'

class SynchronizeArrowInterfaceEssential(Solo48):
    icon_id = 'synchronize-arrow-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 19), (9, 25))
        self.add_line('e1', (14, 21), (9, 25))
        self.add_arc('e2-top', (22, 24), (32, 24), radius_x=5, radius_y=4)
        self.add_arc('e2-bottom', (32, 24), (22, 24), radius_x=5, radius_y=4)
        self.add_bezier('e3', (27, 40), ((27.291, 40), (27.309, 39.992), (27.6, 39.992)), ((36.118, 39.992), (43.991, 32.387), (43.991, 24.573)), ((43.991, 24.448), (44, 24.324), (44, 24.2)), ((44, 24.198), (44, 24.196), (44, 24.194)), ((44, 23.941), (43.991, 23.688), (43.991, 23.436)), ((43.991, 15.36), (35.964, 8.017), (27.255, 8.017)), ((27.118, 8.008), (26.982, 8.008), (26.845, 8)), ((26.839, 8), (26.833, 8), (26.826, 8)), ((26.424, 8), (26.03, 8.017), (25.627, 8.017)), ((19.136, 8.017), (13.027, 12.337), (10.309, 17.6)), ((9.109, 19.916), (9.327, 22.465), (9, 25)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
