"""Tree has a smooth crown, straight trunk, level branch and equal vertical swing ropes. Crown lobes meet at intended valleys; each lobe itself is smooth.
Construction: Lucide tree-deciduous original/atomic-debug: few broad crown lobes and straight trunk.
Omissions: Minor twigs omitted; right-side swing preserves source asymmetry.
Keyshape SQUARE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/family outdoors swing tree_a0e1d015-0d2b-46ee-8ddb-cda6d8f61feb.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tree-with-hanging-swing-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    categories = ("primitives", "kids")
    aliases=()
    keywords=('tree', 'with', 'hanging', 'swing', 'solo', 'b016')
    def build(self):
        self.path('crown',(6,25),[('L',(6,18)),('A',(13,11),7,7,True),('C',(20,6),(13,8),(16,6)),('C',(27,11),(24,6),(27,8)),('C',(29,21),(35,11),(36,18))])
        self.poly('trunk',(16,20),(16,30),(16,42))
        self.poly('branch',(16,30),(30,30),(40,30),(42,30));self.join('trunk','branch')
        self.poly('swing',(30,30),(30,42),(40,42),(40,30));self.join('branch','swing')

    def path(self,n,p,steps,closed=False):
        ids=[]
        for j,step in enumerate(steps):
            k,q,*v=step; uid=f'{n}-{j}'
            if k=='L': self.add_line(uid,p,q)
            elif k=='A': self.add_arc(uid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif k=='C': self.add_bezier(uid,p,(v[0],v[1],q))
            ids.append(uid);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=2):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def line(self,n,a,b): self.add_line(n,a,b)
    def poly(self,n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
    def join(self,a,b): self.relate('connect',a,b)
