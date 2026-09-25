"""Pistol drill on bent support. Lucide drill rounded motor and projecting bit; asymmetric tool direction. Motor subdivision omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '36473314-e81e-4c52-8234-73a3b29780e7'
SOURCE_PATH = 'pictographic-primitives/technology/drill robot arm_36473314-e81e-4c52-8234-73a3b29780e7.svg'
AUTHOR = 'gpt-6'

class DrillOnSupportArm(Solo48):
    icon_id = 'drill-on-support-arm'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('drill', 'robot-arm', 'power-tool', 'industrial', 'machine', 'automation', 'tool')

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
        line('top',(14,6),(30,6))
        arc('nose-top',(30,6),(36,12),6)
        arc('nose-bottom',(36,12),(30,18),6)
        line('underside',(30,18),(23,18))
        grip_points = ((23,18),(19,22),(22,34),(13,34),(6,16))
        for i,(a,b) in enumerate(zip(grip_points,grip_points[1:]),1): line(f'grip-{i}',a,b)
        line('rear',(6,16),(6,14))
        arc('back',(6,14),(14,6),8)
        contour('drill','top','nose-top','nose-bottom','underside','grip-1','grip-2','grip-3','grip-4','rear','back',closed=True)
        line('bit',(36,12),(42,12)); connect('bit','drill')
        poly('support',(17,34),(20,42),(30,42));connect('support','drill')
