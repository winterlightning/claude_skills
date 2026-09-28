'Diagonal wrench: open jaw with rounded inset, round hanging-hole handle. Bounds6,6 to42,42.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ef6a5b2c-1e8c-5ac4-af02-c85d2d6e6b1e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-end-wrench/20260924T093935Z-thuan-mac/reference/wrench_ef6a5b2c-1e8c-5ac4-af02-c85d2d6e6b1e.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide wrench: rounded jaw recess and coherent shaft contour.'
OMISSIONS = 'None'

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
    icon_id = 'open-end-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('wrench',)
    def build(self):
        path(self,'wrench',(33,6),[('L',(25,14)),('A',4,4,False,(25,18)),('L',(29,22)),('A',4,4,False,(33,22)),('L',(42,13)),('C',(42,22),(40,29),(31,29)),('L',(26,38)),('C',(23,41),(20,42),(17,42)),('A',11,11,True,(6,31)),('C',(6,28),(7,25),(9,23)),('L',(20,15)),('C',(20,10),(25,6),(33,6))],True)
        circle(self,'hole',17,31,2)
