'Side-facing head with rounded oxygen mask, cheek strap and long curved hose. Centerline8,4 to40,44.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '271fffbf-c0f5-4271-aa4c-60ff67604b47'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__oxygen-mask-in-profile-271fffbf/20260924T093935Z-thuan-mac/reference/oxygen mask head side_271fffbf-c0f5-4271-aa4c-60ff67604b47.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'human_ref/user.svg: smooth round head; Lucide stethoscope: round tubing.'
OMISSIONS = 'Eye omitted, source continuous head/neck retained.'

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
    icon_id = 'oxygen-mask-in-profile-271fffbf-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('oxygen', 'mask', 'head', 'side')
    def build(self):
        path(self,'head',(14,20),[('L',(14,17)),('C',(14,10),(20,4),(27,4)),('C',(35,4),(40,10),(40,18)),('C',(40,25),(36,31),(34,35)),('L',(34,44))])
        path(self,'mask',(14,20),[('C',(10,23),(8,25),(8,30)),('C',(8,34),(10,36),(14,36)),('L',(20,36)),('C',(22,33),(23,30),(22,28)),('C',(21,25),(18,22),(14,20))],True)
        self.relate('connect','head','mask')
        self.add_line('strap',(22,28),(31,23));self.relate('connect','strap','mask')
        path(self,'hose',(14,36),[('L',(14,40)),('A',4,4,False,(18,44)),('L',(25,44))])
        self.relate('connect','hose','mask')
