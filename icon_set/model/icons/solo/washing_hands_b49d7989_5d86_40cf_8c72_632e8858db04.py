'Two hands overlap horizontally with their fingers pointing right. The rear hand angles down across the front palm, and two small round bubbles float above the joined hands.\n\nConstruction: One open hand beneath a second hand and one washing droplet. Finger creases omitted. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b49d7989-5d86-40cf-8c72-632e8858db04'
SOURCE_PATH = 'pictographic-primitives/wayfinding/washing hand_b49d7989-5d86-40cf-8c72-632e8858db04.svg'
AUTHOR = 'gpt-6'

class WashingHands(Solo48):
    icon_id = 'washing-hands'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('hands', 'washing', 'soap', 'hygiene', 'cleaning', 'palms')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('lower-hand-1', (4, 32), (4, 24))
        self.add_line('lower-hand-2', (4, 24), (18, 16))
        self.add_line('lower-hand-3', (18, 16), (22, 20))
        self.add_line('lower-hand-4', (22, 20), (16, 26))
        self.add_line('lower-hand-5', (16, 26), (38, 26))
        self.add_line('lower-hand-6', (38, 26), (44, 30))
        self.add_line('lower-hand-7', (44, 30), (44, 36))
        self.add_line('lower-hand-8', (44, 36), (40, 40))
        self.add_line('lower-hand-9', (40, 40), (16, 40))
        self.add_line('lower-hand-10', (16, 40), (4, 32))
        self.add_line('lower-hand-11', (4, 32), (4, 32))
        self.add_line('upper-hand-1', (20, 8), (28, 8))
        self.add_line('upper-hand-2', (28, 8), (44, 20))
        self.add_line('drop-left', (8, 10), (8, 10))
        self.add_contour('lower-hand', 'lower-hand-1', 'lower-hand-2', 'lower-hand-3', 'lower-hand-4', 'lower-hand-5', 'lower-hand-6', 'lower-hand-7', 'lower-hand-8', 'lower-hand-9', 'lower-hand-10', 'lower-hand-11', closed=True)
        self.add_contour('upper-hand', 'upper-hand-1', 'upper-hand-2', closed=False)
