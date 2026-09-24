'Whole orange behind a diagonal semicircular slice; upper left leaf and vertical stem. Centerline6,6 to42,42.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fa7b7f99-3071-4d51-9441-0a401cfe97ef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__orange-leaf-slice/20260924T093935Z-thuan-mac/reference/orange grapefruit citrus_fa7b7f99-3071-4d51-9441-0a401cfe97ef.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide citrus: diagonal chord, round rind and radial divider.'
OMISSIONS = 'Double rind and extra segment lines omitted.'

def path(s,n,p,cs,closed=False):
    ids=[]
    for j,c in enumerate(cs):
        eid=f'{n}-{j}';q=c[-1]
        if c[0]=='L':s.add_line(eid,p,q)
        elif c[0]=='A':s.add_arc(eid,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
        elif c[0]=='C':s.add_bezier(eid,p,(c[1],c[2],q))
        ids.append(eid);p=q
    s.add_contour(n,*ids,closed=closed)
def circle(s,n,x,y,r):
    path(s,n,(x-r,y),[('A',r,r,True,(x+r,y)),('A',r,r,True,(x-r,y))],True)

class Drawing(Solo48):
    icon_id = 'orange-leaf-slice'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('orange', 'grapefruit', 'citrus')
    def build(self):
        path(self,'leaf',(6,6),[('C',(16,6),(23,6),(24,15)),('C',(21,16),(18,16),(16,15)),('C',(11,13),(8,10),(6,6))],True)
        self.add_line('stem',(27,6),(27,16))
        self.relate('connect','leaf','fruit')
        path(self,'fruit',(16,15),[('C',(9,20),(6,26),(6,31)),('C',(6,38),(12,42),(18,42))])
        path(self,'top-fruit',(27,16),[('C',(33,16),(36,19),(38,22))])
        self.relate('connect','stem','top-fruit')
        path(self,'slice',(18,42),[('L',(38,22)),('C',(41,25),(42,28),(42,31)),('C',(42,35),(39,38),(35,40)),('C',(33,41),(32,42),(30,42)),('L',(18,42))],True)
        self.relate('connect','slice','fruit');self.relate('connect','slice','top-fruit')
        self.add_line('segment',(28,32),(35,40));self.relate('connect','segment','slice')
