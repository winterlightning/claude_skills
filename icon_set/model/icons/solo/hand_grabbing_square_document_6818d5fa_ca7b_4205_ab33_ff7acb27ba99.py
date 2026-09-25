"""Hand gripping a document with rounded knuckles and a smooth palm.
Plan: Hand gripping a document with rounded knuckles and a smooth palm.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Fine finger creases omitted; two broad knuckles and document corner retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '6818d5fa-ca7b-4205-ab33-ff7acb27ba99'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/drag drop hand_6818d5fa-ca7b-4205-ab33-ff7acb27ba99.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-grabbing-square-document'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='interface-essential'
    aliases=()
    keywords=('hand', 'grabbing', 'square', 'document')

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
        path('paper',(6,34),[('L',(6,10)),('A',(10,6),4,4,True),('L',(34,6))])
        path('hand',(22,30),[('L',(16,24)),('C',(22,18),(12,18),(17,13)),('L',(26,22)),('L',(30,16)),('C',(36,20),(33,12),(35,18)),('L',(42,28)),('C',(28,42),(42,36),(36,42)),('C',(18,38),(24,42),(21,40)),('L',(15,34)),('L',(19,30))])
