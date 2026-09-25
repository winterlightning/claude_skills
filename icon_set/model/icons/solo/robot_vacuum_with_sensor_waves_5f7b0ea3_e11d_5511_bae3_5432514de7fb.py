"""Perspective robot vacuum with cylindrical rim and sensor waves. Square envelope; Lucide cylinder elliptical top/rim construction. Inner oval reduced to a sensor dot and small bumper omitted; one wave per side."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5f7b0ea3-e11d-5511-bae3-5432514de7fb'
SOURCE_PATH = 'pictographic-primitives/technology/iot electronics robot vacuum_5f7b0ea3-e11d-5511-bae3-5432514de7fb.svg'
AUTHOR = 'gpt-6'

class RobotVacuumWithSensorWaves(Solo48):
    icon_id = 'robot-vacuum-with-sensor-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('robot-vacuum', 'vacuum', 'cleaner', 'smart-home', 'appliance', 'sensor', 'iot')

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
        arc('top-back',(6,23),(42,23),18,9)
        arc('top-front',(42,23),(6,23),18,9)
        contour('top','top-back','top-front',closed=True)
        line('rim-left',(6,23),(6,33))
        arc('rim-bottom',(6,33),(42,33),18,9,sweep=False)
        line('rim-right',(42,33),(42,23));contour('rim','rim-left','rim-bottom','rim-right');connect('rim','top')
        self.add_dot('sensor',(24,23))
        arc('wave-left',(8,8),(14,6),6,2)
        arc('wave-right',(34,6),(40,8),6,2)
