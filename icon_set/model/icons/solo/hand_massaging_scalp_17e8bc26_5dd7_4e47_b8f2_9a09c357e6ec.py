"""Hand Massaging Scalp.

Plan: VRECT_L accommodates the descending hand and continuous head/neck.
Grouped the fingers into a broad palm/thumbnail gesture. Lucide hand informed the contour. Preserved upper-right approach.
Reference: original source silhouette; Lucide hand (connected rounded hand silhouette) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage head_17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hand-massaging-scalp-17e8bc26'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('hand-massaging-scalp',)
    keywords = ('hand', 'massaging', 'scalp')

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
        stroke("head", (20,44), [((20,38),), ((16,38),), ((12,34),4,4,True),
            ((12,30),), ((8,30),), ((12,22),), ((18,16),6,6,True)])
        stroke("rear-neck", (34,44), [((34,36),), ((38,28),)])
        stroke("hand", (30,4), [((26,8),), ((18,8),), ((18,16),4,4,False),
            ((28,18),), ((27,26),), ((32,32),5,6,False), ((38,28),6,6,False),
            ((40,20),2,8,False), ((38,12),), ((40,4),)])
        self.relate("connect", "head", "hand")
        self.relate("connect", "rear-neck", "hand")

