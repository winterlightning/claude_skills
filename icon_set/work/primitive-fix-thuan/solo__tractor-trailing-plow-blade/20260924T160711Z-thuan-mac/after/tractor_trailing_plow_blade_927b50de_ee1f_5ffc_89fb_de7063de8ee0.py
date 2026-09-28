"""Tractor with unequal circular wheels and trailing plow. Cab corners are deliberate; blade is one vertical run flowing into a quarter-circle scoop.
Construction: Lucide tractor original/atomic-debug: unequal wheels and spare raised cab.
Omissions: Wheel hubs and panel detail omitted.
Keyshape HRECT_L: exact contract extremes, stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='927b50de-ee1f-5ffc-89fb-de7063de8ee0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tractor-trailing-plow-blade/20260924T160711Z-thuan-mac/reference/plow_927b50de-ee1f-5ffc-89fb-de7063de8ee0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tractor-trailing-plow-blade'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('tractor', 'trailing', 'plow', 'blade')
    def build(self):
        self.path('body',(16,18),[('L',(16,10)),('A',(18,8),2,2,True),('L',(24,8)),('C',(27,11),(26,8),(26.4,8.8)),('L',(30,22)),('L',(42,22)),('A',(44,24),2,2,True),('L',(44,36))])
        self.circle('rear',20,34,6);self.circle('front',40,36,4);self.join('body','front')
        self.line('hitch',(14,34),(4,34));self.join('rear','hitch')
        self.path('blade',(4,26),[('L',(4,34)),('A',(10,40),6,6,False)]);self.join('blade','hitch')

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
