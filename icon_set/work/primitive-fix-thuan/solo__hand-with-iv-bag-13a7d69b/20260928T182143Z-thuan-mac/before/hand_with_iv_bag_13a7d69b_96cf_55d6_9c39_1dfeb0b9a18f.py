"""Hand with IV Bag.

Plan: VRECT_L separates the bag, connecting tube and horizontal palm.
Omitted hanger, bag markings and finger creases. Kept an open palm contour with a clear tube attachment. Lucide hand informed the palm.
Reference: original source silhouette; Lucide hand (open palm silhouette) construction.
Human guidance: human_ref/user.svg and full_body_ref.png; continuous anatomical
necks and isolated body parts, so no detached stick-figure head gap applies.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13a7d69b-96cf-55d6-9c39-1dfeb0b9a18f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/transfusion hand_13a7d69b-96cf-55d6-9c39-1dfeb0b9a18f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hand-with-iv-bag-13a7d69b'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('hand-with-iv-bag',)
    keywords = ('hand', 'with', 'iv', 'bag')

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
        stroke("bag", (14,4), [((26,4),), ((30,8),4,4,True), ((30,18),),
            ((26,22),4,4,True), ((20,22),), ((14,22),), ((10,18),4,4,True),
            ((10,8),), ((14,4),4,4,True)], closed=True)
        stroke("tube", (20,22), [((20,31),)])
        stroke("hand", (8,44), [((8,34),), ((20,31),12,8,True),
            ((28,34),8,5,True), ((32,34),)])
        stroke("palm", (8,44), [((25,44),), ((32,42),7,2,False),
            ((40,34),)])
        self.relate("connect", "hand", "palm")
        self.relate("connect", "bag", "tube")
        self.relate("connect", "hand", "tube")

