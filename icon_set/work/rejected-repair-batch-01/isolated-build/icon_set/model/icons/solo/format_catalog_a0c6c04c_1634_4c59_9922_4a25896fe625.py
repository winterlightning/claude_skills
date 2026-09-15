"""Format catalog (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0c6c04c-1634-4c59-9922-4a25896fe625'
SOURCE_PATH = 'pictographic-primitives/design/format catalog_a0c6c04c-1634-4c59-9922-4a25896fe625.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class FormatCatalog(Solo48):
    icon_id = 'format-catalog'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('format', 'catalog', 'design')

    def build(self):
        self.add_line('e0', (8, 14), (24, 24))
        self.add_line('e1', (8, 14), (24, 4))
        self.add_line('e2', (24, 4), (40, 14))
        self.add_line('e3', (8, 14), (8, 33))
        self.add_line('e4', (9, 34), (24, 44))
        self.add_line('e5', (24, 24), (24, 44))
        self.add_line('e6', (24, 24), (40, 14))
        self.add_line('e7', (24, 44), (40, 34))
        self.add_line('e8', (40, 34), (40, 14))
        self.add_arc('e9', (8, 33), (9, 34), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e9', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
