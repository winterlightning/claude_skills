"""Batch-01/asian interior windows (decoration), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e7', (37, 19), ((37, 18.7), (37.482, 17.936), (37.474, 17.636)), ((37.339, 11.491), (33.768, 6.5), (28.303, 4.727)), ((27.335, 4.409), (26.181, 4.009), (25.162, 4.009)), ((24.859, 4.009), (24.564, 4), (24.269, 4)), ((24.177, 4), (24.093, 4), (24, 4)), ((23.756, 4), (23.52, 4.018), (23.276, 4.018)), ((17.962, 4.018), (12.396, 7.927), (10.973, 13.582)), ((10.804, 14.264), (11, 15.291), (11, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2')
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
