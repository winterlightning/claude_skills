"""An acoustic guitar laid diagonally, crossed by a handheld microphone.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the guitar lies on the anti-diagonal x+y=48 and is mirrored
about it ((x, y) -> (48-y, 48-x)). Its lower bout is a r9 circle about
(15,33) that reaches the left and bottom edges; the waist points sit on the
circle at the cardinal offsets (9,0) and (0,-9), and two r6 shoulder arcs
rise from them to the neck root on the axis, so the body pinches into the
figure-eight guitar outline. A dot is the sound hole. The neck is one stroke
up the axis to a rectangular headstock in the top-right corner. The
microphone is a ball head (r5 ring split at a 3-4-5 node) with a straight
handle running down to the right on x-y=6, crossing the neck at an exact
integer point.
Revision: the rejected drawing squashed the guitar into a blob that did not
read (feedback: "guitar"); the body now has a real waist, sound hole, long
neck and headstock.
Construction reference: Lucide `guitar` (waisted body, neck, head) and `mic`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ae731560-756d-4bfe-9aa1-bcd0df250afa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crossed-guitar-microphone/20260926T152509Z-thuan-mac-1/reference/party music_ae731560-756d-4bfe-9aa1-bcd0df250afa.svg'
AUTHOR = 'claude-opus-5-5'

BOUT, BOUT_R = (15, 33), 9
WAIST = (24, 33)            # BOUT + (9, 0); its mirror is BOUT + (0, -9)
ROOT = (21, 27)             # neck root on the axis
SHOULDER_R = 6
HEAD_BASE = (33, 15)        # neck end on the axis
HEAD_HALF = 3               # headstock half-width, in (1,1) steps
HEAD_LEN = 6                # headstock length, in (1,-1) steps
CROSS = (27, 21)            # mic handle (x-y=6) meets the neck here
MIC_C, MIC_R = (16, 11), 5  # ball head; its node MIC_C+(4,3) is on x-y=6
MIC_NODE = (20, 14)
MIC_END = (42, 36)


def m(p):
    """Mirror across the guitar axis x+y=48."""
    return (48 - p[1], 48 - p[0])


class Drawing(Solo48):
    icon_id = 'crossed-guitar-microphone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('party music', 'guitar and microphone')
    keywords = ('music', 'guitar', 'microphone', 'concert', 'band', 'party', 'song', 'live')

    def build(self):
        bx, by = BOUT
        low = (bx, by + BOUT_R)            # (15,42)  bottom
        left = (bx - BOUT_R, by)           # (6,33)   left
        # body: waist -> bottom -> left -> mirrored waist -> shoulder -> root -> shoulder
        self.add_arc('bout-a', WAIST, low, radius_x=BOUT_R, sweep=True)
        self.add_arc('bout-b', low, left, radius_x=BOUT_R, sweep=True)
        self.add_arc('bout-c', left, m(WAIST), radius_x=BOUT_R, sweep=True)
        self.add_arc('shoulder-l', m(WAIST), ROOT, radius_x=SHOULDER_R, sweep=True)
        self.add_arc('shoulder-r', ROOT, WAIST, radius_x=SHOULDER_R, sweep=True)
        self.add_contour('body', 'bout-a', 'bout-b', 'bout-c', 'shoulder-l', 'shoulder-r', closed=True)
        self.add_dot('sound-hole', BOUT)
        # neck and headstock
        self.add_line('neck-low', ROOT, CROSS)
        self.add_line('neck-high', CROSS, HEAD_BASE)
        self.add_contour('neck', 'neck-low', 'neck-high')
        self.relate('connect', 'neck', 'body')
        hx, hy = HEAD_BASE
        b1, b2 = (hx - HEAD_HALF, hy - HEAD_HALF), (hx + HEAD_HALF, hy + HEAD_HALF)
        t1, t2 = (b1[0] + HEAD_LEN, b1[1] - HEAD_LEN), (b2[0] + HEAD_LEN, b2[1] - HEAD_LEN)
        self.add_line('head-base-l', HEAD_BASE, b1)
        self.add_line('head-side-l', b1, t1)
        self.add_line('head-top', t1, t2)
        self.add_line('head-side-r', t2, b2)
        self.add_line('head-base-r', b2, HEAD_BASE)
        self.add_contour('head', 'head-base-l', 'head-side-l', 'head-top', 'head-side-r', 'head-base-r', closed=True)
        self.relate('connect', 'neck', 'head')
        # microphone
        cx, cy = MIC_C
        pts = [MIC_NODE, (cx - MIC_R, cy), (cx + MIC_R, cy)]
        self.add_arc('mic-head-a', MIC_NODE, (cx - MIC_R, cy), radius_x=MIC_R, sweep=True)
        self.add_arc('mic-head-b', (cx - MIC_R, cy), (cx + MIC_R, cy), radius_x=MIC_R, sweep=True)
        self.add_arc('mic-head-c', (cx + MIC_R, cy), MIC_NODE, radius_x=MIC_R, sweep=True)
        self.add_contour('mic-head', 'mic-head-a', 'mic-head-b', 'mic-head-c', closed=True)
        self.add_line('mic-handle-a', pts[0], CROSS)
        self.add_line('mic-handle-b', CROSS, MIC_END)
        self.add_contour('mic-handle', 'mic-handle-a', 'mic-handle-b')
        self.relate('connect', 'mic-handle', 'mic-head')
        self.relate('connect', 'mic-handle', 'neck')
