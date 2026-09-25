"""Vibrating gamepad with paired motion arcs. Square envelope; Lucide gamepad-2 grip silhouette. Controls omitted, with waves above/below to preserve the haptic subject clearly."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3f48dba1-585e-520b-9cb9-00d5f8e175b5'
SOURCE_PATH = 'pictographic-primitives/technology/haptic sensor vibration controller_3f48dba1-585e-520b-9cb9-00d5f8e175b5.svg'
AUTHOR = 'gpt-6'

class VibratingGameController(Solo48):
    icon_id = 'vibrating-game-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('controller', 'haptic', 'vibration', 'gamepad', 'feedback', 'gaming', 'rumble')

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
        line('top',(12,16),(36,16));arc('tr',(36,16),(42,22),6)
        line('right',(42,22),(42,26));arc('grip-r',(42,26),(30,26),6)
        arc('notch',(30,26),(18,26),6,3,sweep=False)
        arc('grip-l',(18,26),(6,26),6);line('left',(6,26),(6,22));arc('tl',(6,22),(12,16),6)
        contour('gamepad','top','tr','right','grip-r','notch','grip-l','left','tl',closed=True)
        arc('top-a',(16,7),(24,6),8,1);arc('top-b',(24,6),(32,7),8,1);contour('wave-top','top-a','top-b')
        arc('bottom-a',(16,41),(24,42),8,1,sweep=False);arc('bottom-b',(24,42),(32,41),8,1,sweep=False);contour('wave-bottom','bottom-a','bottom-b')
