"""Hand gripping a straight fire-drill shaft above a capsule-shaped log.
Plan: Hand gripping a straight fire-drill shaft above a capsule-shaped log.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Tiny sparks and repeated finger divisions omitted."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e94edbaf-c94d-4cdc-a976-817dfd2498ef'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-drill-fire-log/20260924T162241Z-thuan-mac/reference/outdoors camp fire make_e94edbaf-c94d-4cdc-a976-817dfd2498ef.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-drill-fire-log'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('hand', 'drill', 'fire', 'log')

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
        path('log',(11,32),[('L',(20,32)),('L',(37,32)),('A',(42,37),5,5,True),('A',(37,42),5,5,True),('L',(11,42)),('A',(6,37),5,5,True),('A',(11,32),5,5,True)],True)
        line('stick',(20,6),(20,32));join('stick','log')
        path('hand',(42,12),[('L',(32,12)),('C',(24,6),(28,12),(28,6)),('L',(20,6)),('L',(16,6)),('A',(12,10),4,4,False),('L',(12,16)),('L',(12,20)),('A',(16,24),4,4,False),('L',(42,24))]);join('stick','hand')
        line('finger',(12,16),(24,16));join('finger','hand');join('finger','stick')
