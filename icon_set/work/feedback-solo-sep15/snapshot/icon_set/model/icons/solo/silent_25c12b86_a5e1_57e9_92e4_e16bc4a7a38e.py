"""Silent (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25c12b86-a5e1-57e9-92e4-e16bc4a7a38e'
SOURCE_PATH = 'pictographic-primitives/smileys/silent_25c12b86-a5e1-57e9-92e4-e16bc4a7a38e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Silent(Solo48):
    icon_id = 'silent'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('silent', 'smileys')

    def build(self):
        self.add_line('e0', (30, 17), (30, 21))
        self.add_line('e1', (18, 17), (18, 21))
        self.add_line('e2', (14, 29), (34, 29))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
