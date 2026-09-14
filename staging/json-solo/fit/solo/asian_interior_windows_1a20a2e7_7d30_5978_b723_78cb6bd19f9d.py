"""Batch-01/asian interior windows (decoration), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a20a2e7-7d30-5978-b723-78cb6bd19f9d'
SOURCE_PATH = 'icons-json/decoration/batch-01/asian interior windows_1a20a2e7-7d30-5978-b723-78cb6bd19f9d.json'
AUTHOR = 'json_to_solo'

class Batch01AsianInteriorWindows(Solo48):
    icon_id = 'batch-01-asian-interior-windows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'asian', 'interior', 'windows', 'decoration')

    def build(self):
        self.add_line('e0', (37, 31), (11, 31))
        self.add_line('e1', (37, 44), (37, 19))
        self.add_line('e2', (11, 16), (11, 44))
        self.add_line('e3', (40, 44), (10, 44))
        self.add_line('e4', (10, 44), (8, 44))
        self.add_line('e5', (24, 4), (24, 44))
        self.add_line('e6', (37, 18), (11, 18))
        self.add_arc('e7-1', (37, 19), (24, 4), radius_x=14, sweep=False)
        self.add_arc('e7-2', (24, 4), (11, 16), radius_x=14, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c4', 'c1')
        self.relate('connect', 'c4', 'c1')
