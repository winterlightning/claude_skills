"""Flexed Bicep.

Plan: HRECT_L gives the bent forearm and bicep a broad horizontal envelope.
Retained fist, elbow and bicep; omitted wrist creases. Lucide biceps-flexed informed the continuous outline.
Reference: original source silhouette; Lucide biceps-flexed (broad elbow and continuous muscle contour) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '703b6005-4aed-50c7-9576-435c35184844'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/arm flex_703b6005-4aed-50c7-9576-435c35184844.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'flexed-bicep-703b6005'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('flexed-bicep',)
    keywords = ('flexed', 'bicep')

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
        stroke("arm", (44,40), [((12,40),), ((4,32),8,8,True), ((8,16),),
            ((20,8),12,8,True), ((24,12),4,4,True), ((18,16),6,4,True),
            ((16,30),), ((30,24),14,6,True), ((40,30),10,6,True), ((44,24),)])

