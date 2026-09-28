"""Left-facing running person detected by an upper-right sensor. Square envelope, centerline extremes 6/6/42/42. Lucide person-standing informs the head/limb hierarchy; running pose rebuilt asymmetrically. Three repeated detection waves reduced to one; sensor is a physical part of the scene."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '772e4b1a-004f-49ee-a794-bc8ff194add3'
SOURCE_PATH = 'pictographic-primitives/technology/school motion sensoring for learning_772e4b1a-004f-49ee-a794-bc8ff194add3.svg'
AUTHOR = 'gpt-6'

class PersonDetectedByMotionSensor(Solo48):
    icon_id = 'person-detected-by-motion-sensor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('motion-sensor', 'person', 'running', 'detection', 'school', 'learning', 'sensor')

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
        poly('sensor',(30,6),(42,6),(42,14),(30,14),closed=True)
        circle('head',13,16,3)
        poly('body',(16,27),(20,34),(14,42),(8,42))
        poly('arm-left',(16,27),(10,30),(6,26));connect('arm-left','body')
        poly('arm-right',(16,27),(23,24));connect('arm-right','body');connect('arm-right','arm-left')
        poly('leg-right',(20,34),(28,38),(30,42));connect('leg-right','body')
        arc('signal',(32,24),(42,24),5,3,sweep=False)
