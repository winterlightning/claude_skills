"""Vray logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24e489de-1d83-4e1b-b07e-3ec7241a9511'
SOURCE_PATH = 'icons-json/logos/vray logo_24e489de-1d83-4e1b-b07e-3ec7241a9511.json'
AUTHOR = 'json_to_solo'

class VrayLogoLogos(Solo48):
    icon_id = 'vray-logo-logos'
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
        self.add_bezier('e4', (18, 9), ((14.5, 13.664), (12.318, 18.664), (13.227, 24.491)), ((13.645, 27.182), (15.9, 32.336), (19.473, 30.527)), ((21.136, 29.682), (22.127, 27.573), (23, 26)))
        self.add_bezier('e5', (28, 18), ((30.327, 13.8), (33.009, 10.009), (38, 13)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e3')
