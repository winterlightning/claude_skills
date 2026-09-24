"""Foot Reflexology Map.

Plan: VRECT_M follows the tall, narrow sole.
Grouped the small toes into one forefoot lobe; omitted toe creases. Retained midfoot and heel divisions. Lucide footprints informed the heel.
Reference: original source silhouette; Lucide footprints (continuous sole and rounded heel) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '190a87c0-f140-4783-889d-2b08bb653fa3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage map foot_190a87c0-f140-4783-889d-2b08bb653fa3.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'foot-reflexology-map-190a87c0'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('foot-reflexology-map',)
    keywords = ('foot', 'reflexology', 'map')

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
        stroke("sole", (10,14), [((16,4),6,10,True), ((22,10),6,6,True),
            ((30,10),4,4,True), ((38,18),8,8,True), ((36,22),), ((34,32),),
            ((24,44),10,12,True), ((10,32),14,12,True), ((10,21),), ((10,14),)], closed=True)
        stroke("arch-map", (10,21), [((24,19),14,8,False), ((36,22),12,8,False)])
        # Region dividers meet exact contour nodes after splitting receiver paths.
        self.relate("connect", "arch-map", "sole")
        stroke("heel-map", (10,32), [((34,32),)])
        self.relate("connect", "heel-map", "sole")

