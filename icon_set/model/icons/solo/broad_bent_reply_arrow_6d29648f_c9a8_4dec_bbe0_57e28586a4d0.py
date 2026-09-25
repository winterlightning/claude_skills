"""Broad outlined left reply arrow with an upright lower stem.
SQUARE extremes 6,6–42,42; outer and inner bends belong to one contour.
Source supplies the broad silhouette; Lucide corner-up-left supplies tangent bend construction.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "6d29648f-c9a8-4dec-bbe0-57e28586a4d0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/backward_6d29648f-c9a8-4dec-bbe0-57e28586a4d0.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "broad-bent-reply-arrow"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ["Curved Left Reply Arrow"]
    keywords = ["arrow", "reply", "left", "bent", "back", "return", "direction"]
    def build(self):
        members=[]
        def lines(name,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):
                uid=f"{name}-{i}"; self.add_line(uid,a,b); members.append(uid)
        lines("head-top", (6,20),(22,6),(22,14),(30,14))
        self.add_arc("outer-bend", (30,14),(42,26),radius_x=12);members.append("outer-bend")
        lines("stem",(42,26),(42,42),(32,42),(32,34))
        self.add_arc("inner-bend",(32,34),(24,26),radius_x=8,sweep=False);members.append("inner-bend")
        lines("head-bottom",(24,26),(22,26),(22,34),(6,20))
        self.add_contour("arrow", *members,closed=True)
