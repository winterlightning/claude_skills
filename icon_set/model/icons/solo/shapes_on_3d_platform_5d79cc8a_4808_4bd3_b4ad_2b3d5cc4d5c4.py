"""Cone and cylinder on a perspective platform. Square extremes 6/6/42/42. Lucide box-inspired perspective and cylinder construction inspected earlier; platform thickness omitted and cone simplified to a triangle to preserve both solids."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5d79cc8a-4808-4bd3-b4ad-2b3d5cc4d5c4'
SOURCE_PATH = 'pictographic-primitives/technology/tools reality kit_5d79cc8a-4808-4bd3-b4ad-2b3d5cc4d5c4.svg'
AUTHOR = 'gpt-6'

class ShapesOn3DPlatform(Solo48):
    icon_id = 'shapes-on-3d-platform'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('platform', 'shapes', 'cone', 'cylinder', '3d', 'reality-kit', 'scene')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x+r,y),r)
            arc(n+'b',(x+r,y),(x,y+r),r)
            arc(n+'c',(x,y+r),(x-r,y),r)
            arc(n+'d',(x-r,y),(x,y-r),r)
            contour(n,n+'a',n+'b',n+'c',n+'d',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        poly('cone',(6,26),(14,14),(22,26),closed=True)
        arc('cylinder-top',(30,10),(42,10),6,4)
        arc('cylinder-rim',(42,10),(30,10),6,4)
        contour('rim','cylinder-top','cylinder-rim',closed=True)
        line('cylinder-left',(30,10),(30,22));line('cylinder-right',(42,22),(42,10))
        arc('cylinder-base',(30,22),(42,22),6,4,sweep=False);contour('cylinder','cylinder-left','cylinder-base','cylinder-right');connect('cylinder','rim')
        poly('platform',(6,34),(24,42),(42,34))
