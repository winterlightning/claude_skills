"""Rectangle with circle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53b43ebd-e80c-4707-942c-9028c9950eeb'
SOURCE_PATH = 'pictographic-primitives/symbol/rectangle with circle_53b43ebd-e80c-4707-942c-9028c9950eeb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RectangleWithCircle(Solo48):
    icon_id = 'rectangle-with-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('rectangle', 'with', 'circle', 'symbol')

    def build(self):
        self.add_line('e0', (26, 20), (18, 6))
        self.add_line('e1', (18, 6), (6, 28))
        self.add_line('e2', (6, 28), (19, 28))
        self.add_arc('e3-top', (20, 31), (42, 31), radius_x=11)
        self.add_arc('e3-bottom', (42, 31), (20, 31), radius_x=11)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e3')
