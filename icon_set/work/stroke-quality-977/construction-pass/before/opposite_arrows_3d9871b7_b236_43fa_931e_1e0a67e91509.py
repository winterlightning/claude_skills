"""Opposite arrows (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d9871b7-b236-43fa-931e-1e0a67e91509'
SOURCE_PATH = 'pictographic-primitives/symbol/opposite arrows_3d9871b7-b236-43fa-931e-1e0a67e91509.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class OppositeArrows(Solo48):
    icon_id = 'opposite-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('opposite', 'arrows', 'symbol')

    def build(self):
        self.add_line('e0', (12, 8), (12, 40))
        self.add_line('e1', (4, 31), (12, 40))
        self.add_line('e2', (21, 31), (12, 40))
        self.add_line('e3', (27, 18), (35, 8))
        self.add_line('e4', (35, 40), (35, 8))
        self.add_line('e5', (44, 18), (35, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
