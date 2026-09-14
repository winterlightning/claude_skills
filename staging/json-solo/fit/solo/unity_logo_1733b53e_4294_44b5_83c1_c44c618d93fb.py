"""Unity logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1733b53e-4294-44b5-83c1-c44c618d93fb'
SOURCE_PATH = 'icons-json/logos/unity logo_1733b53e-4294-44b5-83c1-c44c618d93fb.json'
AUTHOR = 'json_to_solo'

class UnityLogoLogos(Solo48):
    icon_id = 'unity-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('unity', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (26, 12), (40, 8))
        self.add_line('e1', (16, 15), (4, 24))
        self.add_line('e2', (16, 32), (4, 24))
        self.add_line('e3', (27, 36), (40, 40))
        self.add_line('e4', (44, 29), (41, 38))
        self.add_line('e5', (41, 38), (40, 40))
        self.add_line('e6', (44, 21), (40, 8))
        self.add_line('e7', (40, 40), (29, 24))
        self.add_line('e8', (40, 8), (29, 24))
        self.add_line('e9', (29, 24), (4, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8')
        self.add_contour('c8', 'e9')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
