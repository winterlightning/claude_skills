"""Six outlined Braille dots arranged in two columns and three rows. Repeated radius-4 circles at x12/36 and y8/24/40. Centerline extremes (8,4)-(40,44).
No useful local Lucide match for this composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b450c082-3a12-488f-997d-8929b3fc010c'
SOURCE_PATH = 'icon_set/work/todo-references/disability braille_b450c082-3a12-488f-997d-8929b3fc010c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'disability-braille'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('disability', 'braille')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, l, t, r, b, radius):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
        for j in range(8):
            if j%2: self.add_arc(name+str(j),pts[j],pts[j+1],radius_x=q)
            else: self.add_line(name+str(j),pts[j],pts[j+1])
        self.add_contour(name, *(name+str(j) for j in range(8)), closed=True)

    def build(self):

        for col,x in enumerate((12,36)):
            for row,y in enumerate((8,24,40)):
                self.circle('dot-'+str(col)+'-'+str(row),x,y,4)
