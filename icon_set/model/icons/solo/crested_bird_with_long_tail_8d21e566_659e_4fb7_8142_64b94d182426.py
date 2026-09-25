"""Crested bird with a smooth back, rounded breast and long pointed tail.
Plan: Crested bird with a smooth back, rounded breast and long pointed tail.
Construction: Lucide bird: continuous rounded breast with long diagonal tail.
Omissions: Eye and wing crease omitted to keep breast open."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '8d21e566-659e-4fb7-8142-64b94d182426'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cardinal_8d21e566-659e-4fb7-8142-64b94d182426.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='crested-bird-with-long-tail'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('crested', 'bird', 'with', 'long', 'tail')

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
        path('bird',(6,42),[('L',(17,26)),('C',(28,14),(21,20),(28,20)),('C',(29,6),(30,10),(29,8)),('C',(36,14),(34,8),(36,10)),('L',(42,18)),('L',(36,22)),('C',(26,34),(36,29),(33,34)),('L',(6,42))],True)
        poly('leg',(26,34),(29,42),(34,42));join('leg','bird')
