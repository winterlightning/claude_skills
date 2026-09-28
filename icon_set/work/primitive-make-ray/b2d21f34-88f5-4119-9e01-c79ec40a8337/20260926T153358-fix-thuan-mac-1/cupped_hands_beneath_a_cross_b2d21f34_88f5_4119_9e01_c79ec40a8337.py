"""An open palm-up hand holding up a Latin cross.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: the hand is the library's palm-up hand (Lucide `hand-heart`
construction): the palm's upper curve rising from the wrist and running flat
into the thumb, whose rounded tip curls back under, and the fingers reaching
right to a rounded fingertip arc and back along the palm base. The cross
stands on the axis x=24: its upright ends on a node of the thumb's top edge
so the hand carries it, and the crossbar sits in its upper third.
Revision: the rejected drawing gave two upright hands as n-shaped arches that
read as letters (feedback: "hand"); one unmistakable open hand replaces them.
Construction reference: Lucide `hand-heart` (via `hand-holding-heart`) and
`cross` proportions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b2d21f34-88f5-4119-9e01-c79ec40a8337'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupped-hands-beneath-a-cross/20260926T152509Z-thuan-mac-1/reference/religion hands_b2d21f34-88f5-4119-9e01-c79ec40a8337.svg'
AUTHOR = "claude-opus-5-5"

AXIS = 24
CROSS_TOP, BAR_Y, BAR_HALF, FOOT = 8, 14, 7, (24, 24)


class Drawing(Solo48):
    icon_id = 'cupped-hands-beneath-a-cross'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('religion hands', 'hand holding cross')
    keywords = ('religion', 'faith', 'cross', 'christian', 'hand', 'prayer', 'church', 'belief')

    def build(self):
        self.add_line('upright', (AXIS, CROSS_TOP), FOOT)
        self.add_line('crossbar', (AXIS - BAR_HALF, BAR_Y), (AXIS + BAR_HALF, BAR_Y))
        self.relate('connect', 'upright', 'crossbar')
        # palm-up hand
        self.add_arc('palm-upper', (4, 28), (14, 24), radius_x=10, radius_y=4)
        self.add_line('palm-top', (14, 24), (20, 24))
        self.add_line('thumb-top-l', (20, 24), FOOT)
        self.add_line('thumb-top-r', FOOT, (28, 24))
        self.add_arc('thumb-tip-upper', (28, 24), (32, 28), radius_x=4)
        self.add_arc('thumb-tip-lower', (32, 28), (28, 32), radius_x=4)
        self.add_line('thumb-bottom', (28, 32), (18, 32))
        self.add_contour('thumb', 'palm-upper', 'palm-top', 'thumb-top-l', 'thumb-top-r', 'thumb-tip-upper', 'thumb-tip-lower', 'thumb-bottom')
        self.relate('connect', 'upright', 'thumb-top-l')
        self.relate('connect', 'upright', 'thumb-top-r')
        self.add_line('fingers-upper', (32, 28), (38, 28))
        self.add_arc('fingertips', (38, 28), (44, 32), radius_x=6)
        self.add_line('fingers-lower', (44, 32), (34, 40))
        self.add_line('palm-base', (34, 40), (12, 40))
        self.add_line('wrist-lower', (12, 40), (4, 38))
        self.add_contour('hand', 'fingers-upper', 'fingertips', 'fingers-lower', 'palm-base', 'wrist-lower')
        self.relate('connect', 'thumb', 'hand')
