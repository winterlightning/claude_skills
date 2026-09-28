"""An open palm-up hand offering a heart: donation, charity and care.

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: the library's palm-up hand (Lucide `hand-heart`, as in
`hand-holding-heart`): the palm's upper curve rising from the wrist into the
thumb, whose rounded tip curls back under, and the fingers reaching right to
a rounded fingertip arc and back along the palm base. The heart is mirrored
about x=24: two r6 lobes meeting in a notch, r5 shoulders and straight sides
to its point, which rests on a node of the thumb's top edge.
Revision: the rejected drawing's two upright hands were bent strokes that
read as letters; one unmistakable open hand now offers the heart.
Construction reference: Lucide `hand-heart`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e4e00065-3df8-4a4e-8fb9-e6dda357af8f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-hands-beneath-floating-heart/20260926T160211Z-thuan-mac-1/reference/donation charity hand care heart_e4e00065-3df8-4a4e-8fb9-e6dda357af8f.svg'
AUTHOR = 'claude-opus-5-5'


class Drawing(Solo48):
    icon_id = 'open-hands-beneath-floating-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('donation charity hand care heart', 'hand with heart')
    keywords = ('donation', 'charity', 'care', 'heart', 'hand', 'give', 'love', 'volunteer')

    def build(self):
        cx, y, r, tip = 24, 14, 6, 24
        self.add_arc('heart-l', (cx, y), (cx - 2 * r, y), radius_x=r, sweep=False)
        self.add_arc('heart-shl', (cx - 2 * r, y), (cx - 2 * r + 2, y + 4), radius_x=5, sweep=False)
        self.add_line('heart-sl', (cx - 2 * r + 2, y + 4), (cx, tip))
        self.add_line('heart-sr', (cx, tip), (cx + 2 * r - 2, y + 4))
        self.add_arc('heart-shr', (cx + 2 * r - 2, y + 4), (cx + 2 * r, y), radius_x=5, sweep=False)
        self.add_arc('heart-r', (cx + 2 * r, y), (cx, y), radius_x=r, sweep=False)
        self.add_contour('heart', 'heart-l', 'heart-shl', 'heart-sl', 'heart-sr', 'heart-shr', 'heart-r', closed=True)
        self.add_arc('palm-upper', (4, 28), (20, 24), radius_x=16, radius_y=8)
        self.add_line('thumb-top-l', (20, 24), (24, 24))
        self.add_line('thumb-top-r', (24, 24), (28, 24))
        self.add_arc('thumb-tip-upper', (28, 24), (32, 28), radius_x=4)
        self.add_arc('thumb-tip-lower', (32, 28), (28, 32), radius_x=4)
        self.add_line('thumb-bottom', (28, 32), (18, 32))
        self.add_contour('thumb', 'palm-upper', 'thumb-top-l', 'thumb-top-r', 'thumb-tip-upper', 'thumb-tip-lower', 'thumb-bottom')
        self.relate('connect', 'heart', 'thumb')
        self.add_line('fingers-upper', (32, 28), (38, 28))
        self.add_arc('fingertips', (38, 28), (44, 32), radius_x=6)
        self.add_line('fingers-lower', (44, 32), (34, 40))
        self.add_line('palm-base', (34, 40), (12, 40))
        self.add_line('wrist-lower', (12, 40), (4, 38))
        self.add_contour('hand', 'fingers-upper', 'fingertips', 'fingers-lower', 'palm-base', 'wrist-lower')
        self.relate('connect', 'thumb', 'hand')
