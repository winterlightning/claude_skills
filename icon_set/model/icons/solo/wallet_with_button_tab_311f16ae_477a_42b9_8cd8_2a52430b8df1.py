"""Wallet with a button tab, complete bottom edge and consistent round corners.
Plan: Wallet with a button tab, complete bottom edge and consistent round corners.
Construction: Lucide wallet original and atoms: rounded main body, semicircular tab and hidden side wall.
Omissions: Upper fold seam omitted to preserve button clearance."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '311f16ae-477a-42b9-8cd8-2a52430b8df1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/ewallet_311f16ae-477a-42b9-8cd8-2a52430b8df1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='wallet-with-button-tab'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('wallet', 'with', 'button', 'tab')

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
        path('wallet',(40,16),[('L',(40,12)),('A',(36,8),4,4,False),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,36)),('A',(8,40),4,4,False),('L',(36,40)),('A',(40,36),4,4,False),('L',(40,32))])
        poly('tab-straight',(30,16),(40,16),(44,16),(44,32),(40,32),(30,32))
        path('tab-round',(30,32),[('A',(22,24),8,8,True),('A',(30,16),8,8,True)]);join('tab-round','tab-straight');join('wallet','tab-straight');self.add_dot('button',(34,24))
