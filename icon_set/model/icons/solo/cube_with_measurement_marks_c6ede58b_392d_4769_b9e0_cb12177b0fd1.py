"""Isometric cube with one measurement tick on each side face. Square extremes 6/6/42/42. Lucide box face junctions inspected earlier; taller side faces reserve clear space around the two ticks."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6ede58b-392d-4769-b9e0-cb12177b0fd1'
SOURCE_PATH = 'pictographic-primitives/technology/virtual measuring volume_c6ede58b-392d-4769-b9e0-cb12177b0fd1.svg'
AUTHOR = 'gpt-6'

class CubeWithMeasurementMarks(Solo48):
    icon_id = 'cube-with-measurement-marks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('cube', 'measure', 'volume', '3d', 'dimensions', 'box', 'virtual')

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
        poly('cube',(6,14),(24,6),(42,14),(42,34),(24,42),(6,34),closed=True)
        poly('top-face',(6,14),(24,20),(42,14));connect('top-face','cube')
        line('edge',(24,20),(24,42));connect('edge','cube');connect('edge','top-face')
        line('left-tick',(14,27),(16,29));line('right-tick',(32,29),(34,27))
