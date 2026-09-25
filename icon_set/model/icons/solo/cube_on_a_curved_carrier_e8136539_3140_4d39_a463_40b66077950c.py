"""Isometric cube on a smooth symmetric carrier with two support legs.
Plan: Isometric cube on a smooth symmetric carrier with two support legs.
Construction: No useful exact local match; mirrored carrier and straight isometric cube from source.
Omissions: Outlined feet reduced to paired support strokes."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'e8136539-3140-4d39-a463-40b66077950c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon web service fargate_e8136539-3140-4d39-a463-40b66077950c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='cube-on-a-curved-carrier'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('cube', 'on', 'a', 'curved', 'carrier')

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
        poly('cube',(24,4),(34,10),(34,20),(24,26),(14,20),(14,10),closed=True)
        poly('planes',(14,10),(24,16),(34,10));line('edge',(24,16),(24,26))
        join('planes','cube');join('edge','planes');join('edge','cube')
        path('carrier',(8,28),[('C',(16,37),(8,32),(12,35)),('C',(24,39),(20,39),(21,39)),('C',(32,37),(27,39),(28,39)),('C',(40,28),(36,35),(40,32))])
        for side,x,end in [('left',16,12),('right',32,36)]:line(side+'-leg',(x,37),(end,44));join(side+'-leg','carrier')
