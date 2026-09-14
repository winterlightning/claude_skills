"""Vray logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24e489de-1d83-4e1b-b07e-3ec7241a9511'
SOURCE_PATH = 'icons-json/logos/vray logo_24e489de-1d83-4e1b-b07e-3ec7241a9511.json'
AUTHOR = 'json_to_solo'

class VrayLogo(Solo48):
    icon_id = 'vray-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('vray', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (20, 5), (18, 9))
        self.add_line('e1', (23, 26), (28, 18))
        self.add_line('e2', (38, 13), (42, 16))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e4-1', (18, 9), (14, 27), radius_x=19, sweep=False)
        self.add_arc('e4-2', (14, 27), (18, 31), radius_x=5, sweep=False)
        self.add_arc('e4-3', (18, 31), (23, 26), radius_x=8, sweep=False)
        self.add_arc('e5', (28, 18), (38, 13), radius_x=7)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1', 'e5', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e3')
