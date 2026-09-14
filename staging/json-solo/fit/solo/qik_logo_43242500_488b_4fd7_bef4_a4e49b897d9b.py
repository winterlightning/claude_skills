"""Qik logo (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43242500-488b-4fd7-bef4-a4e49b897d9b'
SOURCE_PATH = 'icons-json/_uncategorized_32/qik logo_43242500-488b-4fd7-bef4-a4e49b897d9b.json'
AUTHOR = 'json_to_solo'

class QikLogoUncategorized(Solo48):
    icon_id = 'qik-logo-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('qik', 'logo', '_uncategorized')

    def build(self):
        self.add_line('e0', (42, 42), (33, 33))
        self.add_arc('e1-1', (33, 33), (6, 22), radius_x=16)
        self.add_line('e1-2', (6, 22), (8, 14))
        self.add_arc('e1-3', (8, 14), (21, 6), radius_x=15)
        self.add_line('e1-4', (21, 6), (27, 7))
        self.add_line('e1-5', (27, 7), (32, 10))
        self.add_arc('e1-6', (32, 10), (37, 21), radius_x=16)
        self.add_arc('e1-7', (37, 21), (33, 33), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', closed=True)
        self.relate('connect', 'c0', 'c1')
