"""Three separated cycling arrows, each with a continuous curved turn and an open two-arm arrowhead. Shared round joins; no doubled arrowhead shaft.
Construction: Lucide recycle original/atomic-debug: separated cyclic arrows and rounded turns.
Omissions: Arrowhead proportions adapted to strict spacing.
Keyshape SQUARE: exact contract extremes, stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='eba86955-13f5-4b0a-a78e-55e6a9fb7a6a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__three-open-recycling-arrows/20260924T160711Z-thuan-mac/reference/recycling symbol_eba86955-13f5-4b0a-a78e-55e6a9fb7a6a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='three-open-recycling-arrows'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('three', 'open', 'recycling', 'arrows')
    def build(self):
        self.path('top',(13,15),[('L',(17,9)),('C',(25,9),(19,5),(22,5)),('L',(34,21))])
        self.poly('top-head',(24,19),(34,21),(38,10));self.join('top','top-head')
        self.path('right',(42,28),[('L',(42,36)),('A',(36,42),6,6,True),('L',(26,42))])
        self.poly('right-head',(32,34),(26,42),(34,42));self.join('right','right-head')
        self.path('left',(16,42),[('L',(12,42)),('A',(6,36),6,6,True),('L',(6,25))])
        self.poly('left-head',(6,33),(6,25),(14,29));self.join('left','left-head')

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
