"""Fractured Bone.

Plan: SQUARE gives equal room to the two diagonal fracture halves.
Retained double-lobed ends and jagged fracture edges; omitted the impact mark. Lucide bone informed the lobes. Half-turn symmetry.
Reference: original source silhouette; Lucide bone (paired round end lobes) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8cbea4a5-534b-5032-af2e-ceb19429af17'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty broken bone_8cbea4a5-534b-5032-af2e-ceb19429af17.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'fractured-bone-8cbea4a5'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('fractured-bone',)
    keywords = ('fractured', 'bone')

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
        # Two fracture halves related by a half-turn about the canvas center.
        start=(24,12)
        segments=[((30,6),6,6,True), ((36,12),6,6,True),
            ((42,18),6,6,True), ((36,24),6,6,True),
            ((28,22),), ((30,16),), ((24,14),), ((24,12),)]
        for j in range(2):
            def p(v): return v if j==0 else (48-v[0],48-v[1])
            stroke(f"bone-{j}", p(start), [(p(s[0]),*s[1:]) for s in segments], closed=True)

