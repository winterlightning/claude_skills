"""Ceiling smoke detector with three rising smoke curls. Square envelope, centerline extremes 6/6/42/42. Keep broad top and tapered body; narrow vent ribs omitted. No exact useful Lucide match; matched alternating arcs form smoke."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '628d3285-a2cf-423e-8680-501bd94b9c31'
SOURCE_PATH = 'pictographic-primitives/technology/safety fire alarm_628d3285-a2cf-423e-8680-501bd94b9c31.svg'
AUTHOR = 'gpt-6'

class SmokeDetectorWithSmoke(Solo48):
    icon_id = 'smoke-detector-with-smoke'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('smoke-detector', 'fire-alarm', 'safety', 'smoke', 'alarm', 'ceiling', 'sensor')

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
        poly('detector',(6,6),(42,6),(36,18),(12,18),closed=True)
        for n,x in [('left',12),('middle',24),('right',36)]:
            arc(n+'-top',(x,28),(x,35),4,4,sweep=False)
            arc(n+'-bottom',(x,35),(x,42),4,4,sweep=True)
            contour(n+'-smoke',n+'-top',n+'-bottom')
