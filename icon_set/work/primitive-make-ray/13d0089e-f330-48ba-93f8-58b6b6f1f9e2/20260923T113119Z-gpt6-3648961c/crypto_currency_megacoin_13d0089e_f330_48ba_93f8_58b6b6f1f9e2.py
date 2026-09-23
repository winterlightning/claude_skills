"""A Megacoin emblem: circular rim and three separate matching round-headed arches. Radius 20 centered at (24,24); repeated arch widths 6 at step 10. Dense trademark retained for honest spacing review.
No useful local Lucide match for this composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '13d0089e-f330-48ba-93f8-58b6b6f1f9e2'
SOURCE_PATH = 'icon_set/work/todo-references/crypto currency megacoin_13d0089e-f330-48ba-93f8-58b6b6f1f9e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crypto-currency-megacoin'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('crypto', 'currency', 'megacoin')

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

        self.circle('coin',24,24,20)
        for j,x in enumerate((11,21,31)):
            p='arch-'+str(j)
            self.add_line(p+'-left',(x,29),(x,22))
            self.add_arc(p+'-top',(x,22),(x+6,22),radius_x=3)
            self.add_line(p+'-rest-1',(x+6,22),(x+6,29))
            self.add_line(p+'-rest-2',(x+6,29),(x,29))
            self.add_contour(p,p+'-left',p+'-top',p+'-rest-1',p+'-rest-2',closed=True)
