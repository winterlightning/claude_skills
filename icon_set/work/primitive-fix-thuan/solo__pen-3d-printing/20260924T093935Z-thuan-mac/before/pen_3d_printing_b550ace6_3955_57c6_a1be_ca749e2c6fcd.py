"""Diagonal 3D pen and filament. Broad cap, tapered lower barrel, integral filament; tiny button and separate nib seam omitted for clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b550ace6-3955-57c6-a1be-ca749e2c6fcd'
SOURCE_PATH = 'pictographic-primitives/technology/3d pen_b550ace6-3955-57c6-a1be-ca749e2c6fcd.svg'
AUTHOR = 'gpt-6'

class Pen3DPrinting(Solo48):
    icon_id = 'pen-3d-printing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('3d-pen', 'pen', '3d-printing', 'drawing', 'filament', 'craft', 'maker')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x,y+r),r)
            arc(n+'b',(x,y+r),(x,y-r),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        arc('cap',(26,8),(38,24),10)
        barrel_points = ((38,24),(22,36),(14,30),(16,20),(26,8))
        for i,(a,b) in enumerate(zip(barrel_points,barrel_points[1:]),1): line(f'barrel-{i}',a,b)
        contour('pen','cap','barrel-1','barrel-2','barrel-3','barrel-4',closed=True)
        arc('filament-a',(14,30),(6,38),8,sweep=False)
        arc('filament-b',(6,38),(10,42),4,sweep=False)
        line('tail',(10,42),(18,42))
        contour('strand','filament-a','filament-b','tail');connect('strand','pen')
