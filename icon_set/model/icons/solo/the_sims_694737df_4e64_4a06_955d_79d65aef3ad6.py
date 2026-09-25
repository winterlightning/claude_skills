"""The sims (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '694737df-4e64-4a06-955d-79d65aef3ad6'
SOURCE_PATH = 'pictographic-primitives/video-games/the sims_694737df-4e64-4a06-955d-79d65aef3ad6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class TheSims(Solo48):
    icon_id = 'the-sims'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('the', 'sims', 'video-games')

    def build(self):
        self.add_line('e0', (24, 4), (24, 24))
        self.add_line('e1', (24, 4), (8, 24))
        self.add_line('e2', (24, 4), (40, 24))
        self.add_line('e3', (24, 24), (40, 24))
        self.add_line('e4', (24, 24), (24, 44))
        self.add_line('e5', (24, 24), (8, 24))
        self.add_line('e6', (40, 24), (24, 44))
        self.add_line('e7', (24, 44), (8, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c6', 'c7')
