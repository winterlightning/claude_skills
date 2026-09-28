"""Head and Throat Section.

Plan: VRECT_L gives four neck/passage edges nine centerline units of separation.
Retained open mouth and two rounded throat bends. Source anatomy guided the drawing; no useful direct Lucide match.
Reference: original source silhouette; human_ref/user.svg construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '116c496d-58c8-4b77-9d43-fdb1d84aa352'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/throat problem_116c496d-58c8-4b77-9d43-fdb1d84aa352.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'head-and-throat-section-116c496d'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('head-and-throat-section',)
    keywords = ('head', 'and', 'throat', 'section')

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
        stroke("skull", (8,24), [((12,16),), ((26,4),14,12,True),
            ((40,18),14,14,True), ((40,26),), ((39,34),1,8,True), ((39,44),)])
        stroke("upper-passage", (8,24), [((20,24),), ((30,34),10,10,True), ((30,44),)])
        stroke("lower-passage", (8,33), [((15,33),), ((21,39),6,6,True), ((21,44),)])
        stroke("chin", (8,33), [((12,37),4,4,False), ((12,44),)])
        self.relate("connect", "skull", "upper-passage")
        self.relate("connect", "chin", "lower-passage")

