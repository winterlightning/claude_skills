"""Arrow rectangle left svg180 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18fda562-75c1-5d7b-8bc2-26a3a57e4ecf'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle left svg180_18fda562-75c1-5d7b-8bc2-26a3a57e4ecf.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleLeftSvg180Arrows(Solo48):
    icon_id = 'arrow-rectangle-left-svg180-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'svg180', 'arrows')

    def build(self):
        self.add_line('e0', (20, 33), (29, 24))
        self.add_line('e1', (29, 24), (20, 15))
        self.add_line('e2', (6, 41), (8, 42))
        self.add_line('e3', (8, 42), (41, 42))
        self.add_line('e4', (42, 28), (42, 7))
        self.add_line('e5', (40, 6), (7, 6))
        self.add_line('e6', (7, 6), (6, 8))
        self.add_line('e7', (6, 8), (6, 41))
        self.add_bezier('e8', (41, 42), ((41.507, 40.208), (41.681, 38.326), (41.763, 36.477)), ((41.869, 34.186), (41.992, 31.887), (41.992, 29.596)), ((41.992, 29.261), (42, 28.934), (42, 28.606)), ((42, 28.435), (42, 28.172), (42, 28)))
        self.add_bezier('e9', (42, 7), ((41.517, 6.648), (40.646, 6), (40, 6)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e6', 'e7', closed=True)
