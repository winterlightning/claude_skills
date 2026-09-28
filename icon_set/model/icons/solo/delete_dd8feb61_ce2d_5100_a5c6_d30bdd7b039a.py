"""A delete mark with an X spanning a circle. Four rational circle junctions share the radius-20 rim; both diagonal strokes split at their common center.
Lucide delete: two coherent diagonal strokes forming X; supplied circular enclosure preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd8feb61-ce2d-5100-a5c6-d30bdd7b039a'
SOURCE_PATH = 'icon_set/work/todo-references/delete_dd8feb61-ce2d-5100-a5c6-d30bdd7b039a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'delete-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('delete',)

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

        nodes=((12,8),(36,8),(36,40),(12,40))
        for j in range(4): self.add_arc('rim-'+str(j),nodes[j],nodes[(j+1)%4],radius_x=20)
        self.add_contour('rim',*('rim-'+str(j) for j in range(4)),closed=True)
        self.add_polyline('slash',(12,8),(24,24),(36,40))
        self.add_polyline('backslash',(36,8),(24,24),(12,40))
        self.relate('connect','slash','backslash')
        self.relate('connect','rim','slash')
        self.relate('connect','rim','backslash')
