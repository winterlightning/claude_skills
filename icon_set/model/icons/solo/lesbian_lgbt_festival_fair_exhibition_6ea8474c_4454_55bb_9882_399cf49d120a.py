"""Festival bunting strung above a big heart: a pride fair / exhibition.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: mirrored about x=24. A bunting string runs across the top at
y=6 with two pennants hanging from its ends, each a triangle 12 wide and 10
deep (inradius 3.4), 12 apart so they read as separate flags (three
pennants 8 apart would need 52 units). Below, the
library heart (the `hand-holding-heart` heart at r6): two r6 lobes meeting
in a notch, r5 shoulders and straight sides to the tip at (24,42).
Revision: the rejected drawing merged three pennants into a solid zigzag and
flattened the heart into a bowl; the pennants are now open flags on a
string and the heart has full lobes and a point.
Construction reference: Lucide `heart` and `party-popper` bunting.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ea8474c-4454-55bb-9882-399cf49d120a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lesbian-lgbt-festival-fair-exhibition/20260926T160211Z-thuan-mac-1/reference/lesbian lgbt festival fair exhibition_6ea8474c-4454-55bb-9882-399cf49d120a.svg'
AUTHOR = 'claude-opus-5-5'

STRING_Y, PENNANT_W, PENNANT_D = 6, 12, 10
PENNANT_XS = (6, 30)              # left corner of each pennant
HEART_CX, HEART_Y, HEART_R, HEART_TIP = 24, 30, 6, 42


class Drawing(Solo48):
    icon_id = 'lesbian-lgbt-festival-fair-exhibition'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('lesbian lgbt festival fair exhibition', 'pride festival')
    keywords = ('lgbt', 'lesbian', 'pride', 'festival', 'fair', 'bunting', 'heart', 'love', 'celebration')

    def build(self):
        for i, x in enumerate(PENNANT_XS):
            a, b, tip = (x, STRING_Y), (x + PENNANT_W, STRING_Y), (x + PENNANT_W // 2, STRING_Y + PENNANT_D)
            self.add_line(f'pennant-{i}-top', a, b)
            self.add_line(f'pennant-{i}-r', b, tip)
            self.add_line(f'pennant-{i}-l', tip, a)
            self.add_contour(f'pennant-{i}', f'pennant-{i}-top', f'pennant-{i}-r', f'pennant-{i}-l', closed=True)
        self.add_line('string', (PENNANT_XS[0] + PENNANT_W, STRING_Y), (PENNANT_XS[1], STRING_Y))
        self.relate('connect', 'string', 'pennant-0')
        self.relate('connect', 'string', 'pennant-1')
        cx, y, r, tip = HEART_CX, HEART_Y, HEART_R, HEART_TIP
        self.add_arc('heart-l', (cx, y), (cx - 2 * r, y), radius_x=r, sweep=False)
        self.add_arc('heart-shl', (cx - 2 * r, y), (cx - 2 * r + 2, y + 4), radius_x=5, sweep=False)
        self.add_line('heart-sl', (cx - 2 * r + 2, y + 4), (cx, tip))
        self.add_line('heart-sr', (cx, tip), (cx + 2 * r - 2, y + 4))
        self.add_arc('heart-shr', (cx + 2 * r - 2, y + 4), (cx + 2 * r, y), radius_x=5, sweep=False)
        self.add_arc('heart-r', (cx + 2 * r, y), (cx, y), radius_x=r, sweep=False)
        self.add_contour('heart', 'heart-l', 'heart-shl', 'heart-sl', 'heart-sr', 'heart-shr', 'heart-r', closed=True)
