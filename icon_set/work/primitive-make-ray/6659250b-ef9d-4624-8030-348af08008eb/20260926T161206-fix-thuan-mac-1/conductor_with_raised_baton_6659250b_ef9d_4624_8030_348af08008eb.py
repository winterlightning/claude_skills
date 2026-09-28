"""An orchestra conductor seen from the front, baton raised high.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: a `user.svg` bust: a ring head (r8 about (26,14)) exactly 8
above a flat shoulder line at y=30. Both shoulders round down
(r8 quarter arcs) into straight sides to the ground, mirrored about x=26.
From the shoulder line's left end the raised arm climbs to the hand at
(8,24) and the baton rises from the hand to the top-left corner; from its
right end the other arm reaches out and up to (42,26).
Revision: the rejected drawing's arms bent into a knot and the baton did not
read; the conductor now has a clear bust, one arm lifting a long baton and
the other arm out wide.
Human reference: `user.svg` (ring head, shoulders 8 below it) and
`full_body_ref.png` (straight rounded limbs).
Construction reference: no useful Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6659250b-ef9d-4624-8030-348af08008eb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__conductor-with-raised-baton/20260926T160211Z-thuan-mac-1/reference/conductor_6659250b-ef9d-4624-8030-348af08008eb.svg'
AUTHOR = "claude-opus-5-5"

HEAD, HEAD_R = (26, 14), 8
SHOULDER_L, SHOULDER_R, SHOULDER_Y = 18, 34, 30
CORNER_R = 8
GROUND = 42
HAND, BATON_TIP = (8, 24), (6, 6)
RIGHT_HAND = (42, 26)


class Drawing(Solo48):
    icon_id = 'conductor-with-raised-baton'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('conductor', 'maestro')
    keywords = ('conductor', 'baton', 'orchestra', 'music', 'maestro', 'concert', 'person')

    def build(self):
        hx, hy = HEAD
        ring = [(hx + HEAD_R, hy), (hx, hy + HEAD_R), (hx - HEAD_R, hy), (hx, hy - HEAD_R)]
        for i in range(4):
            self.add_arc(f'head-{i}', ring[i], ring[(i + 1) % 4], radius_x=HEAD_R, sweep=True)
        self.add_contour('head', *[f'head-{i}' for i in range(4)], closed=True)
        sl, sr = (SHOULDER_L, SHOULDER_Y), (SHOULDER_R, SHOULDER_Y)
        c = CORNER_R
        self.add_line('side-left', (SHOULDER_L - c, GROUND), (SHOULDER_L - c, SHOULDER_Y + c))
        self.add_arc('shoulder-left', (SHOULDER_L - c, SHOULDER_Y + c), sl, radius_x=c, sweep=True)
        self.add_line('shoulders', sl, sr)
        self.add_arc('shoulder-right', sr, (SHOULDER_R + c, SHOULDER_Y + c), radius_x=c, sweep=True)
        self.add_line('side-right', (SHOULDER_R + c, SHOULDER_Y + c), (SHOULDER_R + c, GROUND))
        self.add_contour('body', 'side-left', 'shoulder-left', 'shoulders', 'shoulder-right', 'side-right')
        self.mark_human_figure('conductor', head='head', torso='shoulders', torso_junction='start')
        self.add_line('arm-raised', sl, HAND)
        self.add_line('baton', HAND, BATON_TIP)
        self.add_contour('raised', 'arm-raised', 'baton')
        self.relate('connect', 'raised', 'body')
        self.add_line('arm-out', sr, RIGHT_HAND)
        self.relate('connect', 'arm-out', 'body')
