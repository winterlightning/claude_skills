'Four rounded fingers and left thumb on a broad smooth open palm. Shared finger radius4 and pitch8. Horizontal envelope accommodates five digits.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '92d8dd38-d4cf-4c21-a6ee-c09f59061b77'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-hand-palm-solo/20260924T093935Z-thuan-mac/reference/hand 1_92d8dd38-d4cf-4c21-a6ee-c09f59061b77.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide hand: four rounded fingertips with shared seams; source palm.'
OMISSIONS = 'Wrist line retained; no palm crease.'

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
    icon_id = 'open-hand-palm-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hand', '1')
    def build(self):
        path(self,'hand',(12,27),[('L',(12,16)),('A',4,4,True,(20,16)),('L',(20,12)),('A',4,4,True,(28,12)),('L',(28,14)),('A',4,4,True,(36,14)),('L',(36,18)),('A',4,4,True,(44,18)),('L',(44,28)),('A',12,12,True,(32,40)),('L',(23,40)),('C',(15,40),(4,32),(4,27)),('C',(4,22),(10,22),(12,27))],True)
        for x,y in [(20,16),(28,14),(36,18)]:
            self.add_line('crease-'+str(x),(x,y),(x,25))
            self.relate('connect','hand','crease-'+str(x))
