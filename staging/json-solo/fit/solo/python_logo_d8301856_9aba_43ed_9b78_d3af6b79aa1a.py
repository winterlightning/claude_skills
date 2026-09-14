"""Python logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8301856-9aba-43ed-9b78-d3af6b79aa1a'
SOURCE_PATH = 'icons-json/logos/python logo_d8301856-9aba-43ed-9b78-d3af6b79aa1a.json'
AUTHOR = 'json_to_solo'

class PythonLogoLogos(Solo48):
    icon_id = 'python-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('python', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (24, 32), (32, 32))
        self.add_line('e1', (24, 16), (16, 16))
        self.add_line('e2', (36, 16), (32, 16))
        self.add_line('e3', (32, 32), (32, 37))
        self.add_line('e4', (16, 38), (16, 32))
        self.add_line('e5', (26, 24), (22, 24))
        self.add_line('e6', (16, 29), (16, 32))
        self.add_line('e7', (16, 10), (16, 16))
        self.add_arc('e8-1', (32, 32), (41, 29), radius_x=8, sweep=False)
        self.add_line('e8-2', (41, 29), (42, 24))
        self.add_line('e8-3', (42, 24), (41, 19))
        self.add_arc('e8-4', (41, 19), (36, 16), radius_x=5, sweep=False)
        self.add_arc('e9-1', (32, 37), (31, 40), radius_x=4)
        self.add_line('e9-2', (31, 40), (24, 42))
        self.add_line('e9-3', (24, 42), (18, 41))
        self.add_arc('e9-4', (18, 41), (16, 38), radius_x=4)
        self.add_arc('e10', (32, 16), (26, 24), radius_x=6)
        self.add_arc('e11', (22, 24), (16, 29), radius_x=6, sweep=False)
        self.add_line('e12-1', (32, 16), (32, 11))
        self.add_line('e12-2', (32, 11), (31, 8))
        self.add_line('e12-3', (31, 8), (24, 6))
        self.add_line('e12-4', (24, 6), (18, 7))
        self.add_arc('e12-5', (18, 7), (16, 10), radius_x=4, sweep=False)
        self.add_line('e13-1', (16, 32), (11, 32))
        self.add_arc('e13-2', (11, 32), (8, 31), radius_x=6)
        self.add_arc('e13-3', (8, 31), (6, 25), radius_x=10)
        self.add_line('e13-4', (6, 25), (7, 19))
        self.add_arc('e13-5', (7, 19), (16, 16), radius_x=8)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e2')
        self.add_contour('c3', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e4')
        self.add_contour('c4', 'e10', 'e5', 'e11', 'e6')
        self.add_contour('c5', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e12-5', 'e7')
        self.add_contour('c6', 'e13-1', 'e13-2', 'e13-3', 'e13-4', 'e13-5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
