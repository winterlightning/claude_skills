"""A closed carton marked with a removal cross.
Plan: Symmetric trapezoidal lid, front rectangle and centered X sharing its intersection.
Keyshape visible bounds: (4, 4, 44, 44).
References: ['box'].
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '664d5dec-e292-48a0-b893-09339844ebf6'
SOURCE_PATH = 'icon_set/work/todo-references/box remove_664d5dec-e292-48a0-b893-09339844ebf6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'box-remove'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ()
    keywords = ('box', 'remove')

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
        axis=24
        self.add_polyline("outline",(6,16),(12,6),(36,6),(42,16),(42,42),(6,42),closed=True)
        self.add_line("lid",(6,16),(42,16))
        self.add_line("seam",(axis,6),(axis,16))
        self.relate("connect","outline","lid")
        self.relate("connect","outline","seam")
        self.relate("connect","lid","seam")
        self.add_polyline("cross-a",(20,25),(24,29),(28,33))
        self.add_polyline("cross-b",(28,25),(24,29),(20,33))
        self.relate("connect","cross-a","cross-b")
