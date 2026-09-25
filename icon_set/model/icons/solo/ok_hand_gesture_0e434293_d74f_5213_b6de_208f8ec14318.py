'A hand makes a closed loop with the thumb and index finger at lower-left. Two fingers project upward and the remaining finger curves beside them above the rounded palm.\n\nConstruction: Circular thumb-index loop beneath two extended fingers and a rounded palm. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e434293-d74f-5213-b6de-208f8ec14318'
SOURCE_PATH = 'pictographic-primitives/wayfinding/ok hand_0e434293-d74f-5213-b6de-208f8ec14318.svg'
AUTHOR = 'gpt-6'

class OkHandGesture(Solo48):
    icon_id = 'ok-hand-gesture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('ok', 'hand', 'gesture', 'fingers', 'approval', 'sign')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('finger-loop-top-joint-1', (8, 30), (16, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('finger-loop-top-joint-2', (16, 22), (24, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('finger-loop-bottom-joint-1', (24, 30), (16, 38), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('finger-loop-bottom-joint-2', (16, 38), (8, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('fingers-1', (16, 22), (16, 8))
        self.add_line('fingers-2', (16, 8), (24, 4))
        self.add_line('fingers-3', (24, 4), (28, 22))
        self.add_line('fingers-4', (28, 22), (32, 8))
        self.add_line('fingers-5', (32, 8), (40, 8))
        self.add_line('fingers-6', (40, 8), (40, 32))
        self.add_arc('palm', (40, 32), (28, 44), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('lower-palm', (28, 44), (16, 38))
        self.add_contour('finger-loop', 'finger-loop-top-joint-1', 'finger-loop-top-joint-2', 'finger-loop-bottom-joint-1', 'finger-loop-bottom-joint-2', closed=True)
        self.add_contour('hand', 'fingers-1', 'fingers-2', 'fingers-3', 'fingers-4', 'fingers-5', 'fingers-6', 'palm', 'lower-palm', closed=False)
        self.relate('connect', 'finger-loop', 'hand')
