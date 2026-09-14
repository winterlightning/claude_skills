"""Material ui logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bab5995-9993-44a4-941d-fd5906950e0d'
SOURCE_PATH = 'icons-json/logos/material ui logo_4bab5995-9993-44a4-941d-fd5906950e0d.json'
AUTHOR = 'json_to_solo'

class MaterialUiLogo(Solo48):
    icon_id = 'material-ui-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('material', 'ui', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (34, 22), (24, 29))
        self.add_line('e1', (24, 42), (42, 31))
        self.add_line('e2', (42, 30), (42, 6))
        self.add_line('e3', (42, 6), (23, 18))
        self.add_line('e4', (23, 18), (7, 8))
        self.add_line('e5', (6, 8), (6, 26))
        self.add_line('e6', (7, 27), (13, 31))
        self.add_line('e7', (13, 31), (13, 22))
        self.add_line('e8', (14, 23), (24, 29))
        self.add_line('e9', (24, 29), (24, 42))
        self.add_arc('e10', (42, 31), (42, 30), radius_x=32)
        self.add_line('e11', (7, 8), (6, 8))
        self.add_arc('e12', (6, 26), (7, 27), radius_x=1, sweep=False)
        self.add_line('e14', (13, 22), (14, 23))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e10', 'e2', 'e3', 'e4', 'e11', 'e5', 'e12', 'e6', 'e7', 'e14', 'e8', 'e9', closed=True)
        self.relate('connect', 'c0', 'c1')
