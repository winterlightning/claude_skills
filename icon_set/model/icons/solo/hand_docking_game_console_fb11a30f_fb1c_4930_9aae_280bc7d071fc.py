"""A rounded hand grip lowers a game console into a clean dock.
Plan: A rounded hand grip lowers a game console into a clean dock.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Buttons and individual fingers omitted; stacked console/dock and grip retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'fb11a30f-fb1c-4930-9aae-280bc7d071fc'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-11/switch dock_fb11a30f-fb1c-4930-9aae-280bc7d071fc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-docking-game-console'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'video-games'
    aliases=()
    keywords=('hand', 'docking', 'game', 'console')

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
        path('hand',(18,6),[('L',(18,14)),('L',(18,16)),('A',(26,16),4,4,False),('L',(26,14)),('L',(26,6))])
        path('console-left',(18,14),[('L',(10,14)),('A',(6,18),4,4,False),('L',(6,34))])
        path('console-right',(26,14),[('L',(38,14)),('A',(42,18),4,4,True),('L',(42,34))])
        path('dock',(6,34),[('A',(10,30),4,4,True),('L',(38,30)),('A',(42,34),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,34))],True)
        for n in ('console-left','console-right'):join(n,'hand');join(n,'dock')
