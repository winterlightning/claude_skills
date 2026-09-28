"""A radio antenna broadcasts above a trapezoidal airport base.

Construction: radio-tower: mirrored wave arcs, centered transmitter and tapering support.
Reduction: One wave per side; omitted doorway, intermediate box and head divider.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '58573359-f61e-52a8-b710-7818357fd8e0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airport-signal-antenna/20260926T064521Z-thuan-mac/reference/airport signal_58573359-f61e-52a8-b710-7818357fd8e0.svg'
AUTHOR = 'claude-opus-5-5'


class AirportSignalAntenna(Solo48):
    icon_id = 'airport-signal-antenna'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "primitives")
    aliases = ()
    keywords = ('airport', 'antenna', 'signal', 'radar', 'radio', 'waves', 'tower', 'communication')

    def build(self) -> None:
        # Revision attempt per review: the round head becomes a wide rounded rectangle
        # (19, 6)-(29, 14), r3 corners, on the stem. The requested second (inner, shorter) signal
        # arc on each side does not fit: outer arc, inner arc and head each need 8 units of
        # clearance, i.e. 2 * (4 + 8 + 3 + 8) = 46 units plus the head's width, and SOLO48 has 40
        # (HRECT_L) at most. Only the outer, tall arcs remain.
        self.add_arc('wave-left', (10, 6), (10, 26), radius_x=4, radius_y=10, sweep=False)
        self.add_arc('wave-right', (38, 6), (38, 26), radius_x=4, radius_y=10)
        l, t, r, b, c = 19, 6, 29, 14, 3
        self.add_line('head-top', (l + c, t), (r - c, t))
        self.add_arc('head-ne', (r - c, t), (r, t + c), radius_x=c)
        self.add_line('head-right', (r, t + c), (r, b - c))
        self.add_arc('head-se', (r, b - c), (r - c, b), radius_x=c)
        self.add_line('head-bottom-right', (r - c, b), (24, b))
        self.add_line('head-bottom-left', (24, b), (l + c, b))
        self.add_arc('head-sw', (l + c, b), (l, b - c), radius_x=c)
        self.add_line('head-left', (l, b - c), (l, t + c))
        self.add_arc('head-nw', (l, t + c), (l + c, t), radius_x=c)
        self.add_contour('head', 'head-top', 'head-ne', 'head-right', 'head-se', 'head-bottom-right',
                         'head-bottom-left', 'head-sw', 'head-left', 'head-nw', closed=True)
        self.add_line('stem', (24, 14), (24, 30))
        self.add_polyline('base', (18, 30), (24, 30), (30, 30), (36, 42), (12, 42), closed=True)
        self.relate('connect', 'head', 'stem')
        self.relate('connect', 'stem', 'base')
