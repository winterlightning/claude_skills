"""Arrows minimize (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f863c29b-edcf-493a-b663-efc79d4ff12d'
SOURCE_PATH = 'icons-json/_uncategorized_04/arrows minimize_f863c29b-edcf-493a-b663-efc79d4ff12d.json'
AUTHOR = 'json_to_solo'

class ArrowsMinimizeUncategorized04(Solo48):
    icon_id = 'arrows-minimize-uncategorized-04'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('arrows', 'minimize', '_uncategorized_04')

    def build(self):
        self.add_line('sym-e0', (17, 31), (6, 42))
        self.add_line('sym-e1', (6, 42), (6, 32))
        self.add_line('sym-e2', (15, 42), (6, 42))
        self.add_line('sym-e3', (31, 31), (42, 42))
        self.add_line('sym-e4', (42, 42), (33, 42))
        self.add_line('sym-e5', (42, 32), (42, 42))
        self.add_line('sym-e6', (17, 17), (6, 6))
        self.add_line('sym-e7', (6, 6), (6, 16))
        self.add_line('sym-e8', (15, 6), (6, 6))
        self.add_line('sym-e9', (31, 17), (42, 6))
        self.add_line('sym-e10', (42, 6), (33, 6))
        self.add_line('sym-e11', (42, 16), (42, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c5', 'sym-e8')
        self.add_contour('sym-c6', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c7', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c6', 'sym-c7')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c4', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c6', 'sym-c7')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c6', 'sym-c7')
        self.relate('connect', 'sym-c2', 'sym-c3')
