"""A girl's bust with swept bangs and a side ponytail over rounded shoulders.

Plan: SQUARE (6,6)-(42,42), avatar construction (human_construction = "bust"). Head: r10 circle about (24,16) whose lower half is one semicircular jaw arc resting on the flat body-top line at y=30 (zero visible ink gap, 4 on centerlines). Hair: side-swept bangs, a cubic from the upper-left rim point (16,10) down across the forehead to the right rim point (34,16), where it flows into the ponytail that swings down the right side to (42,25); the hair mass reads in the upper-left crescent between the bangs and the crown. Shoulders: r12 quarter arcs from the body-top ends (18,30)/(30,30) down to the bottom corners (6,42)/(42,42).
Review of the rejected drawing: the head was a ring with two flat hair cubics making a pointed top, a w-shaped mouth and a tiny hook for a ponytail, so it read as a knight's helmet; the original is a girl with bangs, a ponytail and a smile on rounded shoulders.
Omissions: the eyes and smile (an r10 head cannot hold features 8 from a fringe and the jaw); identity carried by the bangs and ponytail as in the set's user busts.
Human reference: icon_set/references/human_ref/user.svg (round head resting on rounded shoulders).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '709fa319-04a9-4baf-a06c-438374603551'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-ponytail-girl-bust/20260928T042731Z-thuan-mac-1/reference/granddaughter_709fa319-04a9-4baf-a06c-438374603551.svg'
AUTHOR = 'claude-fable-5-1'


class SmilingPonytailGirlBust(Solo48):
    icon_id = 'smiling-ponytail-girl-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    human_construction = 'bust'
    aliases = ('granddaughter', 'girl-with-ponytail')
    keywords = ('girl', 'ponytail', 'bust', 'granddaughter', 'avatar', 'young', 'woman')

    def build(self) -> None:
        cx, cy, r = 24, 16, 10
        # jaw: one semicircular arc from the left rim point round the chin to the right rim point
        self.add_arc('jaw', (cx - r, cy), (cx + r, cy), radius_x=r, sweep=False)
        # crown: right rim point up over the top to the left rim point, split at the fringe root (16,10)
        self.add_arc('crown-right', (cx + r, cy), (cx, cy - r), radius_x=r, sweep=False)
        self.add_arc('crown-top', (cx, cy - r), (cx - 8, cy - 6), radius_x=r, sweep=False)
        self.add_arc('crown-left', (cx - 8, cy - 6), (cx - r, cy), radius_x=r, sweep=False)
        self.add_contour('head', 'jaw', 'crown-right', 'crown-top', 'crown-left', closed=True)
        # side-swept bangs from the upper left down to the right temple, flowing into the ponytail
        self.add_bezier('fringe', (cx - 8, cy - 6), ((22, 14), (28, 16), (cx + r, cy)))
        self.relate('connect', 'fringe', 'head')
        self.add_bezier('ponytail', (cx + r, cy), ((40, 16), (42, 20), (42, 25)))
        self.relate('connect', 'ponytail', 'head')
        self.relate('connect', 'ponytail', 'fringe')
        self.add_line('body-top', (18, 30), (30, 30))
        self.add_arc('shoulder-left', (18, 30), (6, 42), radius_x=12, sweep=False)
        self.add_arc('shoulder-right', (30, 30), (42, 42), radius_x=12, sweep=True)
        self.relate('connect', 'body-top', 'shoulder-left')
        self.relate('connect', 'body-top', 'shoulder-right')
        self.relate('connect', 'jaw', 'body-top')
        self.relate('connect', 'head', 'body-top')
