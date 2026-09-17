"""Head Profile.

Plan: VRECT_L preserves an upright profile with broad crown.
Omitted eye and mouth details. Source silhouette and shared human guidance informed the continuous anatomical neck; no useful direct Lucide match.
Reference: original source silhouette; human_ref/user.svg construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '564c7ddf-a799-4385-9cdb-79ed09c375fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/flu_564c7ddf-a799-4385-9cdb-79ed09c375fc.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'head-profile-564c7ddf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('head-profile',)
    keywords = ('head', 'profile')

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
        stroke("head", (20,44), [((20,36),), ((16,36),), ((12,32),4,4,True),
            ((12,26),), ((8,26),), ((12,18),), ((26,4),14,14,True),
            ((40,18),14,14,True), ((40,22),), ((34,34),6,12,True), ((34,44),)])

