'A head and shoulder appear behind a raised arm holding a small rounded washing pad against the cheek. Two bubbles float beside the pad, and the face has no interior features.\n\nConstruction: Head and shoulder beside a diagonal cloth-covered hand, with one soap bubble. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38f93e3b-3368-5ce7-82af-b9f5884e7642'
SOURCE_PATH = 'pictographic-primitives/wayfinding/cleanser scrubing_38f93e3b-3368-5ce7-82af-b9f5884e7642.svg'
AUTHOR = 'gpt-6'

class PersonScrubbingFace(Solo48):
    icon_id = 'person-scrubbing-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'face', 'scrubbing', 'washing', 'pad', 'hygiene')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (20, 16), (40, 16), radius_x=10, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('head-lower', (40, 16), (30, 28), radius_x=10, radius_y=12, large_arc=False, sweep=True)
        self.add_line('shoulder-1', (30, 28), (30, 34))
        self.add_line('shoulder-2', (30, 34), (40, 38))
        self.add_line('shoulder-3', (40, 38), (40, 44))
        self.add_line('cloth-hand-1', (8, 36), (16, 44))
        self.add_line('cloth-hand-2', (16, 44), (30, 28))
        self.add_line('cloth-hand-3', (30, 28), (22, 20))
        self.add_line('cloth-hand-4', (22, 20), (8, 36))
        self.add_line('soap', (8, 16), (8, 16))
        self.add_contour('head', 'head-top', 'head-lower', closed=False)
        self.add_contour('shoulder', 'shoulder-1', 'shoulder-2', 'shoulder-3', closed=False)
        self.add_contour('cloth-hand', 'cloth-hand-1', 'cloth-hand-2', 'cloth-hand-3', 'cloth-hand-4', closed=True)
        self.relate('connect', 'shoulder', 'head')
        self.relate('connect', 'cloth-hand', 'head')
        self.relate('connect', 'cloth-hand', 'shoulder')
