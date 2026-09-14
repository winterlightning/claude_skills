"""Deploy (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aab49738-a401-514b-847e-1fe43007c663'
SOURCE_PATH = 'icons-json/design/deploy_aab49738-a401-514b-847e-1fe43007c663.json'
AUTHOR = 'json_to_solo'

class Deploy(Solo48):
    icon_id = 'deploy'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('deploy', 'design')

    def build(self):
        self.add_line('e0', (29, 9), (35, 4))
        self.add_line('e1', (35, 4), (40, 9))
        self.add_line('e2', (35, 4), (35, 41))
        self.add_line('e3', (32, 44), (11, 44))
        self.add_line('e4', (8, 41), (8, 21))
        self.add_line('e5', (27, 23), (16, 23))
        self.add_line('e6', (16, 23), (16, 36))
        self.add_line('e7', (16, 36), (27, 36))
        self.add_line('e8', (27, 36), (27, 23))
        self.add_arc('e9', (35, 41), (32, 44), radius_x=3)
        self.add_arc('e10', (11, 44), (8, 41), radius_x=3)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e9', 'e3', 'e10', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
