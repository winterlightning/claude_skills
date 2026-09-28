'Open infinity arrow with wide equal lobes and smooth diagonal crossing; arrow turns inward above left lobe. Bounds4,10 to44,38.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '507c65f5-f61d-400d-aa16-c3e1eb1af23b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-infinity-arrow/20260924T093935Z-thuan-mac/reference/loop arrow_507c65f5-f61d-400d-aa16-c3e1eb1af23b.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide infinity: equal outer lobes with smooth central progression.'
OMISSIONS = 'Reference opening retained, lobes made taller to meet SOLO48 envelope.'

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
    icon_id = 'open-infinity-arrow'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('loop', 'arrow')
    def build(self):
        path(self,'loop',(31,32),[('C',(37,39),(44,33),(44,24)),('C',(44,16),(40,10),(34,10)),('C',(28,10),(20,38),(14,38)),('C',(8,38),(4,32),(4,24)),('C',(4,16),(8,10),(14,10)),('C',(18,10),(19,14),(21,18))])
        self.add_polyline('arrow',(13,18),(21,18),(21,10))
        self.relate('connect','loop','arrow')
