"""Falling bomb above a house.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the bomb falls along the diagonal y = x toward the roof and is
mirrored about that axis. Its body is a capsule: an r5 nose cap about (17,17)
whose 3-4-5 end points (21,14)/(14,21) start straight sides 8.5 long, and a
tail fin bar on the line x + y = 23 that overhangs both sides out to the
canvas edges (17,6)/(6,17). The nose stays 9.1 clear of the roof. The house
is a pentagon (walls x=24..42, 45-degree roof peaking at (33,21)).
Revision: the earlier bomb was a small irregular blob; the capsule with
fins pointed at the roof now reads as a falling bomb.
Reduction: the reference's door (an 8-wide arch leaves only 7 to the walls),
roof eaves and motion lines are omitted for spacing.
Construction reference: Lucide `house` (pentagon body), re-authored.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6595335f-49a0-4788-8fa4-1bde23722302'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__falling-bomb-above-house/20260926T125429Z-thuan-mac/reference/refugee immigration war 1_6595335f-49a0-4788-8fa4-1bde23722302.svg'
AUTHOR = 'claude-opus-5-5'

NOSE_C, NOSE_R = (17, 17), 5
BODY_LEN = 6
FIN_OVERHANG = 2
WALL_L, WALL_R, GROUND = 24, 42, 42
PEAK = (33, 21)


def m(p):
    """Mirror about the bomb axis y = x."""
    return (p[1], p[0])


class Drawing(Solo48):
    icon_id = 'falling-bomb-above-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('airstrike', 'bombing')
    keywords = ('bomb', 'house', 'war', 'airstrike', 'building', 'conflict', 'refugee')

    def build(self):
        cx, cy = NOSE_C
        p1 = (cx + 4, cy - 3)                       # (21, 14)
        t1 = (p1[0] - BODY_LEN, p1[1] - BODY_LEN)   # (15, 8)
        fin1 = (t1[0] + FIN_OVERHANG, t1[1] - FIN_OVERHANG)   # (17, 6), on the tail line
        self.add_arc('nose', p1, m(p1), radius_x=NOSE_R, sweep=True)
        self.add_line('side-b', m(p1), m(t1))
        self.add_line('tail', m(t1), t1)
        self.add_line('side-a', t1, p1)
        self.add_contour('bomb', 'nose', 'side-b', 'tail', 'side-a', closed=True)
        # tail fin bar: the tail line extended past both sides
        self.add_line('fin-a', t1, fin1)
        self.add_line('fin-b', m(t1), m(fin1))
        for fin, parts in (('fin-a', ('tail', 'side-a')), ('fin-b', ('tail', 'side-b'))):
            for part in parts:
                self.relate('connect', fin, part)
        # house
        eave_y = PEAK[1] + (PEAK[0] - WALL_L)       # 30
        self.add_line('roof-left', (WALL_L, eave_y), PEAK)
        self.add_line('roof-right', PEAK, (WALL_R, eave_y))
        self.add_line('wall-right', (WALL_R, eave_y), (WALL_R, GROUND))
        self.add_line('ground', (WALL_R, GROUND), (WALL_L, GROUND))
        self.add_line('wall-left', (WALL_L, GROUND), (WALL_L, eave_y))
        self.add_contour('house', 'roof-left', 'roof-right', 'wall-right', 'ground', 'wall-left', closed=True)
