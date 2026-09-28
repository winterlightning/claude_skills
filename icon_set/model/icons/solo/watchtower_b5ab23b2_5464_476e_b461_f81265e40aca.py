"""Watchtower (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5ab23b2-5464-476e-b461-f81265e40aca'
SOURCE_PATH = 'pictographic-primitives/video-games/watchtower_b5ab23b2-5464-476e-b461-f81265e40aca.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Watchtower(Solo48):
    icon_id = 'watchtower'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('watchtower', 'video-games')

    def build(self):
        self.add_line('e0', (17, 10), (17, 4))
        self.add_line('e1', (31, 10), (31, 4))
        self.add_line('e2', (17, 4), (8, 4))
        self.add_line('e3', (8, 4), (8, 14))
        self.add_line('e4', (8, 14), (11, 17))
        self.add_line('e5', (11, 18), (11, 29))
        self.add_line('e6', (8, 34), (8, 44))
        self.add_line('e7', (8, 44), (20, 44))
        self.add_line('e8', (20, 44), (20, 36))
        self.add_line('e9', (28, 36), (28, 44))
        self.add_line('e10', (28, 44), (40, 44))
        self.add_line('e11', (40, 44), (40, 33))
        self.add_line('e12', (40, 32), (37, 30))
        self.add_line('e13', (37, 30), (37, 18))
        self.add_line('e14', (40, 14), (40, 4))
        self.add_line('e15', (40, 4), (31, 4))
        self.add_line('e16', (17, 4), (31, 4))
        self.add_arc('e17', (11, 17), (11, 18), radius_x=14, sweep=False)
        self.add_line('e18', (11, 29), (8, 34))
        self.add_arc('e19', (20, 36), (28, 36), radius_x=4)
        self.add_arc('e20', (40, 33), (40, 32), radius_x=34)
        self.add_line('e21', (37, 18), (40, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e17', 'e5', 'e18', 'e6', 'e7', 'e8', 'e19', 'e9', 'e10', 'e11', 'e20', 'e12', 'e13', 'e21', 'e14', 'e15')
        self.add_contour('c3', 'e16')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
