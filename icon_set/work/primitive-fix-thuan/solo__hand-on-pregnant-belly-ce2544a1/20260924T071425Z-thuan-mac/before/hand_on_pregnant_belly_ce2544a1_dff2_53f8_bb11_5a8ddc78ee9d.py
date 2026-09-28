"""Hand on Pregnant Belly.

Plan: VRECT_L preserves the upright torso and prominent left-facing belly.
Retained broad abdomen and bent resting arm; omitted fingers. Shared human-reference curves informed the limb.
Reference: original source silhouette; human_ref/full_body_ref.png (coherent curved limb) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce2544a1-dff2-53f8-bb11-5a8ddc78ee9d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pregnancy pregnant_ce2544a1-dff2-53f8-bb11-5a8ddc78ee9d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hand-on-pregnant-belly-ce2544a1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('hand-on-pregnant-belly',)
    keywords = ('hand', 'on', 'pregnant', 'belly')

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
        stroke("belly", (18,4), [((18,12),8,8,False), ((8,28),10,16,False),
            ((18,40),10,12,False), ((18,44),)])
        stroke("arm", (30,4), [((26,17),12,17,True), ((19,24),),
            ((23,31),5,5,False), ((36,22),13,9,False)])
        stroke("back", (40,4), [((40,14),), ((36,22),), ((40,44),4,22,False)])

        self.relate("connect", "arm", "back")
