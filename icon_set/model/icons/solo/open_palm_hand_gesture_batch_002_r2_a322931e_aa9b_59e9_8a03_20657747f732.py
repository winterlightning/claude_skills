"""Open Palm Hand Gesture -- batch-002 r2 generation.

Subject: an upturned open hand seen from the side, extending right from a
squared wrist. A curved thumb rests on top, a crease separates it from the
palm, and the fingertips are raised at the right, as in an offering or
receiving gesture.

Plan: one closed contour traced clockwise from the wrist foot. The squared
wrist edge rises to the back of the hand. A low thumb hump descends to the
thumb-tip valley K. From K the finger edge sweeps up to a radius-4 fingertip
that turns the top-right corner; the arc's top and right points are the
keyshape's top and right extremes. The palm's underside then sweeps down to
its lowest point and back to the wrist foot. Joins are tangent-continuous
except the deliberate valley at K and the two wrist corners. The crease is a
separate stroke that shares K and runs back under the thumb. It keeps more
than 8 from the thumb's back and from the wrist.
Keyshape HRECT_M; centerline box (4,10)-(44,38).
Deliberate asymmetry: a side view of a hand has no mirror axis.
Reduction: the reference hand is about 2.3:1. The widest SOLO48 envelope is
40x28, so the fingers rise more steeply and the palm is fuller than in the
reference. The thumb's separate rounded tip merges into the valley K,
because a free tip would sit within 4 units of the finger edge. Twenty-one
prototypes were rendered; this one kept the thumb, crease and raised
fingertips legible at 48.
Construction reference: Lucide hand-helping (upturned palm, round fingertip
cap, thumb above the palm) for topology; the reference SVG for the silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import path

SOURCE_ICON_ID = 'a322931e-aa9b-59e9-8a03-20657747f732'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/begging hand ask_a322931e-aa9b-59e9-8a03-20657747f732.svg'
OLDER_BRIEF_REFERENCE = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/business/begging hand ask_a322931e-aa9b-59e9-8a03-20657747f732.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/begging hand ask_a322931e-aa9b-59e9-8a03-20657747f732.svg'
AUTHOR = 'claude-opus-5'

WRIST_X, WRIST_TOP, WRIST_FOOT = 4, 22, 36
THUMB_TOP = (15, 15)
VALLEY = (28, 26)
TIP_CENTER, TIP_RADIUS = (40, 14), 4
PALM_LOW = (26, 38)
CREASE_END = (20, 24)


class OpenPalmHandGestureBatch002R2(Solo48):
    icon_id = 'open-palm-hand-gesture-batch-002-r2'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'body/hands'
    aliases = ('upturned-open-palm', 'begging-hand', 'offering-hand', 'open-hand')
    keywords = ('hand', 'palm', 'gesture', 'offer', 'receive', 'open', 'ask', 'give')

    def build(self) -> None:
        tx, ty = TIP_CENTER
        r = TIP_RADIUS
        tip_top, tip_right = (tx, ty - r), (tx + r, ty)
        path(self, 'hand', (WRIST_X, WRIST_FOOT),
             ('L', (WRIST_X, WRIST_TOP)),
             ('C', (6, 17), (10, 15), THUMB_TOP),
             ('C', (22, 15), (27, 19), VALLEY),
             ('C', (33, 24), (35, 10), tip_top),
             ('A', tip_right, r, r, True),
             ('C', (44, 26), (36, 38), PALM_LOW),
             ('C', (14, 38), (8, 37), (WRIST_X, WRIST_FOOT)),
             closed=True)
        self.add_line('crease', VALLEY, CREASE_END)
        self.relate('connect', 'hand', 'crease')
