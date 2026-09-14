"""Palette (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013'
SOURCE_PATH = 'icons-json/design/palette_bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013.json'
AUTHOR = 'json_to_solo'

class PaletteDesign(Solo48):
    icon_id = 'palette-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('palette', 'design')

    def build(self):
        self.add_line('e0', (18, 15), (19, 16))
        self.add_arc('e1', (13, 30), (14, 30), radius_x=18)
        self.add_arc('e2', (31, 16), (31, 15), radius_x=20)
        self.add_line('e3-1', (8, 17), (6, 25))
        self.add_line('e3-2', (6, 25), (6, 28))
        self.add_arc('e3-3', (6, 28), (9, 36), radius_x=20, sweep=False)
        self.add_arc('e3-4', (9, 36), (18, 42), radius_x=11, sweep=False)
        self.add_line('e3-5', (18, 42), (22, 41))
        self.add_line('e3-6', (22, 41), (29, 32))
        self.add_line('e3-7', (29, 32), (38, 30))
        self.add_arc('e3-8', (38, 30), (41, 27), radius_x=7, sweep=False)
        self.add_line('e3-9', (41, 27), (42, 22))
        self.add_arc('e3-10', (42, 22), (26, 6), radius_x=16, sweep=False)
        self.add_line('e3-11', (26, 6), (19, 7))
        self.add_line('e3-12', (19, 7), (15, 9))
        self.add_arc('e3-13', (15, 9), (8, 17), radius_x=20, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', 'e3-12', 'e3-13', closed=True)
