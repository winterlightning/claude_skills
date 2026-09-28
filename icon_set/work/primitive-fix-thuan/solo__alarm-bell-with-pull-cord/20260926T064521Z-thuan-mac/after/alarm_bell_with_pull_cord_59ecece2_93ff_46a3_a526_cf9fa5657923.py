"""Align the final pull-cord segment vertically through the pull-ring center. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '59ecece2-93ff-46a3-a526-cf9fa5657923'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__alarm-bell-with-pull-cord/20260926T064521Z-thuan-mac/reference/safety bell_59ecece2-93ff-46a3-a526-cf9fa5657923.svg'
AUTHOR = 'claude-opus-5-5'

class AlarmBellWithPullCord(Solo48):
    icon_id = 'alarm-bell-with-pull-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('bell', 'alarm', 'cord', 'ring', 'safety', 'signal')

    def build(self):
        """Revision per review: the pull cord leaves the bell's rim centre and sweeps in one
        tangent-continuous curve beneath the bell (two cubics bottoming on y 42) before rising
        straight up to the pull ring, which is larger (r5, was r3). To make room the bell is a
        little narrower: an r8 dome about (17, 18), sides x 9 and 25, flared rim y 30 from x 6 to
        28, and a short hanger nub on top."""
        self.add_line('hanger', (17, 6), (17, 10))
        self.add_arc('dome-left', (9, 18), (17, 10), radius_x=8)
        self.add_arc('dome-right', (17, 10), (25, 18), radius_x=8)
        self.add_line('side-right', (25, 18), (25, 27))
        self.add_line('flare-right', (25, 27), (28, 30))
        self.add_line('rim-right', (28, 30), (17, 30))
        self.add_line('rim-left', (17, 30), (6, 30))
        self.add_line('flare-left', (6, 30), (9, 27))
        self.add_line('side-left', (9, 27), (9, 18))
        self.add_contour('bell', 'dome-left', 'dome-right', 'side-right', 'flare-right', 'rim-right', 'rim-left',
                         'flare-left', 'side-left', closed=True)
        self.add_bezier('cord-sweep', (17, 30), ((17, 36), (21, 42), (27, 42)))
        self.add_bezier('cord-rise', (27, 42), ((33, 42), (37, 40), (37, 36)))
        self.add_line('cord-up', (37, 36), (37, 16))
        self.add_contour('cord', 'cord-sweep', 'cord-rise', 'cord-up')
        cx, cy, r = 37, 11, 5
        self.add_arc('pull-w', (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc('pull-n', (cx, cy - r), (cx + r, cy), radius_x=r)
        self.add_arc('pull-e', (cx + r, cy), (cx, cy + r), radius_x=r)
        self.add_arc('pull-s', (cx, cy + r), (cx - r, cy), radius_x=r)
        self.add_contour('pull', 'pull-w', 'pull-n', 'pull-e', 'pull-s', closed=True)
        self.relate('connect', 'hanger', 'bell')
        self.relate('connect', 'cord', 'bell')
        self.relate('connect', 'cord', 'pull')
