"""Two equal lenses measured by a double-ended arrow. HRECT_L reaches (6,8)-(42,40); mirrored circles and arrowheads. No useful exact Lucide match; complete diagram retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e05719aa-f588-4b1a-89c4-699f4a8354ec'
SOURCE_PATH = 'pictographic-primitives/technology/lens distance_e05719aa-f588-4b1a-89c4-699f4a8354ec.svg'
AUTHOR = 'gpt-6'

class LensesWithDistanceArrow(Solo48):
    icon_id = 'lenses-with-distance-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('lens', 'distance', 'measure', 'interpupillary', 'optics', 'headset', 'adjust')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
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
        for x in (11,37):circle(f'lens-{x}',x,15,7)
        line('measure',(11,35),(37,35))
        poly('arrow-left',(16,30),(11,35),(16,40))
        poly('arrow-right',(32,30),(37,35),(32,40))
        connect('measure','arrow-left');connect('measure','arrow-right')
