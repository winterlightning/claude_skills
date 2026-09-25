"""Horse pulling a small carriage with smooth neck and back, paired legs and round wheel.
Plan: Horse pulling a small carriage with smooth neck and back, paired legs and round wheel.
Construction: Lucide bird fluid animal contours and truck wheel construction; original horse/carriage arrangement retained.
Omissions: Wheel spokes and far-side legs omitted for clear spacing."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '589093c2-50d1-4d6e-b46e-2aef2795cea3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/carriage_589093c2-50d1-4d6e-b46e-2aef2795cea3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='horse-pulling-small-carriage'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('horse', 'pulling', 'small', 'carriage')

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
        path('horse',(4,20),[('L',(8,10)),('C',(16,18),(12,10),(12,18)),('L',(17,18)),('A',(20,21),3,3,True),('L',(20,22)),('L',(20,30)),('L',(16,38))])
        path('foreleg',(10,22),[('L',(10,30)),('L',(6,38))]);line('belly',(10,30),(20,30));join('belly','foreleg');join('belly','horse')
        path('seat',(28,22),[('L',(28,14)),('A',(32,10),4,4,True),('L',(38,10)),('A',(40,12),2,2,True),('L',(40,22))])
        circle('wheel',36,30,8)
        poly('shaft',(20,22),(28,22),(36,22));join('shaft','horse');join('shaft','seat');join('shaft','wheel')
