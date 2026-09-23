"""A book with a person emblem on its cover.
Plan: Upright book envelope; circular human head with symmetric bowl arms and central torso.
Keyshape visible bounds: (6, 2, 42, 46).
References: ['book-open', 'human_ref/user.svg'].
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ed961c5-a996-4c78-a7d6-d1d6baa41755'
SOURCE_PATH = 'icon_set/work/todo-references/book person_8ed961c5-a996-4c78-a7d6-d1d6baa41755.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'book-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('book', 'person')

    def rounded(self, p, x, y, w, h, r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2: self.add_arc(f"{p}-{i}",a,b,radius_x=r)
            else: self.add_line(f"{p}-{i}",a,b)
        self.add_contour(p,*(f"{p}-{i}" for i in range(8)),closed=True)

    def browser(self):
        self.rounded("window",6,6,36,36)
        self.add_line("header",(6,14),(42,14))
        self.relate("connect","window","header")

    def dollar(self,x,y):
        # Two tangent semicircles; short top/bottom currency stems.
        self.add_line("dollar-top",(x+4,y),(x,y))
        self.add_arc("dollar-upper",(x,y),(x,y+8),radius_x=4,sweep=False)
        self.add_arc("dollar-lower",(x,y+8),(x,y+16),radius_x=4)
        self.add_line("dollar-bottom",(x,y+16),(x-4,y+16))
        self.add_contour("dollar","dollar-top","dollar-upper","dollar-lower","dollar-bottom")
        for label,a,b in [("stem-top",(x,y-2),(x,y)),("stem-bottom",(x,y+16),(x,y+18))]:
            self.add_line(label,a,b)
            self.relate("connect","dollar",label)

    def euro(self,x):
        # Source has one crossbar. Quarter circles share the true left junction.
        self.add_line("euro-top",(x+3,22),(x,22))
        self.add_arc("euro-upper",(x,22),(x-6,28),radius_x=6,sweep=False)
        self.add_arc("euro-lower",(x-6,28),(x,34),radius_x=6,sweep=False)
        self.add_line("euro-bottom",(x,34),(x+3,34))
        self.add_contour("euro","euro-top","euro-upper","euro-lower","euro-bottom")
        self.add_polyline("crossbar",(x-9,28),(x-6,28),(x+1,28))
        self.relate("connect","euro","crossbar")

    def build(self):
        self.rounded("book",8,4,32,40,3)
        self.add_line("pages",(8,36),(40,36))
        self.relate("connect","book","pages")
        cx,cy,r=24,15,3
        self.add_arc("head-top",(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc("head-bottom",(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour("head","head-top","head-bottom",closed=True)
        self.add_arc("arm-left",(16,26),(24,30),radius_x=10,sweep=False)
        self.add_arc("arm-right",(24,30),(32,26),radius_x=10,sweep=False)
        self.add_contour("arms","arm-left","arm-right")
        self.add_line("torso",(24,26),(24,32))
        self.relate("connect","arms","torso")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")
