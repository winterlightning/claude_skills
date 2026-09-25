"""Circular reel with integral curling filament; square extremes (6,6)-(42,42). Asymmetric physical strand; no useful Lucide reel match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6ebf26bb-d83f-5d6b-85d3-0d3a694dbbfe'
SOURCE_PATH = 'pictographic-primitives/technology/3 d print reel_6ebf26bb-d83f-5d6b-85d3-0d3a694dbbfe.svg'
AUTHOR = 'gpt-6'

class FilamentSpoolWithStrand(Solo48):
    icon_id = 'filament-spool-with-strand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('filament', 'spool', 'reel', '3d-printing', 'strand', 'material', 'maker')

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
        arc('reel-a',(34,20),(6,20),14)
        arc('reel-b',(6,20),(34,20),14)
        contour('reel','reel-a','reel-b',closed=True)
        circle('hub',20,20,3)
        arc('strand-a',(34,20),(29,32),18,sweep=True)
        arc('strand-b',(29,32),(34,42),7,sweep=False)
        arc('strand-c',(34,42),(42,34),8,sweep=False)
        contour('strand','strand-a','strand-b','strand-c')
        connect('strand','reel')
