"""Tilted open paint pail with smooth rim, curved base and pointed drop.
Plan: Tilted open paint pail with smooth rim, curved base and pointed drop.
Construction: No useful exact local match inspected; reference sets tilted vessel and detached drop.
Omissions: No handle added; none appears in the source."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '78957ac2-2cd6-40d7-880e-fe1886f1b394'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/color bucket_78957ac2-2cd6-40d7-880e-fe1886f1b394.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tilted-open-paint-pail'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('tilted', 'open', 'paint', 'pail')

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
        path('rim',(25,7),[('L',(37,16)),('A',(39,20),5,5,True),('A',(34,25),5,5,True),('A',(31,24),5,5,True),('L',(19,15)),('A',(17,11),5,5,True),('A',(22,6),5,5,True),('A',(25,7),5,5,True)],True)
        path('pail',(17,11),[('L',(8,26)),('C',(6,33),(6,29),(6,30)),('C',(14,39),(6,37),(10,39)),('C',(34,25),(21,39),(27,31))]);join('pail','rim')
        path('drop',(38,33),[('C',(42,38),(39,34),(42,35)),('A',(34,38),4,4,True),('C',(38,33),(34,35),(37,34))],True)
