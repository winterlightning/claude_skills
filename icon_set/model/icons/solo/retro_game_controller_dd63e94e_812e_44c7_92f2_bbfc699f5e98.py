"""Tilted retro gamepad. Shared capsule geometry and Lucide gamepad-2 controls; minor lower-edge dip and second tiny button omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd63e94e-812e-44c7-92f2-bbfc699f5e98'
SOURCE_PATH = 'pictographic-primitives/technology/game_dd63e94e-812e-44c7-92f2-bbfc699f5e98.svg'
AUTHOR = 'gpt-6'

class RetroGameController(Solo48):
    icon_id = 'retro-game-controller'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('technology', 'state')
    aliases = ()
    keywords = ('controller', 'gamepad', 'retro', 'game', 'gaming', 'console', 'joypad')

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
        arc('left',(12,15),(22,39),13,sweep=False)
        line('bottom',(22,39),(36,33))
        arc('right',(36,33),(26,9),13,sweep=False)
        line('top',(26,9),(12,15))
        contour('body','left','bottom','right','top',closed=True)
        poly('dpad-h',(13,27),(17,27),(21,27))
        poly('dpad-v',(17,23),(17,27),(17,31));connect('dpad-h','dpad-v')
        self.add_dot('button',(31,21))
