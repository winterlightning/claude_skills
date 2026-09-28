"""A desk globe: a ball with its equator and a meridian, on a stem and base.

SOLO48 VRECT_L: visible (6, 2)-(42, 46), centerline (8, 4)-(40, 44).

Symbol plan: mirrored about x=24. The globe is a r16 circle about (24,20)
built from four cardinal quarter arcs. Inside it, the Lucide globe grid: a
meridian ellipse (rx7, ry16) from pole to pole, split at the equator, and
the equator line crossing both, split where they meet so every junction is
a shared node. A short stem drops from the south pole to split a flat base
line.
Revision: the rejected drawing set a bare ring beside a C-shaped arc on a
bar and read as a letter; the globe grid and the stand now read as a desk
globe. The reference's side meridian ring was dropped: with the ball wide
enough to carry a grid there is no room for a concentric ring 8 clear of it.
Construction reference: Lucide `globe` (circle, meridian ellipse, equator).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a5e62027-4155-4c3f-9eea-0fcf4e0f687b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__earth-model-1/20260926T152509Z-thuan-mac-1/reference/earth model 1_a5e62027-4155-4c3f-9eea-0fcf4e0f687b.svg'
AUTHOR = 'claude-opus-5-5'

AXIS = 24
CENTER, BALL_R, MERIDIAN_RX = (24, 20), 16, 7
BASE_Y, BASE_HALF = 44, 8


class Drawing(Solo48):
    icon_id = 'earth-model-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('earth model 1', 'desk globe')
    keywords = ('globe', 'earth', 'world', 'geography', 'school', 'map', 'planet', 'desk globe')

    def build(self):
        cx, cy = CENTER
        east, south, west, north = (cx + BALL_R, cy), (cx, cy + BALL_R), (cx - BALL_R, cy), (cx, cy - BALL_R)
        self.add_arc('ball-se', east, south, radius_x=BALL_R, sweep=True)
        self.add_arc('ball-sw', south, west, radius_x=BALL_R, sweep=True)
        self.add_arc('ball-nw', west, north, radius_x=BALL_R, sweep=True)
        self.add_arc('ball-ne', north, east, radius_x=BALL_R, sweep=True)
        self.add_contour('ball', 'ball-se', 'ball-sw', 'ball-nw', 'ball-ne', closed=True)
        m_e, m_w = (cx + MERIDIAN_RX, cy), (cx - MERIDIAN_RX, cy)
        kw = dict(radius_x=MERIDIAN_RX, radius_y=BALL_R)
        self.add_arc('meridian-ne', north, m_e, sweep=True, **kw)
        self.add_arc('meridian-se', m_e, south, sweep=True, **kw)
        self.add_arc('meridian-sw', south, m_w, sweep=True, **kw)
        self.add_arc('meridian-nw', m_w, north, sweep=True, **kw)
        self.add_contour('meridian', 'meridian-ne', 'meridian-se', 'meridian-sw', 'meridian-nw', closed=True)
        self.add_line('equator-w', west, m_w)
        self.add_line('equator-c', m_w, m_e)
        self.add_line('equator-e', m_e, east)
        self.add_contour('equator', 'equator-w', 'equator-c', 'equator-e')
        self.relate('connect', 'meridian', 'ball')
        self.relate('connect', 'equator', 'ball')
        self.relate('connect', 'equator', 'meridian')
        self.add_line('stem', south, (AXIS, BASE_Y))
        self.relate('connect', 'stem', 'ball')
        self.relate('connect', 'stem', 'meridian')
        self.add_line('base-left', (AXIS - BASE_HALF, BASE_Y), (AXIS, BASE_Y))
        self.add_line('base-right', (AXIS, BASE_Y), (AXIS + BASE_HALF, BASE_Y))
        self.relate('connect', 'stem', 'base-left')
        self.relate('connect', 'stem', 'base-right')
        self.relate('connect', 'base-left', 'base-right')
