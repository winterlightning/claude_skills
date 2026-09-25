'A walking frame has two outward-sloping legs joined by a rounded upper rail and a horizontal crossbar. A padded grip caps the top, and a small wheel meets the lower-right leg.\n\nConstruction: Two splayed frame legs joined by a top handgrip and transverse brace, with one small wheel. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '208dc93e-b8da-4b4a-9b6c-3dce53244f29'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking assistance_208dc93e-b8da-4b4a-9b6c-3dce53244f29.svg'
AUTHOR = 'gpt-6'

class WalkingFrame(Solo48):
    icon_id = 'walking-frame'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('walker', 'frame', 'mobility', 'accessibility', 'support', 'wheel')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('frame-1-joint-1', (8, 44), (11, 26))
        self.add_line('frame-1-joint-2', (11, 26), (14, 8))
        self.add_line('frame-2', (14, 8), (18, 4))
        self.add_line('frame-3', (18, 4), (30, 4))
        self.add_line('frame-4', (30, 4), (32, 8))
        self.add_line('frame-5-joint-1', (32, 8), (35, 26))
        self.add_line('frame-5-joint-2', (35, 26), (37, 38))
        self.add_line('brace', (11, 26), (35, 26))
        self.add_arc('wheel-top-joint-1', (34, 41), (37, 38), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('wheel-top-joint-2', (37, 38), (40, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('wheel-bottom', (40, 41), (34, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('frame', 'frame-1-joint-1', 'frame-1-joint-2', 'frame-2', 'frame-3', 'frame-4', 'frame-5-joint-1', 'frame-5-joint-2', closed=False)
        self.add_contour('wheel', 'wheel-top-joint-1', 'wheel-top-joint-2', 'wheel-bottom', closed=True)
        self.relate('connect', 'brace', 'frame')
        self.relate('connect', 'wheel', 'frame')
