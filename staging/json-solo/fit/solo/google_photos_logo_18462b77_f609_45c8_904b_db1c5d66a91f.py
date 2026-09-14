"""Google photos logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18462b77-f609-45c8-904b-db1c5d66a91f'
SOURCE_PATH = 'icons-json/logos/google photos logo_18462b77-f609-45c8-904b-db1c5d66a91f.json'
AUTHOR = 'json_to_solo'

class GooglePhotosLogoLogos(Solo48):
    icon_id = 'google-photos-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'photos', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (23, 26), (22, 24))
        self.add_line('e1', (23, 26), (22, 32))
        self.add_line('e2', (22, 32), (22, 42))
        self.add_line('e3', (42, 24), (29, 24))
        self.add_line('e4', (29, 24), (27, 24))
        self.add_line('e5', (20, 24), (22, 24))
        self.add_line('e6', (20, 24), (6, 24))
        self.add_line('e7', (27, 24), (22, 24))
        self.add_line('e8', (22, 6), (22, 22))
        self.add_arc('e9', (22, 42), (20, 24), radius_x=10)
        self.add_arc('e10-1', (23, 26), (42, 25), radius_x=10, sweep=False)
        self.add_line('e10-2', (42, 25), (42, 24))
        self.add_arc('e11-1', (6, 24), (11, 17), radius_x=9)
        self.add_arc('e11-2', (11, 17), (22, 22), radius_x=8)
        self.add_arc('e12-1', (27, 24), (32, 13), radius_x=8, sweep=False)
        self.add_arc('e12-2', (32, 13), (23, 6), radius_x=11, sweep=False)
        self.add_line('e12-3', (23, 6), (22, 6))
        self.add_arc('e13', (22, 22), (22, 24), radius_x=23)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e9')
        self.add_contour('c2', 'e10-1', 'e10-2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e11-1', 'e11-2')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e12-1', 'e12-2', 'e12-3', 'e8')
        self.add_contour('c7', 'e13')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
