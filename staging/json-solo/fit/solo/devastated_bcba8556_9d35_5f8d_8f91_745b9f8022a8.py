"""Devastated (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcba8556-9d35-5f8d-8f91-745b9f8022a8'
SOURCE_PATH = 'icons-json/smileys/devastated_bcba8556-9d35-5f8d-8f91-745b9f8022a8.json'
AUTHOR = 'json_to_solo'

class DevastatedSmileys(Solo48):
    icon_id = 'devastated-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('devastated', 'smileys')

    def build(self):
        self.add_line('e0', (19, 15), (13, 22))
        self.add_line('e1', (12, 15), (16, 19))
        self.add_line('e2', (19, 22), (16, 19))
        self.add_line('e3', (29, 15), (35, 22))
        self.add_line('e4', (29, 22), (35, 15))
        self.add_arc('e5-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e5-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e6', (15, 34), (33, 34), radius_x=10)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e6')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
