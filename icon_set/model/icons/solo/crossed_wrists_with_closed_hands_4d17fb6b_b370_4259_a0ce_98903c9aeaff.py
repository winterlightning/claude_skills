'Two forearms cross diagonally to form an X below a pair of closed hands. The knuckles face upward, with the thumbs curving inward near the point where the hands meet.\n\nConstruction: Two broad forearms cross below closed fists; back arm is visibly interrupted at the crossing. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d17fb6b-b370-4259-a0ce-98903c9aeaff'
SOURCE_PATH = 'pictographic-primitives/wayfinding/sign language love_4d17fb6b-b370-4259-a0ce-98903c9aeaff.svg'
AUTHOR = 'gpt-6'

class CrossedWristsWithClosedHands(Solo48):
    icon_id = 'crossed-wrists-with-closed-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('hands', 'wrists', 'crossed', 'love', 'gesture', 'sign')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('front-1', (10, 42), (6, 36))
        self.add_line('front-2-joint-1', (6, 36), (18, 21))
        self.add_line('front-2-joint-2', (18, 21), (26, 11))
        self.add_line('front-2-joint-3', (26, 11), (30, 6))
        self.add_line('front-3', (30, 6), (42, 16))
        self.add_line('front-4-joint-1', (42, 16), (30, 29))
        self.add_line('front-4-joint-2', (30, 29), (18, 42))
        self.add_line('back-top-1', (18, 21), (6, 12))
        self.add_line('back-top-2', (6, 12), (12, 6))
        self.add_line('back-top-3', (12, 6), (26, 11))
        self.add_line('back-bottom-1', (30, 29), (42, 38))
        self.add_contour('front', 'front-1', 'front-2-joint-1', 'front-2-joint-2', 'front-2-joint-3', 'front-3', 'front-4-joint-1', 'front-4-joint-2', closed=False)
        self.add_contour('back-top', 'back-top-1', 'back-top-2', 'back-top-3', closed=False)
        self.add_contour('back-bottom', 'back-bottom-1', closed=False)
        self.relate('connect', 'front', 'back-top')
        self.relate('connect', 'front', 'back-bottom')
