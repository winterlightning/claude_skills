"""Metal sheet (construction), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a05feef9-d6c1-4050-8014-feb049ba4197'
SOURCE_PATH = 'pictographic-primitives/construction/metal sheet_a05feef9-d6c1-4050-8014-feb049ba4197.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MetalSheet(Solo48):
    icon_id = 'metal-sheet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('metal', 'sheet', 'construction')

    def build(self):
        self.add_line('e0', (4, 12), (4, 37))
        self.add_line('e1', (7, 40), (25, 40))
        self.add_line('e2', (29, 37), (29, 32))
        self.add_line('e3', (12, 8), (13, 10))
        self.add_line('e4', (15, 12), (15, 29))
        self.add_line('e5', (18, 32), (29, 32))
        self.add_line('e6', (12, 8), (41, 8))
        self.add_line('e7', (44, 11), (44, 31))
        self.add_line('e8', (42, 32), (29, 32))
        self.add_line('e9-1', (12, 8), (6, 9))
        self.add_arc('e9-2', (6, 9), (4, 12), radius_x=4, sweep=False)
        self.add_arc('e10', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_line('e11', (25, 40), (29, 37))
        self.add_line('e12', (13, 10), (15, 12))
        self.add_arc('e13', (15, 29), (18, 32), radius_x=3, sweep=False)
        self.add_arc('e14', (41, 8), (44, 11), radius_x=3)
        self.add_arc('e15', (44, 31), (42, 32), radius_x=2)
        self.add_contour('c0', 'e9-1', 'e9-2', 'e0', 'e10', 'e1', 'e11', 'e2')
        self.add_contour('c1', 'e3', 'e12', 'e4', 'e13', 'e5')
        self.add_contour('c2', 'e6', 'e14', 'e7', 'e15', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
