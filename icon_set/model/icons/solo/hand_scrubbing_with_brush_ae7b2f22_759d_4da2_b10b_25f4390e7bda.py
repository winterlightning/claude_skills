'A hand reaches down to grip a broad horizontal scrubbing brush. Several bristles descend from its underside toward a rounded patch of suds spread across the lower-right area.\n\nConstruction: Hand grips a broad scrub brush with three equally spaced bristles. Foam omitted to keep the bristles distinct. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae7b2f22-759d-4da2-b10b-25f4390e7bda'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hand brush bubble_ae7b2f22-759d-4da2-b10b-25f4390e7bda.svg'
AUTHOR = 'gpt-6'

class HandScrubbingWithBrush(Solo48):
    icon_id = 'hand-scrubbing-with-brush'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('hand', 'brush', 'scrubbing', 'cleaning', 'suds', 'washing')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('hand-1', (12, 8), (20, 20))
        self.add_line('hand-2', (20, 20), (32, 20))
        self.add_line('hand-3', (32, 20), (28, 12))
        self.add_line('hand-4', (28, 12), (22, 12))
        self.add_line('brush-0-joint-1', (8, 20), (20, 20))
        self.add_line('brush-0-joint-2', (20, 20), (32, 20))
        self.add_line('brush-0-joint-3', (32, 20), (40, 20))
        self.add_arc('brush-1', (40, 20), (44, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('brush-2', (44, 24), (44, 24))
        self.add_arc('brush-3', (44, 24), (40, 28), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('brush-4-joint-1', (40, 28), (34, 28))
        self.add_line('brush-4-joint-2', (34, 28), (24, 28))
        self.add_line('brush-4-joint-3', (24, 28), (14, 28))
        self.add_line('brush-4-joint-4', (14, 28), (8, 28))
        self.add_arc('brush-5', (8, 28), (4, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('brush-6', (4, 24), (4, 24))
        self.add_arc('brush-7', (4, 24), (8, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bristle-14', (14, 28), (14, 40))
        self.add_line('bristle-24', (24, 28), (24, 40))
        self.add_line('bristle-34', (34, 28), (34, 40))
        self.add_contour('hand', 'hand-1', 'hand-2', 'hand-3', 'hand-4', closed=False)
        self.add_contour('brush', 'brush-0-joint-1', 'brush-0-joint-2', 'brush-0-joint-3', 'brush-1', 'brush-2', 'brush-3', 'brush-4-joint-1', 'brush-4-joint-2', 'brush-4-joint-3', 'brush-4-joint-4', 'brush-5', 'brush-6', 'brush-7', closed=True)
        self.relate('connect', 'hand', 'brush')
        self.relate('connect', 'bristle-14', 'brush')
        self.relate('connect', 'bristle-24', 'brush')
        self.relate('connect', 'bristle-34', 'brush')
