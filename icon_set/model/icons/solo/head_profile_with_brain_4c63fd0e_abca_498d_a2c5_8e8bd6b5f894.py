"""Head Profile with Brain.

Plan: SQUARE widens the cranium enough for a readable brain contour.
Retained a single broad brain bean; omitted folds. Lucide brain informed smooth lobes; the source owns the right-facing profile.
Reference: original source silhouette; Lucide brain (rounded lobes) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c63fd0e-abca-498d-a2c5-8e8bd6b5f894'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dementia disorder symptoms_4c63fd0e-abca-498d-a2c5-8e8bd6b5f894.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'head-profile-with-brain-4c63fd0e'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('head-profile-with-brain',)
    keywords = ('head', 'profile', 'with', 'brain')

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
        stroke("head", (16,42), [((16,36),), ((6,22),10,14,True),
            ((24,6),18,16,True), ((38,20),14,14,True), ((42,28),),
            ((38,28),), ((38,32),), ((32,38),6,6,True), ((32,42),)])
        stroke("brain", (16,22), [((23,15),7,7,True), ((29,21),6,6,True),
            ((21,25),8,4,True), ((16,22),5,3,True)], closed=True)
