"""Images (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94993cb5-32ce-48f8-ba6f-9fe516a4704d'
SOURCE_PATH = 'pictographic-primitives/state/images_94993cb5-32ce-48f8-ba6f-9fe516a4704d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Images(Solo48):
    icon_id = 'images'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('images', 'state')

    def build(self):
        self.add_line('e0', (44, 33), (34, 22))
        self.add_line('e1', (27, 23), (11, 40))
        self.add_line('e2', (44, 30), (44, 40))
        self.add_line('e3', (44, 40), (4, 40))
        self.add_line('e4', (4, 40), (4, 8))
        self.add_line('e5', (4, 8), (44, 8))
        self.add_line('e6', (44, 8), (44, 30))
        self.add_arc('e7', (34, 22), (27, 23), radius_x=4, sweep=False)
        self.add_dot('e8', (13, 19))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
