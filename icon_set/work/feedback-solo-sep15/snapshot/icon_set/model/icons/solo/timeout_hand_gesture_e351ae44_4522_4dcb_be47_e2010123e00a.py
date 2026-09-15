'Two hands form a T shape: an upper hand extends horizontally to the right while a lower index finger points upward against it. The upper wrist has a visible cuff.\n\nConstruction: One horizontal hand forms a T above an upright hand. Small knuckle creases omitted. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e351ae44-4522-4dcb-be47-e2010123e00a'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hands timeout_e351ae44-4522-4dcb-be47-e2010123e00a.svg'
AUTHOR = 'gpt-6'

class TimeoutHandGesture(Solo48):
    icon_id = 'timeout-hand-gesture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('timeout', 'hands', 'gesture', 'sport', 'pause', 'fingers')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('top-hand-1', (8, 4), (32, 4))
        self.add_line('top-hand-2', (32, 4), (40, 8))
        self.add_line('top-hand-3', (40, 8), (40, 12))
        self.add_line('top-hand-4', (40, 12), (28, 12))
        self.add_line('top-hand-5', (28, 12), (24, 16))
        self.add_line('top-hand-6', (24, 16), (8, 12))
        self.add_line('vertical-hand-1', (20, 44), (16, 34))
        self.add_line('vertical-hand-2', (16, 34), (20, 26))
        self.add_line('vertical-hand-3', (20, 26), (20, 16))
        self.add_line('vertical-hand-4-joint-1', (20, 16), (24, 16))
        self.add_line('vertical-hand-4-joint-2', (24, 16), (28, 16))
        self.add_line('vertical-hand-5', (28, 16), (30, 44))
        self.add_contour('top-hand', 'top-hand-1', 'top-hand-2', 'top-hand-3', 'top-hand-4', 'top-hand-5', 'top-hand-6', closed=False)
        self.add_contour('vertical-hand', 'vertical-hand-1', 'vertical-hand-2', 'vertical-hand-3', 'vertical-hand-4-joint-1', 'vertical-hand-4-joint-2', 'vertical-hand-5', closed=False)
        self.relate('connect', 'vertical-hand', 'top-hand')
