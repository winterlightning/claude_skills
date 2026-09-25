"""Headache Profile.

Plan: VRECT_L reserves crown space for two repeated symptom waves.
Retained both waves and the open crown; shortened the waves equally for clearance. No useful direct Lucide match.
Reference: original source silhouette; human_ref/user.svg construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27b13dec-64c9-52f3-b0c7-06e23b9be3cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/medical condition head pain_27b13dec-64c9-52f3-b0c7-06e23b9be3cf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'headache-profile-27b13dec'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('headache-profile',)
    keywords = ('headache', 'profile')

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
        stroke("face", (20,44), [((20,36),), ((16,36),), ((12,32),4,4,True),
            ((12,26),), ((8,26),), ((12,18),), ((15,16),8,8,True)])
        stroke("rear", (38,17), [((40,24),8,12,True), ((34,34),6,10,True), ((34,44),)])
        # Shared two-wave definition; 10-unit horizontal pitch.
        for j in range(2):
            x=22+j*10
            stroke(f"wave-{j}", (x,4), [((x-1,7),3,3,False), ((x,10),3,3,True)])

