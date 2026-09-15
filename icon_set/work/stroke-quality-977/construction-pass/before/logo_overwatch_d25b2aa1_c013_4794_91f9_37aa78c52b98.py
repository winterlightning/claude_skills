"""Logo overwatch (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd25b2aa1-c013-4794-91f9-37aa78c52b98'
SOURCE_PATH = 'pictographic-primitives/video-games/logo overwatch_d25b2aa1-c013-4794-91f9-37aa78c52b98.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class LogoOverwatch(Solo48):
    icon_id = 'logo-overwatch'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('logo', 'overwatch', 'video-games')

    def build(self):
        self.add_line('e0', (24, 16), (24, 24))
        self.add_line('e1', (24, 24), (38, 38))
        self.add_line('e2', (24, 24), (10, 38))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c2', 'e3')
