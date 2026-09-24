"""Mirror-symmetric tapered glass with tangent bottom rounding. Water is a single gentle cubic wave, avoiding the old kink between half ellipses.
Construction: Lucide glass-water original/atomic-debug: tapered walls and a coherent water surface.
Omissions: No defining feature omitted.
Keyshape VRECT_L: exact contract extremes, stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='34a460c1-99e1-4757-9b55-ce2bf85e1d92'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tapered-glass-of-water/20260924T160711Z-thuan-mac/reference/glass water_34a460c1-99e1-4757-9b55-ce2bf85e1d92.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tapered-glass-of-water'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('tapered', 'glass', 'of', 'water')
    def build(self):
        self.path('glass',(8,4),[('L',(40,4)),('L',(38,20)),('L',(36,36)),('C',(30,44),(35,44),(34,44)),('L',(18,44)),('C',(12,36),(14,44),(13,44)),('L',(10,20)),('L',(8,4))],True)
        self.path('water',(10,20),[('C',(38,20),(19,15),(29,25))]);self.join('glass','water')

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
