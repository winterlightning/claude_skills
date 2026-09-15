"""Astronomy blackhole (science), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6e3210e-16d6-594e-b7d4-c8d497384b4e'
SOURCE_PATH = 'pictographic-primitives/science/astronomy blackhole_a6e3210e-16d6-594e-b7d4-c8d497384b4e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AstronomyBlackhole(Solo48):
    icon_id = 'astronomy-blackhole'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('astronomy', 'blackhole', 'science')

    def build(self):
        self.add_line('e0', (24, 8), (24, 17))
        self.add_line('e1', (4, 24), (17, 24))
        self.add_line('e2', (24, 40), (24, 31))
        self.add_line('e3', (31, 24), (44, 24))
        self.add_arc('e4-top', (17, 24), (31, 24), radius_x=7)
        self.add_arc('e4-bottom', (31, 24), (17, 24), radius_x=7)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c3', 'e4')
