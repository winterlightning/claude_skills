"""Walking person framed by detection waves. Square envelope; Lucide person-standing limb hierarchy. One wave per side replaces the repeated pairs; unequal stride preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fb97392d-0568-4dd6-9a92-c740fd996757'
SOURCE_PATH = 'pictographic-primitives/technology/motion sensor pir_fb97392d-0568-4dd6-9a92-c740fd996757.svg'
AUTHOR = 'gpt-6'

class WalkingPersonSensorWaves(Solo48):
    icon_id = 'walking-person-sensor-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('motion-sensor', 'pir', 'walking', 'person', 'detection', 'waves', 'presence')

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
        circle('head',24,9,3)
        poly('body',(24,21),(22,30),(17,42))
        line('leg',(22,30),(30,42));connect('leg','body')
        poly('arms',(17,28),(24,21),(31,28));connect('arms','body')
        arc('left-top',(8,14),(6,24),2,10,sweep=False);arc('left-bottom',(6,24),(8,34),2,10,sweep=False);contour('left-wave','left-top','left-bottom')
        arc('right-top',(40,14),(42,24),2,10);arc('right-bottom',(42,24),(40,34),2,10);contour('right-wave','right-top','right-bottom')
