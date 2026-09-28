"""A framed group of three busts, one above two.

HRECT_L extrema (4,8)-(44,40). Heads share radius 3, lower pair mirrors
about x=24. Human user.svg guides circular heads and short shoulders; Lucide
users-round guides the overlapping group rhythm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "3c4dd908-5e55-4361-8d6c-404a2e82e0b6"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/contact family_3c4dd908-5e55-4361-8d6c-404a2e82e0b6.svg"
AUTHOR = "gpt-6"


class ThreePersonGroupIcon(Solo48):
    icon_id = "three-person-group-icon"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("family contact", "group profile")
    keywords = ("three", "people", "users", "team")

    def build(self) -> None:
        p=[(8,8),(40,8),(44,12),(44,36),(40,40),(36,40),(30,40),(18,40),(12,40),(8,40),(4,36),(4,12),(8,8)]
        parts=[]
        for i,(a,b) in enumerate(zip(p,p[1:])):
            n=f"frame-{i}"
            if i in (1,3,9,11):self.add_arc(n,a,b,radius_x=4,radius_y=4,sweep=True)
            else:self.add_line(n,a,b)
            parts.append(n)
        self.add_contour("frame",*parts,closed=True)
        def head(name,x,y):
            r=3; pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]; members=[]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                n=f"{name}-{i}";self.add_arc(n,a,b,radius_x=r,radius_y=r,sweep=True);members.append(n)
            self.add_contour(name,*members,closed=True)
        head("head-back",24,19)
        for name,x in (("head-left",15),("head-right",33)):
            head(name,x,29)
        self.add_line("back-shoulder-left",(24,22),(15,26))
        self.add_line("back-shoulder-right",(24,22),(33,26))
        self.relate("connect","head-back","back-shoulder-left")
        self.relate("connect","head-back","back-shoulder-right")
        self.relate("connect","head-left","back-shoulder-left")
        self.relate("connect","head-right","back-shoulder-right")
        for side,x in (("left",15),("right",33)):
            for direction,foot in (("outer",x-3),("inner",x+3)):
                n=f"{side}-shoulder-{direction}"
                self.add_line(n,(x,32),(foot,40))
                self.relate("connect",n,f"head-{side}")
                self.relate("connect",n,"frame")
