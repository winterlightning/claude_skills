"""A horizontal capsule above a right-pointing arrow. Preserve the empty capsule exactly as visible in the supplied reference; no inferred digits. Centerline extremes (4,8)-(44,40).
No useful local Lucide match for this composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94c872cf-8c68-4f83-8b74-b91b3ce122c3'
SOURCE_PATH = 'icon_set/work/todo-references/decrease decimal_94c872cf-8c68-4f83-8b74-b91b3ce122c3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'decrease-decimal'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('decrease', 'decimal')

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

        self.rounded('capsule',4,8,40,20,6)
        self.add_line('shaft',(22,34),(44,34))
        self.add_polyline('arrow',(38,28),(44,34),(38,40))
        self.relate('connect','shaft','arrow')
