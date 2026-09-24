'Rounded diagonal pen beside flowing loop signature. Bounds6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f25f2fcc-8f1e-51ec-9c1c-2b8093904cb5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/files/fill and sign_f25f2fcc-8f1e-51ec-9c1c-2b8093904cb5.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide pen: smooth rounded cap and diagonal nib; source loop signature.'
OMISSIONS = 'Extra signature wave omitted.'

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
    icon_id = 'pen-writing-looped-signature'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/agriculture'
    aliases = ()
    keywords = ('fill', 'and', 'sign')
    def build(self):
        path(self,'pen',(6,30),[('L',(10,18)),('L',(17,8)),('C',(18,6),(20,6),(21,6)),('C',(25,6),(28,10),(25,14)),('L',(18,24)),('L',(6,30))],True)
        self.add_line('nib',(10,18),(18,24));self.relate('connect','pen','nib')
        path(self,'signature',(6,42),[('C',(20,42),(36,33),(36,25)),('C',(36,18),(26,25),(27,33)),('C',(28,43),(34,43),(38,38)),('C',(40,42),(41,42),(42,42))])
