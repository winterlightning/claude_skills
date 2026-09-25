"""Head Profile with Scalp Divisions.

Plan: VRECT_L allows three generous scalp regions.
Omitted the ear and tiny subdivisions to retain clear region openings. Source scalp arrangement informed the shared crown/temple junction.
Reference: original source silhouette; Lucide ear (coherent open curl) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '120e93f7-4477-4c69-83d2-04f9f32af357'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage map head_120e93f7-4477-4c69-83d2-04f9f32af357.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'head-profile-with-scalp-divisions-120e93f7'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('head-profile-with-scalp-divisions',)
    keywords = ('head', 'profile', 'with', 'scalp', 'divisions')

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
        stroke("scalp", (26,4), [((26,18),), ((34,34),)])
        stroke("temple", (12,18), [((26,18),)])
        self.relate("connect", "head", "scalp")
        self.relate("connect", "head", "temple")
        self.relate("connect", "scalp", "temple")
