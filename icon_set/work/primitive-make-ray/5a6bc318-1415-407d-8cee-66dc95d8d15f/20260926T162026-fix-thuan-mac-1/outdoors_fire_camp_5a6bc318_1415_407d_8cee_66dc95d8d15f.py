"""A campfire: a flickering flame over two crossed logs.

SOLO48 VRECT_L: visible (6, 2)-(42, 46), centerline (8, 4)-(40, 44).

Symbol plan: the flame is one closed outline: a r9 round base about (24,17)
from (15,17) through the bottom (24,26) to (33,17); both sides sweep up
(one cubic each, vertical at the base) to a tip leaning right at (28,4),
the left side in a long S-curve so the flame flickers rather than reading
as a drop. The logs cross
under it on an exact integer node (24,38): from (8,32) to (40,44) and from
(40,32) to (8,44); the flame's base is 12 above the crossing.
Revision: the rejected drawing's round blob with an inner hook did not read
as fire (feedback: "fire"); the flame now has a pointed leaning tip and
sits over crossed logs.
Construction reference: Lucide `flame` (base bowl, leaning tip) and `flame-kindling` (crossed logs).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5a6bc318-1415-407d-8cee-66dc95d8d15f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__outdoors-fire-camp/20260926T160211Z-thuan-mac-1/reference/outdoors fire camp_5a6bc318-1415-407d-8cee-66dc95d8d15f.svg'
AUTHOR = "claude-opus-5-5"

BASE, BASE_R = (24, 17), 9
TIP = (28, 4)
LOG_A, LOG_B, CROSS = ((8, 32), (40, 44)), ((40, 32), (8, 44)), (24, 38)


class Drawing(Solo48):
    icon_id = 'outdoors-fire-camp'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('outdoors fire camp', 'campfire', 'bonfire')
    keywords = ('fire', 'campfire', 'flame', 'camping', 'outdoors', 'logs', 'bonfire', 'warmth')

    def build(self):
        bx, by = BASE
        left, bottom, right = (bx - BASE_R, by), (bx, by + BASE_R), (bx + BASE_R, by)
        self.add_arc('base-l', left, bottom, radius_x=BASE_R, sweep=False)
        self.add_arc('base-r', bottom, right, radius_x=BASE_R, sweep=False)
        self.add_bezier('right-side', right, ((33, 12), (31, 8), TIP))
        self.add_bezier('left-side', TIP, ((22, 9), (15, 11), left))
        self.add_contour('flame', 'base-l', 'base-r', 'right-side', 'left-side', closed=True)
        for name, (a, b) in (('log-a', LOG_A), ('log-b', LOG_B)):
            self.add_line(f'{name}-1', a, CROSS)
            self.add_line(f'{name}-2', CROSS, b)
            self.add_contour(name, f'{name}-1', f'{name}-2')
        self.relate('connect', 'log-a', 'log-b')
