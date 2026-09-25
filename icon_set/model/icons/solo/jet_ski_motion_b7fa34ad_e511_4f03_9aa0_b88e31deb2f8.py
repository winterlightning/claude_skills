"""Jet ski with smooth bow, straight handle and even water wave.
Plan: Jet ski with smooth bow, straight handle and even water wave.
Construction: No useful exact Lucide match; source motion marks and watercraft layout retained.
Omissions: No additional details added."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='b7fa34ad-e511-4f03-9aa0-b88e31deb2f8'
SOURCE_PATH='pictographic-primitives/symbol/water scooter_b7fa34ad-e511-4f03-9aa0-b88e31deb2f8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='jet-ski-motion'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'symbol'
    aliases=()
    keywords=('jet', 'ski', 'motion')

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
        path('hull',(6,14),[('L',(22,28)),('C',(32,22),(26,27),(30,24)),('L',(24,18)),('L',(12,6))])
        line('handle',(24,18),(24,6));join('handle','hull')
        line('speed-upper',(6,30),(18,38));line('speed-lower',(6,40),(8,42))
        path('water',(28,38),[('C',(35,38),(28,32),(35,32)),('C',(42,38),(35,43),(42,43))])
