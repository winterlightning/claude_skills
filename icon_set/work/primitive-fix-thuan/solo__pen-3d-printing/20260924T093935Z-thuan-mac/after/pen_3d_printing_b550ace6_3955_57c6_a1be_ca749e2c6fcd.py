'Diagonal 3D printing pen with narrow working tip and flowing filament. Bounds6,6 to42,42.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b550ace6-3955-57c6-a1be-ca749e2c6fcd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pen-3d-printing/20260924T093935Z-thuan-mac/reference/3d pen_b550ace6-3955-57c6-a1be-ca749e2c6fcd.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide pen: diagonal barrel and short nib; source filament curl.'
OMISSIONS = 'Small barrel button omitted for clearance.'

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
    icon_id = 'pen-3d-printing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('3d', 'pen')
    def build(self):
        path(self,'pen',(17,26),[('L',(30,9)),('C',(32,7),(34,6),(36,6)),('A',6,6,True,(42,12)),('C',(42,15),(41,17),(40,19)),('L',(24,32)),('L',(17,26))],True)
        path(self,'nib',(17,26),[('L',(13,31)),('L',(17,35)),('L',(24,32))])
        self.relate('connect','pen','nib')
        path(self,'filament',(13,31),[('C',(9,33),(6,35),(6,38)),('A',4,4,False,(10,42)),('L',(17,42))])
        self.relate('connect','filament','nib')
