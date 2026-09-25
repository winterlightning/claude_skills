"""Flamingo with flowing S neck, rounded body, pointed tail and one supporting leg.
Plan: Flamingo with flowing S neck, rounded body, pointed tail and one supporting leg.
Construction: Lucide bird: flowing body silhouette and simple leg strokes.
Omissions: Eye, interior wing and tucked leg omitted for clearance."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '81d15e2a-dffb-4f68-873c-f118f99d99a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flamingo_81d15e2a-dffb-4f68-873c-f118f99d99a6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='flamingo-on-one-leg-batch-045'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('flamingo', 'on', 'one', 'leg', 'batch', '045')

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
        path('neck',(8,14),[('L',(8,11)),('C',(14,4),(8,7),(10,4)),('C',(20,10),(18,4),(20,6)),('C',(10,22),(20,14),(12,18)),('C',(24,30),(8,28),(16,30))])
        path('body',(24,30),[('C',(40,26),(31,30),(37,30)),('C',(29,18),(38,22),(34,18)),('C',(24,30),(24,18),(22,26))],True)
        join('neck','body')
        poly('leg',(28,30),(28,44),(22,44));join('leg','body')
