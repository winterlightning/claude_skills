"""A five-petal flower on a straight stem with one leaf (a corsage bloom).

SOLO48 VRECT_M: visible (8, 2)-(40, 46), centerline (10, 4)-(38, 44).

Symbol plan: mirrored about x=24. The head is one scalloped outline of five
petal arcs around a centre dot at (24,17), with notches at (30,10), (33,19)
and (24,26) (and their mirrors), each 9 from the dot, whose petal centres
fall at 0, 72 and 141 degrees: the top petal is a r6 semicircle reaching
y=4, the upper side petals are r5 arcs about (33,14) reaching x=38, and the
lower petals are r6 arcs meeting at the bottom notch. The stem drops from
that notch to the ground; a lens-shaped leaf (two r8 arcs) springs from it
to the lower left.
Revision: the rejected drawing's head was a lumpy blob; the petals are now
five even rounded lobes around a centre, so it reads as a flower.
Construction reference: Lucide `flower` (petal lobes round a centre) and
`sprout` (leaf off the stem).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f5ba3e5a-1e84-4926-9afb-e69a52e23191'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__five-petal-flower-with-side-leaf/20260926T152509Z-thuan-mac-1/reference/corsage_f5ba3e5a-1e84-4926-9afb-e69a52e23191.svg'
AUTHOR = 'claude-opus-5-5'

AXIS = 24
CENTER = (24, 17)
N_TOP, N_SIDE, N_BOTTOM = (30, 10), (33, 19), (24, 26)
TOP_R, SIDE_R, LOW_R = 6, 5, 6
GROUND = 44
LEAF_BASE, LEAF_TIP, LEAF_R = (24, 41), (12, 36), 8


def mx(p):
    return (2 * AXIS - p[0], p[1])


class Drawing(Solo48):
    icon_id = 'five-petal-flower-with-side-leaf'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('corsage', 'flower with leaf')
    keywords = ('flower', 'corsage', 'blossom', 'petal', 'plant', 'bloom', 'garden', 'nature')

    def build(self):
        self.add_arc('petal-top', mx(N_TOP), N_TOP, radius_x=TOP_R, sweep=True)
        self.add_arc('petal-right', N_TOP, N_SIDE, radius_x=SIDE_R, large_arc=True, sweep=True)
        self.add_arc('petal-low-right', N_SIDE, N_BOTTOM, radius_x=LOW_R, sweep=True)
        self.add_arc('petal-low-left', N_BOTTOM, mx(N_SIDE), radius_x=LOW_R, sweep=True)
        self.add_arc('petal-left', mx(N_SIDE), mx(N_TOP), radius_x=SIDE_R, large_arc=True, sweep=True)
        self.add_contour('head', 'petal-top', 'petal-right', 'petal-low-right', 'petal-low-left', 'petal-left', closed=True)
        self.add_dot('centre', CENTER)
        self.add_line('stem-upper', N_BOTTOM, LEAF_BASE)
        self.add_line('stem-lower', LEAF_BASE, (AXIS, GROUND))
        self.add_contour('stem', 'stem-upper', 'stem-lower')
        self.relate('connect', 'stem', 'head')
        self.add_arc('leaf-upper', LEAF_BASE, LEAF_TIP, radius_x=LEAF_R, sweep=False)
        self.add_arc('leaf-lower', LEAF_TIP, LEAF_BASE, radius_x=LEAF_R, sweep=False)
        self.add_contour('leaf', 'leaf-upper', 'leaf-lower', closed=True)
        self.relate('connect', 'leaf', 'stem')
