"""A person crouched under a sturdy table while the ground shakes above.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: a seismic zigzag runs across the top (45-degree strokes, 12
apart, peaks at y 8 and 14). The table is a top line with a leg line hung
from each end, x=4 and x=44, the top at y=23. Under it a person crouches in the duck
and cover pose: a ring head (r3, the exempt circle) low at the front, and a
torso that starts level beside the head exactly 8 from its outline, rises in
a rounded back (r4 hump, 9 under the table top) and drops to the knee on the floor.
Revision: the rejected drawing gave a dotted ring and a bent line inside an
open frame that did not read; the table now has a clear top and legs, a
continuous shake line tops it and the figure has a head and hunched back.
Human reference: `full_body_ref.png` (round head, simple rounded torso),
detached head gap 8 on centerlines.
Construction reference: no useful Lucide match (`table` checked for the
top-and-legs outline).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d2595e2-135f-48bd-8886-08c5da475869'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__earthquake-hiding-proof-table/20260926T152509Z-thuan-mac-1/reference/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg'
AUTHOR = 'claude-opus-5-5'

ZIG_LOW, ZIG_HIGH, ZIG_STEP = 14, 8, 6
TABLE_TOP, FLOOR, LEG_L, LEG_R = 23, 40, 4, 44
HEAD, HEAD_R = (15, 36), 3
NECK = (26, 36)          # HEAD outline (18,36) + 8
BACK_L, BACK_R, HUMP_R = (27, 36), (35, 36), 4


class Drawing(Solo48):
    icon_id = 'earthquake-hiding-proof-table'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('earthquake hiding proof table', 'duck and cover')
    keywords = ('earthquake', 'table', 'shelter', 'hide', 'safety', 'disaster', 'drill', 'person')

    def build(self):
        pts = []
        x, up = 6, False
        while x <= 42:
            pts.append((x, ZIG_HIGH if up else ZIG_LOW))
            x += ZIG_STEP
            up = not up
        self.add_polyline('quake', *pts)
        self.add_line('table-top', (LEG_L, TABLE_TOP), (LEG_R, TABLE_TOP))
        self.add_line('leg-left', (LEG_L, TABLE_TOP), (LEG_L, FLOOR))
        self.add_line('leg-right', (LEG_R, TABLE_TOP), (LEG_R, FLOOR))
        self.relate('connect', 'leg-left', 'table-top')
        self.relate('connect', 'leg-right', 'table-top')
        hx, hy = HEAD
        ring = [(hx + HEAD_R, hy), (hx, hy + HEAD_R), (hx - HEAD_R, hy), (hx, hy - HEAD_R)]
        for i in range(4):
            self.add_arc(f'head-{i}', ring[i], ring[(i + 1) % 4], radius_x=HEAD_R, sweep=True)
        self.add_contour('head', *[f'head-{i}' for i in range(4)], closed=True)
        self.add_line('torso', NECK, BACK_L)
        self.add_arc('back', BACK_L, BACK_R, radius_x=HUMP_R, sweep=True)
        self.add_line('thigh', BACK_R, (BACK_R[0], FLOOR))
        self.add_contour('body', 'torso', 'back', 'thigh')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
