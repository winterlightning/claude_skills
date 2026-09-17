"""Hand Massaging Foot.

Plan: VRECT_L accommodates the upright sole and grasping hand.
Retained toe, heel and pressing thumb; omitted pressure marks and individual fingers. Lucide hand and footprints informed the silhouettes.
Reference: original source silhouette; Lucide hand and footprints (continuous gesture and broad sole) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ab52d55-ae52-4c12-82e0-c8e7e2dc8409'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hand-massaging-foot-8ab52d55'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('hand-massaging-foot',)
    keywords = ('hand', 'massaging', 'foot')

    def build(self):

        def stroke(name, start, segments, closed=False):
            members = []
            point = start
            for index, segment in enumerate(segments):
                member = f"{name}-{index}"
                end = segment[0]
                if len(segment) == 1:
                    self.add_line(member, point, end)
                else:
                    rx, ry, sweep = segment[1:4]
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry,
                                 sweep=sweep, large_arc=segment[4] if len(segment)>4 else False)
                members.append(member)
                point = end
            self.add_contour(name, *members, closed=closed)
        stroke("foot", (18,40), [((8,30),10,10,True), ((8,10),),
            ((14,4),6,6,True), ((20,10),6,6,True), ((28,18),8,8,True), ((25,26),)])
        stroke("hand", (28,44), [((28,40),), ((17,29),), ((22,22),5,5,True),
            ((25,26),), ((30,16),), ((40,28),10,12,True), ((40,44),)])
        self.relate("connect", "foot", "hand")

