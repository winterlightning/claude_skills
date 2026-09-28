"""A pointing hand, index finger raised, beside a double-headed vertical arrow.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the hand is one closed outline: an index finger 8 wide (x
12..20) with a r4 rounded tip reaching y=6, a knuckle ledge out to x=28, the
palm's right side down to a rounded heel, the wrist, and a thumb bulge on
the left. The swipe is a vertical shaft at x=38 from top to bottom edge with
an open arrowhead at each end, 8+ clear of the hand.
Revision: the rejected drawing's short finger on a flat block read as a gun
between two chevrons; the hand now has a tall raised finger and palm, and
the gesture is one continuous up-down arrow.
Construction reference: Lucide `pointer` (raised index finger on a palm)
and `move-vertical` (double-headed arrow).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db37e620-1eb0-4c99-bce3-2c53b5c5fa76'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__one-finger-vertical-swipe-gesture/20260926T160211Z-thuan-mac-1/reference/gesture swipe vertical 3_db37e620-1eb0-4c99-bce3-2c53b5c5fa76.svg'
AUTHOR = 'claude-opus-5-5'

FINGER_L, FINGER_R, TIP_Y, TIP_R = 12, 20, 10, 4
KNUCKLE_Y, PALM_R, HEEL_Y, HEEL_R = 20, 28, 30, 6
WRIST = ((22, 36), (22, 42))
THUMB = ((12, 36), (6, 28), (12, 24))
ARROW_X, ARROW_HEAD = 38, 4


class Drawing(Solo48):
    icon_id = 'one-finger-vertical-swipe-gesture'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('gesture swipe vertical 3', 'swipe up down')
    keywords = ('swipe', 'gesture', 'scroll', 'finger', 'touch', 'vertical', 'hand')

    def build(self):
        self.add_line('finger-left', THUMB[2], (FINGER_L, TIP_Y))
        self.add_arc('fingertip', (FINGER_L, TIP_Y), (FINGER_R, TIP_Y), radius_x=TIP_R, sweep=True)
        self.add_line('finger-right', (FINGER_R, TIP_Y), (FINGER_R, KNUCKLE_Y))
        self.add_line('knuckles', (FINGER_R, KNUCKLE_Y), (PALM_R, KNUCKLE_Y))
        self.add_line('palm-right', (PALM_R, KNUCKLE_Y), (PALM_R, HEEL_Y))
        self.add_arc('heel', (PALM_R, HEEL_Y), WRIST[0], radius_x=HEEL_R, sweep=True)
        self.add_line('wrist-right', WRIST[0], WRIST[1])
        self.add_line('wrist-bottom', WRIST[1], (FINGER_L, WRIST[1][1]))
        self.add_line('wrist-left', (FINGER_L, WRIST[1][1]), THUMB[0])
        self.add_line('thumb-lower', THUMB[0], THUMB[1])
        self.add_line('thumb-upper', THUMB[1], THUMB[2])
        self.add_contour('hand', 'finger-left', 'fingertip', 'finger-right', 'knuckles', 'palm-right', 'heel',
                         'wrist-right', 'wrist-bottom', 'wrist-left', 'thumb-lower', 'thumb-upper', closed=True)
        top, bottom = (ARROW_X, 6), (ARROW_X, 42)
        self.add_line('shaft', top, bottom)
        self.add_polyline('head-up', (ARROW_X - ARROW_HEAD, 6 + ARROW_HEAD), top, (ARROW_X + ARROW_HEAD, 6 + ARROW_HEAD))
        self.add_polyline('head-down', (ARROW_X - ARROW_HEAD, 42 - ARROW_HEAD), bottom, (ARROW_X + ARROW_HEAD, 42 - ARROW_HEAD))
        self.relate('connect', 'shaft', 'head-up')
        self.relate('connect', 'shaft', 'head-down')
