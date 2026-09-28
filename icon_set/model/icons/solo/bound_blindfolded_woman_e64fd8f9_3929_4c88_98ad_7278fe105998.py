"""Blindfolded woman with circular head, paired hair arcs and bound shoulder outline. Head bottom26 and shoulder top34 leave exact 4 ink gap.
Construction: human_ref/user.svg: circular head and broad curved shoulders.
Omissions: Mouth and rope hatching omitted; blindfold and diagonal binding retained.
Keyshape SQUARE: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e64fd8f9-3929-4c88-98ad-7278fe105998'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/kidnapping woman_e64fd8f9-3929-4c88-98ad-7278fe105998.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='bound-blindfolded-woman'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases=()
    keywords=('bound', 'blindfolded', 'woman')
    def build(self):
        self.circle('head',24,16,10)
        self.line('blindfold',(14,16),(34,16));self.join('head','blindfold')
        for side in (-1,1):
         self.path('hair'+str(side),(24+side*10,16),[('C',(24+side*18,26),(24+side*10,21),(24+side*14,25))])
         self.join('hair'+str(side),'head');self.join('hair'+str(side),'blindfold')
        self.path('binding',(6,42),[('C',(16,34),(6,38),(11,34)),('L',(26,34)),('L',(32,34)),('C',(42,42),(37,34),(42,38)),('L',(18,42)),('L',(6,42))],True)
        self.line('wrap',(18,42),(26,34));self.join('binding','wrap')

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
