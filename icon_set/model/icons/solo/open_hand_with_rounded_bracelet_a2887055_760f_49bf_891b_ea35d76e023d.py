'Open hand wearing a capsule bracelet. Four round tips with pitch8; bracelet centerline height8.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a2887055-760f-49bf-891b-ea35d76e023d'
SOURCE_PATH = 'pictographic-primitives/romance/lgbt bracelet hand_a2887055-760f-49bf-891b-ea35d76e023d.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide hand: shared finger creases and semicircular tips.'
OMISSIONS = 'Bracelet stripes omitted; one capsule retained.'

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
    icon_id = 'open-hand-with-rounded-bracelet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/romance'
    aliases = ()
    keywords = ('lgbt', 'bracelet', 'hand')
    def build(self):
        path(self,'hand',(16,32),[('C',(12,29),(7,27),(4,24)),('A',4,4,True,(12,24)),('L',(12,16)),('A',4,4,True,(20,16)),('L',(20,12)),('A',4,4,True,(28,12)),('L',(28,14)),('A',4,4,True,(36,14)),('L',(36,18)),('A',4,4,True,(44,18)),('C',(44,24),(42,29),(40,32))])
        for x,y in [(20,16),(28,14),(36,18)]:
            self.add_line('crease-'+str(x),(x,y),(x,24));self.relate('connect','hand','crease-'+str(x))
        path(self,'bracelet',(16,32),[('L',(40,32)),('A',4,4,True,(40,40)),('L',(16,40)),('A',4,4,True,(16,32))],True)
        self.relate('connect','hand','bracelet')
