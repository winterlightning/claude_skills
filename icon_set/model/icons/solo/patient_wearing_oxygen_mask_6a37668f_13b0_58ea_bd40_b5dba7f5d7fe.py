'Frontal oxygen-mask patient: round upper head, rounded mask, broad open shoulders and hose crossing chest. Head bottom28 to shoulder apex36 gives4-unit ink gap. Bounds6,6 to42,42.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6a37668f-13b0-58ea-bd40-b5dba7f5d7fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/oxygen mask head_6a37668f-13b0-58ea-bd40-b5dba7f5d7fe.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'human_ref/user.svg: round head and broad curved shoulders; Lucide stethoscope: hose turn.'
OMISSIONS = 'Small valve ring omitted; open shoulders and actual hose crossing preserved.'

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
    icon_id = 'patient-wearing-oxygen-mask-6a37668f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('oxygen', 'mask', 'head')
    def build(self):
        path(self,'head',(14,24),[('C',(13,22),(13,20),(13,17)),('A',11,11,True,(24,6)),('A',11,11,True,(35,17)),('C',(35,20),(35,22),(34,24))])
        path(self,'mask',(24,15),[('C',(28,15),(34,22),(34,24)),('C',(34,27),(28,28),(24,28)),('C',(20,28),(14,27),(14,24)),('C',(14,22),(20,15),(24,15))],True)
        self.relate('connect','head','mask')
        path(self,'shoulders',(6,42),[('C',(6,38),(14,36),(24,36)),('C',(34,36),(42,38),(42,42))])
        path(self,'hose',(24,28),[('L',(24,36)),('A',6,6,False,(30,42))])
        self.relate('connect','hose','mask');self.relate('connect','hose','shoulders')
