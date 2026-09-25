"""Motion sensor with two widening detection arcs. Portrait envelope; Lucide router-style rounded device. Two slots reduced to dots and three arcs reduced to two."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '24bd37ec-c683-4809-ae11-a3eaebab7a53'
SOURCE_PATH = 'pictographic-primitives/technology/motion sensor_24bd37ec-c683-4809-ae11-a3eaebab7a53.svg'
AUTHOR = 'gpt-6'

class MotionSensorDetectionWaves(Solo48):
    icon_id = 'motion-sensor-detection-waves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('motion-sensor', 'sensor', 'detection', 'waves', 'smart-home', 'security', 'device')

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
        box('sensor',8,4,40,22,4)
        self.add_dot('slot-left',(18,13));self.add_dot('slot-right',(30,13))
        arc('inner-wave',(16,31),(32,31),8,2,sweep=False)
        arc('outer-wave',(8,34),(40,34),16,10,sweep=False)
