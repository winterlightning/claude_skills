"""Walking cane user and seated dog. Head centered on upper torso axis, bottom16 to neck24 gives exact 4 ink gap. Dog has smooth back and clear muzzle.
Construction: human_ref/full_body_ref.png: circular head and simple coherent limbs.
Omissions: Facial details, collar, fingers omitted; cane and seated dog remain distinct.
Keyshape HRECT_L: exact contract extremes, stroke 4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID="16b98dc5-5cf7-4f49-9caa-cb2029082676"
SOURCE_PATH="pictographic-primitives/_uncategorized_15/dog for blind_16b98dc5-5cf7-4f49-9caa-cb2029082676.svg"
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='cane-user-beside-seated-guide-dog'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="Uncategorized"
    aliases=()
    keywords=('cane', 'user', 'beside', 'seated', 'guide', 'dog')
    def build(self):
        self.circle('head',28,12,4)
        self.line('torso',(28,24),(28,30))
        self.poly('legs',(26,40),(28,30),(34,40))
        self.poly('arm',(28,24),(32,28),(38,28));self.line('cane',(38,28),(44,40))
        for a,b in [('torso','legs'),('torso','arm'),('arm','cane')]:self.join(a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.path('dog',(4,40),[('C',(8,30),(4,34),(8,34)),('L',(8,24)),('C',(12,22),(8,22),(10,22)),('L',(18,26)),('C',(14,30),(18,29),(16,30)),('L',(14,40))])

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
