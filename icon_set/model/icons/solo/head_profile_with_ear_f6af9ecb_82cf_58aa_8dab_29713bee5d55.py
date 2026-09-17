"""Head Profile with Ear.

Plan: VRECT_L allows one clear open ear curl inside the skull.
Omitted the enclosed inner ear fold. Lucide ear informed the open curl.
Reference: original source silhouette; Lucide ear (open outer curl) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6af9ecb-82cf-58aa-8dab-29713bee5d55'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/wearable hearing aid_f6af9ecb-82cf-58aa-8dab-29713bee5d55.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'head-profile-with-ear-f6af9ecb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('head-profile-with-ear',)
    keywords = ('head', 'profile', 'with', 'ear')

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
        stroke("ear", (23,21), [((31,21),4,4,True), ((26,29),5,8,True)])

