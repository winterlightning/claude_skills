"""A browser window with a dollar sign at the right.
Plan: Square window and header; dollar kept right aligned.
Keyshape visible bounds: (4, 4, 44, 44).
References: ['panels-top-left', 'dollar-sign'].
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '150d4701-3c3f-45a7-a26d-8c580a891da1'
SOURCE_PATH = 'icon_set/work/todo-references/browser dollar sign right_150d4701-3c3f-45a7-a26d-8c580a891da1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'browser-dollar-sign-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('browser', 'dollar', 'sign', 'right')

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
        self.browser()
        self.dollar(30,22)
