"""A dog's paw resting in an open palm-up hand ("give paw" training).

SOLO48 HRECT_L: visible (2, 6)-(46, 42), centerline (4, 8)-(44, 40).

Symbol plan: the hand is the library's palm-up hand (Lucide `hand-heart`
construction): the palm's upper curve rising from the wrist and running flat
into the thumb, whose rounded tip curls back under, and the fingers reaching
right to a rounded fingertip arc and back along the palm base. The paw is
mirrored about x=22: a pad dome (rx6, ry7) standing on the thumb's top edge,
whose two feet split that edge, and three toe beans as dots fanned above it.
Revision: the rejected drawing merged a dog head and a hand into one
unreadable outline (feedback: meaning); the paw print on a clear open hand
now carries "dog gives paw".
Construction reference: Lucide `hand-heart` (via `hand-holding-heart`) and
`paw-print` (pad with separate toe beans).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '511ea518-3b8b-552d-b9df-827c71ed2c6b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dog-paw-on-hand/20260926T152509Z-thuan-mac-1/reference/dog training giving hand paw_511ea518-3b8b-552d-b9df-827c71ed2c6b.svg'
AUTHOR = "claude-opus-5-5"

PAW_AXIS = 22
PAD_L, PAD_R, PAD_RX, PAD_RY = (16, 24), (28, 24), 6, 7
TOES = ((13, 12), (22, 8), (31, 12))


class Drawing(Solo48):
    icon_id = 'dog-paw-on-hand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('dog training giving hand paw', 'give paw')
    keywords = ('dog', 'paw', 'hand', 'training', 'pet', 'trick', 'shake', 'animal care')

    def build(self):
        for i, toe in enumerate(TOES):
            self.add_dot(f'toe-{i}', toe)
        self.add_arc('pad', PAD_L, PAD_R, radius_x=PAD_RX, radius_y=PAD_RY, sweep=True)
        # palm-up hand
        self.add_arc('palm-upper', (4, 28), (14, 24), radius_x=10, radius_y=4)
        self.add_line('thumb-top-l', (14, 24), PAD_L)
        self.add_line('thumb-top-c', PAD_L, PAD_R)
        self.add_arc('thumb-tip-upper', PAD_R, (32, 28), radius_x=4)
        self.add_arc('thumb-tip-lower', (32, 28), (28, 32), radius_x=4)
        self.add_line('thumb-bottom', (28, 32), (18, 32))
        self.add_contour('thumb', 'palm-upper', 'thumb-top-l', 'thumb-top-c', 'thumb-tip-upper', 'thumb-tip-lower', 'thumb-bottom')
        self.relate('connect', 'pad', 'thumb-top-l')
        self.relate('connect', 'pad', 'thumb-top-c')
        self.relate('connect', 'pad', 'thumb-tip-upper')
        self.add_line('fingers-upper', (32, 28), (38, 28))
        self.add_arc('fingertips', (38, 28), (44, 32), radius_x=6)
        self.add_line('fingers-lower', (44, 32), (34, 40))
        self.add_line('palm-base', (34, 40), (12, 40))
        self.add_line('wrist-lower', (12, 40), (4, 38))
        self.add_contour('hand', 'fingers-upper', 'fingertips', 'fingers-lower', 'palm-base', 'wrist-lower')
        self.relate('connect', 'thumb', 'hand')
