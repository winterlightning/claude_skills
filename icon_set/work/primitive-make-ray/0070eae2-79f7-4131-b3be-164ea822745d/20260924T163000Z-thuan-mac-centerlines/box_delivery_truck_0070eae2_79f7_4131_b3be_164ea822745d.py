"""Box delivery truck with rounded cargo corners and equal wheels with clear separation.
Plan: Box delivery truck with rounded cargo corners and equal wheels with clear separation.
Construction: Lucide truck original and atomic-debug: rounded cargo, angled cabin, circular attached wheels.
Omissions: Window subdivision omitted; wheels separated from body to maintain full interior clearance."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0070eae2-79f7-4131-b3be-164ea822745d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260924T162241Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='box-delivery-truck'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('box', 'delivery', 'truck')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        path('cargo',(6,8),[('L',(23,8)),('A',(25,10),2,2,True),('L',(25,16)),('L',(25,24)),('L',(6,24)),('A',(4,22),2,2,True),('L',(4,10)),('A',(6,8),2,2,True)],True)
        poly('cab',(25,16),(34,16),(44,24),(25,24));join('cab','cargo')
        for name,x in [('rear',12),('front',36)]:circle(name,x,36,4)
