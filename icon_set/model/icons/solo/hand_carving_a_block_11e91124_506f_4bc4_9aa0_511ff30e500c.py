"""Hand carving a block with a diagonal chisel and smooth grip.
Plan: Hand carving a block with a diagonal chisel and smooth grip.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Finger creases omitted; tool edge and block retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '11e91124-506f-4bc4-9aa0-511ff30e500c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carving_11e91124-506f-4bc4-9aa0-511ff30e500c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-carving-a-block'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('hand', 'carving', 'a', 'block')

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
        path('block',(6,42),[('L',(18,42)),('L',(42,42)),('L',(42,38)),('A',(38,34),4,4,False),('L',(26,34))])
        poly('chisel-left',(12,34),(20,22));poly('chisel-right',(34,26),(26,34),(18,42));join('chisel-right','block')
        path('hand',(26,6),[('L',(34,6)),('C',(42,12),(38,6),(40,9)),('L',(34,26)),('C',(26,18),(25,26),(23,21)),('L',(20,22))]);join('hand','chisel-left');join('hand','chisel-right')
