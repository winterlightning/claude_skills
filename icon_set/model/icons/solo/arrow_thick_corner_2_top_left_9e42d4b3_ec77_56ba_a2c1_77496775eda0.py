"""Arrow thick corner 2 top left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e42d4b3-ec77-56ba-a2c1-77496775eda0'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick corner 2 top left_9e42d4b3-ec77-56ba-a2c1-77496775eda0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThickCorner2TopLeft(Solo48):
    icon_id = 'arrow-thick-corner-2-top-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'top', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (42, 42), (6, 6))
        self.add_line('e1', (6, 6), (42, 6))
        self.add_line('e2', (6, 6), (6, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
